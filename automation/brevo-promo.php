#!/usr/bin/env php
<?php
declare(strict_types=1);

/**
 * Promo Phidias — envoi récurrent via l'API Brevo.
 *
 * Crée une campagne Brevo à partir du HTML local puis l'envoie, les dimanche
 * et lundi à 10h (heure de Paris). Prévu pour un cron horaire :
 *
 *     0 * * * 0,1  /usr/bin/php /chemin/automation/brevo-promo.php
 *
 * Le cron tourne toutes les heures ces deux jours ; le script sort
 * immédiatement sauf s'il est 10h à Paris. Cela le rend insensible au fuseau
 * du serveur et au passage heure d'été / heure d'hiver.
 *
 * Modes : --check --lists --test --dry-run --force --help
 */

const API_BASE   = 'https://api.brevo.com/v3';
const TZ         = 'Europe/Paris';
const SEND_HOUR  = 10;

// ---------------------------------------------------------------- utilitaires

function send_days(): array
{
    // clés = date('w') : 0 = dimanche, 1 = lundi
    return [0 => 'sunday', 1 => 'monday'];
}

function logline(string $msg, bool $quiet = false): void
{
    $line = '[' . (new DateTimeImmutable('now', new DateTimeZone(TZ)))->format('Y-m-d H:i:s T') . '] ' . $msg;
    if (!$quiet) {
        echo $line, PHP_EOL;
    }
    $dir = __DIR__ . '/logs';
    if (!is_dir($dir)) {
        @mkdir($dir, 0750, true);
    }
    @file_put_contents($dir . '/brevo-promo.log', $line . PHP_EOL, FILE_APPEND | LOCK_EX);
}

function fail(string $msg): never
{
    logline('ERREUR : ' . $msg);
    exit(1);
}

/**
 * Décide si l'envoi doit avoir lieu maintenant.
 * Fonction pure : testable avec n'importe quel horodatage.
 *
 * @return array{0: bool, 1: string} [autorisé, jour ou raison du refus]
 */
function should_send(DateTimeImmutable $now): array
{
    $paris = $now->setTimezone(new DateTimeZone(TZ));
    $dow   = (int) $paris->format('w');
    $hour  = (int) $paris->format('G');
    $days  = send_days();

    if (!array_key_exists($dow, $days)) {
        return [false, 'jour non planifié (' . $paris->format('l') . ')'];
    }
    if ($hour !== SEND_HOUR) {
        return [false, sprintf('il est %dh à Paris, envoi prévu à %dh', $hour, SEND_HOUR)];
    }
    return [true, $days[$dow]];
}

/** Appel HTTP à l'API Brevo. */
function brevo(string $method, string $path, ?array $body, string $apiKey): array
{
    $ch = curl_init(API_BASE . $path);
    if ($ch === false) {
        fail('curl indisponible sur ce serveur');
    }
    $headers = ['api-key: ' . $apiKey, 'accept: application/json'];
    if ($body !== null) {
        $headers[] = 'content-type: application/json';
    }
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CUSTOMREQUEST  => $method,
        CURLOPT_HTTPHEADER     => $headers,
        CURLOPT_TIMEOUT        => 90,
    ]);
    if ($body !== null) {
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    }
    $raw  = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $err  = curl_error($ch);
    curl_close($ch);

    if ($raw === false) {
        fail('réseau : ' . $err);
    }
    $decoded = ($raw === '') ? [] : (json_decode((string) $raw, true) ?? ['raw' => $raw]);
    return ['code' => $code, 'body' => $decoded];
}

/** Message d'erreur API lisible, avec aide dédiée au filtrage d'IP. */
function api_error(array $res): string
{
    $b   = $res['body'];
    $msg = $b['message'] ?? json_encode($b, JSON_UNESCAPED_UNICODE);
    $out = sprintf('HTTP %d — %s', $res['code'], (string) $msg);
    if ($res['code'] === 401 && str_contains((string) $msg, 'IP address')) {
        $out .= PHP_EOL . '  → Autorise cette IP dans Brevo : https://app.brevo.com/security/authorised_ips';
    }
    if ($res['code'] === 402) {
        $out .= PHP_EOL . '  → Crédits d\'envoi insuffisants sur le compte Brevo.';
    }
    return $out;
}

// -------------------------------------------------------------- configuration

$argvOpts = array_slice($argv, 1);
$opt      = static fn(string $name): bool => in_array('--' . $name, $GLOBALS['argvOpts'], true);

if ($opt('help')) {
    echo <<<TXT
    Promo Phidias — envoi récurrent via Brevo

      --check     Vérifie la clé API et la liste blanche d'IP
      --lists     Affiche les IDs de listes Brevo (pour remplir config.php)
      --test      Envoie à la liste de test (test_list_id)
      --dry-run   Fait tout sauf l'envoi réel
      --force     Ignore la garde horaire (test hors dimanche/lundi)
      --selftest  Vérifie la garde horaire (été/hiver) sans rien envoyer
      --help      Ce message

    Cron recommandé :
      0 * * * 0,1  /usr/bin/php {$argv[0]}

    TXT;
    exit(0);
}

if ($opt('selftest')) {
    // Vérifie la garde horaire en heure d'hiver (CET, UTC+1) et d'été (CEST, UTC+2).
    $cases = [
        ['2026-01-11 09:00:00', true,  "dimanche 10h Paris (hiver)"],
        ['2026-01-12 09:00:00', true,  "lundi 10h Paris (hiver)"],
        ['2026-08-30 08:00:00', true,  "dimanche 10h Paris (ete)"],
        ['2026-08-31 08:00:00', true,  "lundi 10h Paris (ete)"],
        ['2026-01-11 08:00:00', false, "dimanche 9h Paris (hiver)"],
        ['2026-01-11 10:00:00', false, "dimanche 11h Paris (hiver)"],
        ['2026-08-30 07:00:00', false, "dimanche 9h Paris (ete)"],
        ['2026-08-30 09:00:00', false, "dimanche 11h Paris (ete)"],
        ['2026-01-13 09:00:00', false, "mardi 10h Paris"],
        ['2026-08-29 08:00:00', false, "samedi 10h Paris (ete)"],
    ];
    $fails = 0;
    foreach ($cases as [$utc, $expected, $label]) {
        [$got, $info] = should_send(new DateTimeImmutable($utc, new DateTimeZone('UTC')));
        $ok = ($got === $expected);
        $fails += $ok ? 0 : 1;
        printf("%-6s %-34s -> %s%s", $ok ? 'OK' : 'ECHEC', $label, $got ? 'envoi' : "pas d'envoi", PHP_EOL);
    }
    $total = count($cases);
    echo PHP_EOL, $fails === 0
        ? "{$total}/{$total} : garde horaire correcte, ete comme hiver." . PHP_EOL
        : "{$fails} echec(s) sur {$total}." . PHP_EOL;
    exit($fails === 0 ? 0 : 1);
}

$configPath = __DIR__ . '/config.php';
if (!is_file($configPath)) {
    fail("config.php introuvable. Copie config.example.php en config.php et renseigne-le.");
}
$cfg = require $configPath;

foreach (['api_key', 'sender_name', 'sender_email', 'list_ids', 'html_file'] as $k) {
    if (empty($cfg[$k])) {
        fail("config.php : la clé « {$k} » est absente ou vide.");
    }
}
$apiKey = (string) $cfg['api_key'];

// ---------------------------------------------------------------- modes utils

if ($opt('check')) {
    $res = brevo('GET', '/account', null, $apiKey);
    if ($res['code'] !== 200) {
        fail(api_error($res));
    }
    logline('OK — clé valide et IP autorisée. Compte : ' . ($res['body']['companyName'] ?? '?'));
    exit(0);
}

if ($opt('lists')) {
    $res = brevo('GET', '/contacts/lists?limit=50', null, $apiKey);
    if ($res['code'] !== 200) {
        fail(api_error($res));
    }
    echo 'ID    CONTACTS  NOM', PHP_EOL;
    foreach ($res['body']['lists'] ?? [] as $l) {
        printf("%-5d %-9d %s%s", $l['id'], $l['totalSubscribers'] ?? 0, $l['name'], PHP_EOL);
    }
    exit(0);
}

// ------------------------------------------------------------- garde horaire

$now    = new DateTimeImmutable('now');
$forced = $opt('force');

if ($forced) {
    $day = send_days()[(int) $now->setTimezone(new DateTimeZone(TZ))->format('w')] ?? 'monday';
    logline('--force : garde horaire ignorée.');
} else {
    [$ok, $info] = should_send($now);
    if (!$ok) {
        // Sortie silencieuse : le cron tourne toutes les heures, inutile de
        // journaliser 46 non-événements par semaine.
        exit(0);
    }
    $day = $info;
}

// ---------------------------------------------------------------- idempotence

$stateDir = __DIR__ . '/state';
if (!is_dir($stateDir)) {
    @mkdir($stateDir, 0750, true);
}
$today = $now->setTimezone(new DateTimeZone(TZ))->format('Y-m-d');
$lock  = $stateDir . '/.sent-' . $today;

$isDryRun = $opt('dry-run');
$isTest   = $opt('test');

if (!$isDryRun && !$isTest && is_file($lock)) {
    logline("Déjà envoyé aujourd'hui ({$today}) — rien à faire.");
    exit(0);
}

// ------------------------------------------------------------------- contenu

$htmlFile = $cfg['html_file'];
if (!is_file($htmlFile)) {
    fail("Fichier HTML introuvable : {$htmlFile}");
}
$html = file_get_contents($htmlFile);
if ($html === false || trim($html) === '') {
    fail("Fichier HTML vide ou illisible : {$htmlFile}");
}
if (!str_contains($html, '{{ unsubscribe }}')) {
    logline('AVERTISSEMENT : la balise {{ unsubscribe }} est absente du HTML. Brevo ajoutera son propre lien.');
}

$subject = $day === 'sunday'
    ? ($cfg['subject_sunday'] ?? 'Code LUCAS : jusqu\'à -80% sur Phidias')
    : ($cfg['subject_monday'] ?? 'Phidias : le code LUCAS est toujours actif');

$campaignName = sprintf('Promo Phidias — %s (%s)', $today, $day);

logline(sprintf(
    '%sPréparation : jour=%s | objet=« %s » | listes=%s',
    $isDryRun ? '[DRY-RUN] ' : '',
    $day,
    $subject,
    implode(',', (array) $cfg['list_ids'])
));

// ------------------------------------------------------------------ création

$payload = [
    'name'       => $campaignName,
    'subject'    => $subject,
    'sender'     => ['name' => $cfg['sender_name'], 'email' => $cfg['sender_email']],
    'type'       => 'classic',
    'htmlContent'=> $html,
    'recipients' => ['listIds' => array_map('intval', (array) $cfg['list_ids'])],
];
if (!empty($cfg['reply_to'])) {
    $payload['replyTo'] = $cfg['reply_to'];
}

if ($isDryRun) {
    logline('[DRY-RUN] Campagne non créée. Taille du HTML : ' . strlen($html) . ' octets.');
    exit(0);
}

$res = brevo('POST', '/emailCampaigns', $payload, $apiKey);
if ($res['code'] !== 201 || empty($res['body']['id'])) {
    fail('création de la campagne — ' . api_error($res));
}
$campaignId = (int) $res['body']['id'];
logline("Campagne créée (id {$campaignId}).");

// -------------------------------------------------------------------- envoi

if ($isTest) {
    if (empty($cfg['test_emails'])) {
        fail('--test : renseigne « test_emails » dans config.php.');
    }
    $res = brevo('POST', "/emailCampaigns/{$campaignId}/sendTest", ['emailTo' => (array) $cfg['test_emails']], $apiKey);
    if ($res['code'] !== 204) {
        fail('envoi de test — ' . api_error($res));
    }
    logline('Email de test envoyé à : ' . implode(', ', (array) $cfg['test_emails']));
    exit(0);
}

$res = brevo('POST', "/emailCampaigns/{$campaignId}/sendNow", null, $apiKey);
if ($res['code'] !== 204) {
    fail('envoi — ' . api_error($res));
}

@file_put_contents($lock, $campaignName . PHP_EOL);
logline("Envoyé. Campagne {$campaignId} « {$campaignName} ».");
exit(0);

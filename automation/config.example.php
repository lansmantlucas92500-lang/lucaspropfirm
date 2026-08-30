<?php
/**
 * Configuration de l'envoi récurrent Brevo.
 *
 * Copier ce fichier en « config.php » puis le renseigner.
 * config.php contient la clé API : il est exclu de git (.gitignore).
 */

return [
    // Clé API Brevo (SMTP & API → Clés API).
    'api_key' => 'xkeysib-VOTRE_NOUVELLE_CLE',

    // Expéditeur — l'adresse doit être validée dans Brevo.
    'sender_name'  => 'Lucas Prop Firm',
    'sender_email' => 'lucas@lucaspropfirm.fr',
    'reply_to'     => 'lucas@lucaspropfirm.fr',

    // IDs des listes destinataires. Les découvrir avec :  php brevo-promo.php --lists
    'list_ids' => [/* 2, 3 */],

    // Adresses de test pour  php brevo-promo.php --test
    'test_emails' => ['lucas@lucaspropfirm.fr'],

    // Chemin absolu du HTML à envoyer.
    'html_file' => __DIR__ . '/../email-prospects-21-08-2026-brevo.html',

    // Objets distincts selon le jour : un même objet répété deux fois par
    // semaine augmente nettement le taux de plaintes spam.
    'subject_sunday' => 'Phidias : jusqu\'à -80% avec le code LUCAS',
    'subject_monday' => 'Financer son trading cette semaine — code LUCAS',
];

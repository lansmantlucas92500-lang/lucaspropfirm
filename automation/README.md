# Envoi automatique de la promo Phidias — dimanche & lundi 10h

Script autonome qui crée une campagne Brevo à partir du HTML local et l'envoie,
**chaque dimanche et lundi à 10h (heure de Paris)**.

Les emails partent bien de **ton compte Brevo** — ta liste, ta réputation
d'expéditeur, ta gestion des désabonnements. Seul le *déclencheur* est externe,
parce que les workflows d'automatisation Brevo ne sont pas créables par API.

- PHP natif, **aucune dépendance** à installer
- Insensible au changement d'heure : 10h reste 10h été comme hiver
- Impossible d'envoyer deux fois le même jour (verrou)
- Objets d'email différents dimanche / lundi

---

## Installation (une seule fois)

### 1. Régénérer une clé API

L'ancienne clé a été exposée : **Brevo → SMTP & API → Clés API** → supprimer,
puis en créer une nouvelle.

### 2. Déposer les fichiers sur Hostinger

Via le gestionnaire de fichiers ou FTP, **en dehors de `public_html`** (pour que
le script ne soit jamais accessible depuis le web) :

```
/home/TON_USER/automation/brevo-promo.php
/home/TON_USER/automation/config.php
/home/TON_USER/email-prospects-21-08-2026-brevo.html
```

### 3. Créer `config.php`

Copier `config.example.php` en `config.php` et renseigner la clé API,
l'expéditeur et le chemin du HTML.

### 4. Autoriser l'IP du serveur dans Brevo

C'est l'étape qui débloque l'API. Depuis un terminal SSH Hostinger :

```bash
php /home/TON_USER/automation/brevo-promo.php --check
```

- Si la clé et l'IP sont bonnes : `OK — clé valide et IP autorisée`
- Sinon Brevo renvoie l'IP à autoriser ; l'ajouter sur
  https://app.brevo.com/security/authorised_ips puis relancer `--check`

> L'IP d'un hébergement Hostinger est fixe : cette autorisation est à faire
> une seule fois, contrairement à un runner cloud dont l'IP change.

### 5. Renseigner les IDs de liste

```bash
php /home/TON_USER/automation/brevo-promo.php --lists
```

Reporter le ou les IDs voulus dans `list_ids` de `config.php`.

### 6. Programmer le cron

**hPanel → Avancé → Tâches cron**, expression :

```
0 * * * 0,1
```

commande :

```
/usr/bin/php /home/TON_USER/automation/brevo-promo.php
```

> Le cron tourne **toutes les heures** les dimanche et lundi ; le script sort en
> quelques millisecondes sauf s'il est 10h à Paris. C'est ce qui le rend
> insensible au fuseau du serveur et au changement d'heure : aucun réglage à
> corriger deux fois par an.

---

## Vérifier avant de brancher toute la liste

```bash
php brevo-promo.php --selftest              # garde horaire (été + hiver)
php brevo-promo.php --check                 # clé API + autorisation d'IP
php brevo-promo.php --force --dry-run       # tout sauf l'envoi
php brevo-promo.php --test                  # envoi réel aux adresses de test
```

Le `--test` est le seul moyen de valider le **lien de désinscription** :
`{{ unsubscribe }}` n'est jamais résolu dans un aperçu, uniquement à l'envoi réel.

## Options

| Option | Effet |
|---|---|
| `--check` | Vérifie la clé API et l'autorisation d'IP |
| `--lists` | Affiche les IDs de listes Brevo |
| `--test` | Envoie aux adresses de `test_emails` |
| `--dry-run` | Fait tout sauf l'envoi |
| `--force` | Ignore la garde horaire (test hors créneau) |
| `--selftest` | Teste la garde horaire, sans rien envoyer |
| `--help` | Aide |

## Suivi

Journal : `automation/logs/brevo-promo.log`
Verrous d'envoi : `automation/state/.sent-AAAA-MM-JJ`

En cas d'échec, le script sort avec un code non nul et journalise la réponse de
Brevo (crédits insuffisants, IP non autorisée, expéditeur non validé…).

## Changer le contenu de l'email

Éditer `email-prospects-21-08-2026-brevo.html` et le redéposer sur le serveur.
Aucune modification du script n'est nécessaire.

---

## Deux points d'attention

**Délivrabilité.** Deux envois hebdomadaires sur une liste prospects génèrent
mécaniquement des plaintes spam, qui dégradent durablement la réputation du
domaine expéditeur. Les objets distincts dimanche/lundi (déjà configurés)
atténuent le phénomène ; faire varier aussi l'accroche du corps ferait beaucoup
mieux encore.

**Cohérence du consentement.** La page Récap Macro annonce « un PDF par semaine »
au moment de l'inscription. Si la cadence passe durablement à deux envois, cette
mention mérite d'être alignée.

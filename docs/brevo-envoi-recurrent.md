# Envoi récurrent dimanche + lundi à 10h — configuration Brevo

> Objectif : envoyer `email-prospects-21-08-2026-brevo.html` automatiquement
> chaque **dimanche** et chaque **lundi à 10h00 (Paris)**.

## Pourquoi cette configuration se fait à la main

Brevo sait faire des envois récurrents nativement, **mais uniquement via l'interface** :
l'API Brevo v3 n'expose aucun endpoint de création de workflow d'automatisation.
Elle permet de *déclencher* un workflow existant (Events API), jamais d'en créer un.
Aucun script — quel qu'il soit — ne peut donc monter cette automatisation à ta place.
Les 6 étapes ci-dessous prennent ~10 minutes, une seule fois.

---

## Étape 1 — Créer le template email

1. **Campagnes → Templates → Créer un template**
2. Type d'éditeur : **Code HTML** (surtout pas le drag & drop, il réécrirait le HTML)
3. Coller le contenu de `email-prospects-21-08-2026-brevo.html`
4. Renseigner l'objet de l'email et l'expéditeur, puis **Enregistrer**

> C'est bien un **template** qu'il faut créer, pas une campagne : une campagne est un
> envoi unique, alors qu'une automatisation référence un template.

## Étape 2 — Créer le segment des destinataires

1. **Contacts → Segments → Créer un segment**
2. Condition : les contacts de ta liste prospects
3. Enregistrer sous un nom clair, ex. `Prospects — envoi récurrent`

> Inutile d'exclure les désabonnés : Brevo ne les recontacte jamais automatiquement.

## Étape 3 — Créer l'automatisation du dimanche

1. **Automatisations → Créer une automatisation → Personnalisée**
2. Point d'entrée : **« Le contact correspond à des filtres »**
   *(selon la version de l'interface : « Un contact est dans un segment à un moment donné »)*
3. Sélectionner le segment de l'étape 2
4. Régler la vérification récurrente :
   - Fréquence : **hebdomadaire**
   - Jour : **dimanche**
   - Heure : **10:00**

## Étape 4 — Ajouter l'envoi

1. Ajouter une étape **« Envoyer un email »**
2. Choisir le template créé à l'étape 1

## Étape 5 — ⚠️ Autoriser la ré-entrée des contacts

Dans les **paramètres du workflow**, activer :

> **« Autoriser vos contacts à entrer plusieurs fois dans l'automatisation »**

**C'est l'étape la plus importante du montage.** Par défaut, un contact n'entre
qu'**une seule fois** dans un workflow. Sans cette option, chaque personne reçoit
l'email une fois — puis plus jamais — et la récurrence semblera cassée alors que
tout le reste est correct.

## Étape 6 — Dupliquer pour le lundi

Dupliquer l'automatisation et changer le jour en **lundi**.

> Deux workflows séparés plutôt qu'un seul avec deux jours cochés : ça fonctionne
> quelle que soit la version de l'interface, et tu obtiens des statistiques
> distinctes pour chaque jour d'envoi.

Activer ensuite les **deux** automatisations.

---

## Trois vérifications avant de conclure à un bug

| À vérifier | Où | Pourquoi |
|---|---|---|
| **Fuseau horaire du compte** | Paramètres du compte | S'il n'est pas sur Europe/Paris, « 10h » sera l'heure d'un autre fuseau |
| **Frequency cap / Email overload prevention** | Paramètres d'envoi | Si ce garde-fou est actif, il peut **supprimer silencieusement** le second envoi de la semaine |
| **Ré-entrée activée** | Paramètres du workflow | Voir étape 5 — la cause n°1 d'un « ça n'envoie qu'une fois » |

## Test à blanc recommandé

Avant de brancher toute la liste :

1. Créer un segment temporaire ne contenant **que ton adresse**
2. Pointer l'automatisation dessus, avec une récurrence sur le prochain jour qui arrive
3. Vérifier la réception à 10h, le rendu, et **le lien de désinscription**

> Le lien de désinscription (`{{ unsubscribe }}`) n'est résolu qu'à l'envoi réel :
> il ne fonctionne jamais dans l'aperçu Brevo. Seul un envoi réel le valide.

---

## Deux points d'attention

**Délivrabilité.** Le même contenu envoyé deux fois par semaine à une liste
prospects génère mécaniquement des plaintes spam, qui dégradent durablement la
réputation du domaine expéditeur. Faire varier au moins l'objet et l'accroche
entre le dimanche et le lundi réduirait nettement ce risque.

**Cohérence avec le consentement.** La page Récap Macro promet *« un PDF par
semaine »* au moment de l'inscription. Deux envois hebdomadaires s'écartent de la
finalité annoncée lors de la collecte — à ajuster sur la page d'inscription si la
cadence change durablement.

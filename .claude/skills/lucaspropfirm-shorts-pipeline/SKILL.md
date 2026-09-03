---
name: lucaspropfirm-shorts-pipeline
description: |-
  Orchestration d'un short trading LucasPropfirm — de l'idée au livrable publié. Lecture du journal de production, choix du concept par RECHERCHE EN LIGNE (protocole en 3 requêtes, aucun catalogue, jamais deux shorts identiques), gates (hook, coût, viralité), programmation Metricool (toute demande de programmation vise TOUS les réseaux connectés au brand LucasPropfirm), journal, mesure. Charger pour planifier/piloter une production ou pour programmer des posts. Le contenu (anti-IP, prompt, script, description) → skill lucaspropfirm-short-description. La procédure d'exécution (génération, montage voix, sous-titres) → skill lucaspropfirm-shorts-generation.
---

# LucasPropfirm — orchestration des shorts 15 s

> Périmètre : **la carte du pipeline**, le **choix du concept** et le **journal**. Il ne redonne pas les règles créatives (voir `lucaspropfirm-short-description`) ni la procédure d'exécution (voir `lucaspropfirm-shorts-generation`).

## Contexte fixe
- Comptes : TikTok/IG @lucaspropfirm01, YouTube @lucasPropfirm2026.
- Univers : « marché financier vivant », faceless premium, bleu nuit + lime/or (détaillé dans `short-description`).
- Journal de production : `shorts/production-log.md` (à la racine du repo). Assets de marque : `shorts/assets/`.
- Baselines : recalculer à chaque nouvel audit — ne jamais réutiliser d'anciennes stats comme actuelles.

## Étapes (idée → livrable publié)
| # | Étape | Où | Gate |
|---|---|---|---|
| 0 | **Lire le journal** `shorts/production-log.md` : derniers concepts, dernier patron de hook, échecs IP récents | ici | — |
| 1 | **Choix du concept** par recherche en ligne (protocole ci-dessous) | ici | concept ≠ des 10 derniers ; patron hook ≠ du précédent |
| 2 | **Contenu** — hook, script (34-38 mots, CTA oral), prompt 8 blocs, description | `short-description` | checklist hook ✔ ; **test d'ancrage trading ✔** (≥ 2 marqueurs concrets hors CTA) ; zéro mot de la liste interdite |
| 3 | **Validation utilisateur** — concept + hook + script + prompt + description, puis **coût** (`get_cost`) | ici | OK explicite ×2 |
| 4 | **Exécution** — narration → gate débit → vidéo muette → gate viralité → montage → sous-titres → vérifs | `shorts-generation` | `speech` ≤ 14,3 s ; `completed` ; frames propres |
| 5 | **Publication / programmation** — Metricool : **UN post par short, sur TOUS les réseaux du brand** (§ Programmation Metricool) ; TikTok direct via `tiktok_prepare_publish`/`tiktok_publish` seulement si Lucas le demande | `shorts-generation` §11 + § ci-dessous | description complète (CTA haut 5 lignes + CTA écrit + 11 liens) ; tous les réseaux du brand couverts |
| 6 | **Journal + mesure** — écrire la ligne du journal ; noter la variable testée | ici | ligne écrite |

## Choix du concept — protocole de recherche (aucun catalogue, aucune rotation)
**Aucun template d'idées.** Chaque concept sort d'une recherche faite **au moment de la production** :
1. **3 requêtes minimum** (WebSearch) :
   - « *[sujet]* trading débutant » (ce que le public FR demande) ;
   - « *[sujet]* short / tiktok / reels » (formats et hooks qui tournent) ;
   - 2-3 comptes FR de la niche (prop firms, futures) — ce qu'ils ont posté récemment sur le sujet.
2. **Extraire 3 hooks performants** observés + l'angle qui les différencie (peur, surprise, erreur, chiffre).
3. **Choisir UN angle** pour UNE idée ; le reformuler dans le patron de hook imposé par l'alternance.
4. **Noter la source** (URL/compte) dans le journal. Jamais copier un hook mot pour mot.
5. Le visuel reste une métaphore abstraite (anti-IP dans `short-description`) : le terme technique est porté par la narration, jamais par l'image.

**Règle de variété** : jamais 2 posts consécutifs de la même famille de plan ni du même patron de hook ; jamais 2 vidéos identiques (le journal fait foi).

## Contrat de script (rappel — détail dans short-description)
UNE idée par vidéo ; 34-38 mots CTA oral inclus ; durée verrouillée sur la parole mesurée (jamais accélérer la voix — réécrire) ; hook à 0-1,2 s compréhensible sans le son ; CTA oral fixe en fin, CTA écrit complet sur l'encart et la description. Zéro promesse de gains ; « jusqu'à -80 % » jamais garanti ; pas de nom de firme dans les vidéos éducatives.

## Mode semaine (« programme ma semaine », « lance la semaine »)
Un lot de **N shorts (défaut 7)** produit en **une session**, publié **étalé**.
1. **Planification groupée (0 crédit)** : journal → recherche (protocole ci-dessus, une recherche par concept) → N fiches complètes : concept, hook avec **alternance pré-calculée sur le lot** (Q · CH · ER · CI · Q · CH · ER), **signature visuelle différente** pour chaque short, script, prompt (recette FR), description, 1 variable testée par post.
2. **Coût total** préflighté (`get_cost` × N) → **UNE validation** pour tout le lot = mandat de production.
3. **Exécution séquentielle** : short 1 de A à G, ligne de journal, livraison immédiate (fichier + description), puis short 2. Jamais deux vidéos en parallèle.
4. **Échec en cours de lot** : 1 relance sur prompt corrigé ; 2ᵉ échec → `échec-IP` au journal, on passe au suivant sans casser la séquence ; un **concept de remplacement** est proposé en **fin de lot**.
5. **Calendrier de publication** livré avec le lot : `jour · heure · plateforme · slug · patron hook` — l'alternance des hooks est respectée dans l'ordre de **publication**, pas seulement de production.
6. **Programmation** : via Metricool, **un post par short couvrant TOUS les réseaux du brand** (§ Programmation Metricool). TikTok en direct (`UPLOAD_TO_DRAFT`) uniquement si Lucas demande explicitement de court-circuiter Metricool.

## Programmation Metricool — brand LucasPropfirm (`blogId` 6758811)

**Règle par défaut, sans avoir à la redemander : « programme », « planifie », « programme ma semaine »
= publication sur TOUS les réseaux sociaux connectés au Metricool de LucasPropfirm.**
Jamais un sous-ensemble, jamais « TikTok + Instagram seulement », sauf si Lucas nomme lui-même
les réseaux qu'il veut — et dans ce cas seulement pour ce lot-là, ça ne change pas la règle.

1. **Découvrir les réseaux, ne jamais les supposer.** Appeler `getBrandSettings` sur le brand
   LucasPropfirm au début de chaque programmation et lister les réseaux réellement connectés.
   Le compte peut en gagner ou en perdre entre deux lots : la liste vivante fait foi, pas cette page.
   Réseaux connectés au moment de la rédaction : **X (twitter) · Facebook · Instagram · LinkedIn ·
   TikTok · YouTube**.
2. **UN post par short, pas un post par réseau.** Tous les réseaux vont dans le tableau `providers`
   du même `createScheduledPost`. Un post par réseau crée des doublons impossibles à supprimer
   par l'API (voir point 6).
3. **Texte identique partout.** X est en abonnement Premium : la limite de 280 caractères ne
   s'applique pas, la description longue complète part telle quelle sur les 6 réseaux.
4. **`networkData` obligatoire pour chaque réseau du post**, avec les déclarations IA :
   `tiktokData.isAigc: true` · `instagramData.isAiGenerated: true` (type `REEL`) ·
   `youtubeData.isAiGeneratedContent: true` (type `short`, `category: EDUCATION`,
   `madeForKids: false`) · `facebookData.type: REEL` · `linkedinData.type: post` ·
   `twitterData.tags: []`. Sur un short **promotionnel Phidiaspropfirm.com**, ajouter
   `tiktokData.commercialContentOwnBrand: true`.
5. **Fuseau** : `Europe/Paris`, format `{dateTime, timezone}`. Les dates passées à
   `getScheduledPosts` exigent un offset explicite (`2026-09-02T00:00:00+02:00`).
6. **Les `id` numériques changent à CHAQUE mise à jour** d'un post Metricool ; **seuls les `uuid`
   sont stables**. Consigner les uuid au journal, relire le planner avant toute modification.
   L'API n'expose **aucune suppression** : un post en trop se met en `draft: true` et se supprime
   à la main dans le planner — d'où la règle 2.
7. **Vérification finale obligatoire** : `getScheduledPosts` sur la fenêtre programmée, et
   contrôler que chaque post porte bien la liste complète des réseaux en `PENDING`.

## Journal — `shorts/production-log.md`
Une ligne par short, écrite à l'étape 6 (et une ligne « échec » si un concept est abandonné) : date · slug · concept · patron hook (Q/CH/ER/CI) · famille de plan · source recherche · job_id voix · job_id vidéo · coût · statut · URL publiée · variable testée. **Sans journal, les règles d'alternance sont inapplicables.**

## Mesure
- Tester **UNE seule variable par post** (patron de hook, famille de plan, heure, longueur du hook) ; seuils relatifs à la médiane du compte.
- Ne jamais comparer TikTok/IG/YT entre elles, ni prendre les vues pour organiques sans ratio like/vue.
- `virality_predictor` (étape 4) donne une lecture *avant* publication ; les stats réelles *après* — noter les deux dans le journal pour calibrer.

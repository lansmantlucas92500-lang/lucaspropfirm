---
name: lucaspropfirm-shorts-pipeline
description: |-
  Pipeline de production des shorts trading LucasPropfirm — de l'idée au short final. Rotation = catalogue vivant (18 concepts « C'est quoi… ? » + banque injectée, jamais deux shorts identiques), vidéo Seedance 2.0 Mini 15 s 720p, narr. la voix Julian en post-prod, anti-IP, alternance. À charger pour toute production/planification d'un short lucaspropfirm.
---

# LucasPropfirm — pipeline shorts 15 s

## Contexte fixe (recalculer à chaque audit)
- Comptes : TikTok/IG @lucaspropfirm01, YouTube @lucasPropfirm2026.
- Univers visuel : « marché financier vivant », faceless premium, bleu nuit + lime/or, rouge/vert = signaux. Logo LP en post-prod uniquement.
- Baselines : recalcular à chaque nouvel audit — ne jamais réutiliser les anciennes statistiques comme actuelles.

## Contrat de script
1. UNE idée par vidéo ; 38-42 mots ; ≈15 s (2,7-2,8 mots/s) ; durée verrouillée au TTS réel (Julian FR) — jamais change_voice.
2. Hook verbal + visuel à 0-1,2 s, compréhensible sans le son.
3. Structure : 0-1,2 s hook / 1,2-4 problème / 4-9 explication / 9-13 règle / 13-15 CTA.
4. Conformité : zéro promesse de gains ; « jusqu'à -80 % » jamais garanti ; pas de nom de firme dans les vidéos éducatives.
5. CTA unique fixe en fin de narration : « Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com. »
6. Interdits : Limova sur compte trading, contenu EN, 16:9, chandeliers génériques sans contexte, fausses interfaces broker, lifestyle richesse.

## Choix du concept — par recherche & analyse (pas de rotation figée)
- **Aucun template d'idées.** Le choix du concept/l'angle de chaque vidéo vient d'une **recherche web + analyse détaillée de ce qui fonctionne** pour le sujet et la niche (formats viraux, hooks qui marchent, angles d'analyse technique, besoins du public FR).
- Pour chaque idée : rechercher et étudier avant de proposer — ce qui retient, ce qui convertit, ce qui différencie.
- Le refus : jamais 2 vidéos identiques — le concept est choisi pour sa pertinence et son impact, pas par rotation programmée.
- **Anti-catalogue** (dans `references/visual-catalog.md`) : zéro chiffre/montant à l'écran, pas d'interface broker réaliste, bougies en verre abstraites = identité visuelle autorisée ; jamais de visuel réaliste chiffré.
- **Règle de variété** : jamais 2 posts consécutifs de la même famille de plan ; un concept = un angle éditorial adapté à l'idée analysée.

## Publication
Lire `references/publication-spec.md` : rotation quotidienne, signature de fin (logo LP + encart), format descriptions IG/TikTok avec le bloc de liens 9 lignes (Phidias LUCAS, Discord, PropLog, newsletters, Affiliation, Limova PROFILM30, Wisewand LUCAS10 FR/EN).

## Génération — règles non négociables
- Modèle : `seedance_2_0_mini`, 720p, 9:16, 15 s, **`generate_audio=false` OBLIGATOIRE** (booléen littéral ; défaut backend = true → omettre → rejet IP).
- Soumission pure : `prompt` + `model` + `aspect_ratio` + `resolution` + `duration` + `params.generate_audio=false` — **aucune image / audio / référence** dans medias.
- Anti-IP total dans les prompts visuels : interdits argent/gains/versements/payout/pièces ; marques (Phidias, LucasPropfirm…), instruments réels (Futures ES/NQ…), texte/chiffre/logo/UI simulée. Vocabulaire abstract (bougies de verre, verre fumé, chrome, flux, colonnes…).
- **Narration** : TTS Julian (voice_id connu) en post-prod ffmpeg, vérifiée (jamais sans voix) ; video muette.
- Prompts 8 blocs : SCENE CONTEXT→FIRST FRAME→OPTICS→CAMERA→LIGHTING→PHYSICS→ACTION TIMING→AUDIO ; pas de texte généré (sous-parties en post-prod).
- Validation : double validation utilisateur (idée + coût affiché) avant tout crédit ; 1 video à la fois, pas de batch ; en cas de 429 : pause 90 s.

## Mesure
- Tester UNE variable par post (matrice T01-T10) ; seuils relatifs à la médiane du compte. Ne jamais comparer TikTok/IG/YT entre elles ni prendre les vues pour organiques sans ratio like/vue.
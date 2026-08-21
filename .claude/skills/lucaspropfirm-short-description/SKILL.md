---
name: lucaspropfirm-short-description
description: |
  Spec complet de production des shorts lucaspropfirm (trading Futures ES/NQ, prop firms, audience FR). Utilise pour TOUTE création de short lucaspropfirm : vidéo (Seedance 2.0 Mini, univers visuel, prompt, narration Julian), description IG (format aligné émojis + bloc de liens), et règle de validation (proposer avant générer). Contient le contexte compte, le format technique, l'univers visuel (rotation 18 concepts v4.2 — voir lucaspropfirm-shorts-pipeline), la structure de prompt, la structure de narration 15 s, et la validation obligatoire.
---

# Spec de production des shorts lucaspropfirm

## CONTEXTE COMPTE
@lucaspropfirm01 — trading **Futures ES/NQ**, prop firms, audience FR débutante/intermédiaire. Objectif : vues + commentaires → Discord gratuit → conversion Phidias (code **LUCAS**) et Discord Pro/Élite.

## FORMAT TECHNIQUE (non négociable)
- Modèle : **Seedance 2.0 Mini**, 720p, **9:16**, **15 secondes maximum**
- **Aucun texte lisible** à l'écran dans la vidéo générée
- Narration TTS voix **"Julian"** en français (jamais change_voice — Mini prononce mal le FR)

### LOI DE GÉNÉRATION ANTI-ÉCHECS (non négociable)
- **JAMAIS de batch.** Lancer **1 (une seule) vidéo à la fois** via `higgsfield_generate_video` avec `requests: [ {un seul} ]`.
- **Pourquoi :** le compte est plafonné à **8 jobs simultanés** ; lancer plusieurs vidéos d'un coup (même 6-7) dépasse la limite → échecs `429 rate_limit` en cascade.
- **Rythme obligatoire** : générer → attendre le résultat (`higgsfield_job_status`) → AVANT de lancer la suivante.
- **En cas d'échec d'un job** : attendre **40-60 s** (sleep), puis **retenter UNE fois la même vidéo**. Ne jamais relancer en boucle sans pause.
- Ne déclarer un short terminé que si son job vidéo est `completed`.
- **Même règle pour l'audio** : la narration TTS est générée 1 voix à la fois (jamais de batch audio).

### PIPELINE VOIX — MÉTHODE VALIDÉE (montage post-prod, jamais de référence audio dans la vidéo)
**La voix Julian n'est JAMAIS intégrée à la génération vidéo** (l'ancienne méthode « narration en référence audio » causait des rejets IP et est ABANDONNÉE). La vidéo est générée **muette** (`generate_audio=false`) puis la narration est montée en post-prod.
1. Générer la narration **TTS Julian** (`voiceover`, voice_id Julian, script 38-42 mots, CTA exact) — 1 à la fois.
2. Générer la vidéo **Seedance 2.0 Mini avec `params.generate_audio=false`** (720p, 9:16, 15 s) — **aucune référence audio, aucune image** dans `medias`/`params` (text-to-video pur).
3. **Monter la narration sur la vidéo** (ffmpeg, mapper uniquement la piste audio de la TTS).
4. **Vérifier la voix** (audio_analyze) : narration audible + non coupée.
5. **Seule MAINTENANT la vidéo est un livrable.**
**Séquence : narration(i) → vidéo muette(i) → montage voix(i) → vérif(i) → livraison(i) → narration(i+1).** Jamais de vidéo sans voix livrée.

## UNIVERS VISUEL — "marché financier vivant" · FUTURISTE PREMIUM
Style : animation 3D stylisée **futuriste de haute qualité** (rendu cinématique, type film de science-fiction financier), bleu nuit profond + accents or/lime, **SANS visage humain**, ambiance premium fintech. **Matériaux riches** (verre fumé, métal brossé, chrome, surfaces réfléchissantes, lumières HDR), **éclairage cinématique** (rim light bleu froid + halos or/lime + bokeh, jamais plat), **détails fintech** (micro-textures, particules lumineuses, hologrammes abstraits, HUD flottants sans texte lisible), **échelle et profondeur** (volumes monumentaux ou intimes avec profondeur de champ et couches FG/MG/BG), **mouvement fluide** (dolly lent, transitions organiques). Cohérent avec la charte branding (covers/bannières bleu nuit + lime-jaune, logo LP rond).

## CHOIX DU CONCEPT — par recherche & analyse (pas de rotation)
**Aucun template d'idées.** Le concept/l'angle de chaque vidéo vient d'une **recherche web + analyse de ce qui fonctionne** pour le sujet (formats viraux, hooks, angles d'analyse technique, audience FR). Recherche avant de proposer ; jamais 2 vidéos identiques. Visuel = métaphore abstraite (zéro chiffre à l'écran). Le terme technique exact (VWAP, doji…) est porté par la narration/description, jamais par l'image.

## RÈGLE DE NEUTRALISATION VISUELLE (concepts financiers)
Tout concept évoquant argent/prix/chiffre (ex. coût, tick value, payout, levier) : les **chiffres, montants, $, prix, valeurs** sont autorisés **UNIQUEMENT en narration (TTS)** — **JAMAIS générés à l'écran par Seedance** (le modèle classe le visuel financier chiffré comme spéculatif → rejet IP). Le visuel reste **abstrait et métaphorique** (tick → escalier de lumière sans chiffre ; coût → structure qui se déplie sans $ ; levier → balance sans montant ; news → tempête abstraite non lisible). Table complète des 18 concepts et règles de rendu : skill `lucaspropfirm-shorts-pipeline` → `references/visual-catalog.md` (catalogue v4.2 — source de vérité).

## COHÉRENCE TRANSVERSALE
- Même palette bleu nuit + or/lime sur tous les concepts.
- Aucun texte lisible généré dans la vidéo (sous-titres ajoutés au montage).
- Signature finale : logo LP rond lime apparaissant les 2 dernières secondes avec un son de validation.
- **Encart de fin (ajouté au montage, dernière seconde)** : afficher "CODE : LUCAS chez phidiaspropfirm.com" et "Discord & formation : lucaspropfirm.fr" pendant la dernière seconde de la vidéo.

## Concepts visuels (18, source de vérité)
Le catalogue officiel et sa rotation sont dans `lucaspropfirm-shorts-pipeline` → `references/visual-catalog.md` (**v4.2**). Ne pas dupliquer ici : toute génération lit le catalogue v4.2. Les anciennes listes (8 concepts, concepts S01-S18 de l'ancienne version) sont **obsolètes et ne doivent plus être utilisées**.

## STRUCTURE DE PROMPT VIDÉO (dans cet ordre)
`SCENE CONTEXT → FIRST FRAME → OPTICS → CAMERA → LIGHTING → PHYSICS → ACTION TIMING → AUDIO` (design sonore ; la voix est ajoutée après en TTS).

### RÈGLES ANTI-IP / ANTI-REFUS (obligatoires dans TOUT prompt visuel)
- **AUCUNE évocation d'argent, gain, paiement, retrait, versement, profit, pièce, monnaie, récompense** (le modèle classe le contenu financier lié à l'argent comme spéculatif → rejet copyright). Remplacer tout objet « valeur/monnaie » par un objet abstrait : « colis abstrait de verre », « objet qui se déplie », « escalier de lumière », « flux de particules ».
- **AUCUNE marque, firme, nom de société, nom de site ou nom de personne** (interdit : Phidias, LucasPropfirm, prop firm, nom d'échange, plateforme). Le visuel est 100 % abstrait et générique.
- **AUCUNE référence précise au monde réel** : pas de « Futures ES/NQ », pas de tick value chiffrée, pas d'horaires boursiers (14h30/16h), pas de chiffres de marché. Tout est métaphorique et visuel.
- **AUCUN texte, chiffre, logo ou UI simulée** généré par le modèle (texte en post-prod uniquement).
- **AUCUNE identité visuelle copiée** : pas de charte, pas de logo, pas d'interface d'une application existante.
- **MOTS DÉCLENCHEURS À BANNIR** : trader, broker, chart seul, trading floor, candlestick (anglais), Bloomberg, terminal, market data, exchange, portfolio, payout, payment, withdrawal, money, coin, gain, profit, price tag, reward, salaire, capital, argent. Remplacer par du vocabulaire générique : « bougies de verre », « écrans abstraits », « ville de verre », « mécanisme », « flux », « colonnes lumineuses », « colis abstrait », « structure qui se révèle ».
- **✅ AUTORISÉ — bougies/chandeliers en verre abstrait** : les chandeliers en verre (corps + mèches en formes de verre lumineux doré/lime sur bleu nuit) sont l'IDENTITÉ VISUELLE DU PROJET et sont autorisés en tant que métaphore abstraite (« océan de chandeliers », « mer de bougies de verre », « une bougie en verre »). Ils restent autorisés TANT QUE : aucun chiffre (pas de valeurs de prix, de $, de montants) ; aucune interface de trading réaliste (pas de graphique broker, de fausse plateforme, de lignes d'axes avec valeurs) ; aucune valeur affichée sur/autour. La bougie de verre SANS interface réaliste = autorisée ; la bougie DANS un graphique chiffré réaliste = refus. **Ne pas bannir les bougies par erreur — c'est l'identité visuelle ; le contexte chiffré/réaliste est interdit.**
- Décrire l'idée par **métaphore visuelle générique** — jamais par son nom réel ni un concept financier nommé.
- Si le sujet est un concept financier, le formuler abstraitement (ex. « un plafond lumineux » pour résistance, « un sol » pour support) sans nommer le produit.

## MODULE HOOK (obligatoire avant toute production)
Le hook est la phrase d'accroche des 0-1,2 s. Il doit être compréhensible SANS le son (appuyé par le visuel). **Aucun short ne part en production sans hook validé.**

### Les 4 patrons de hooks (choisir UN)
1. **Question (Q)** — interpelle directement : « Tu sais lire ce que le marché dit VRAIMENT ? »
2. **Chiffre choc (CH)** — nombre précis, vérifié, qui surprend : « 1 tick = 12,50 $ »
3. **Erreur courante (ER)** — dénonce une fausse croyance : « ES + NQ en même temps ? Tu doubles ton risque »
4. **Contre-intuitif (CI)** — affirme l'inverse de l'intuition : « Le prix affiché n'est pas le prix que tu paies »

Règle : alterner les patrons d'un post à l'autre (jamais 2 hooks du même patron consécutifs). Exemples par concept dans `references/hook-examples.md`.

### CHECK-LIST DE VALIDATION DU HOOK (toutes les cases doivent passer)
- [ ] **1,2 s max** — se dit en moins de 1,2 seconde à l'oral
- [ ] **Compréhensible sans le son** — le visuel du premier plan illustre le hook
- [ ] **Un seul patron** — Q, CH, ER ou CI, pas un mélange
- [ ] **Zéro promesse de gain** — aucun rendement, aucun payout garanti
- [ ] **Zéro stat non sourcée** — banni : « 90 % des traders… » ; tout chiffre est vérifié
- [ ] **Sans jargon** — vocabulaire débutant, aucune abréviation technique non expliquée
- [ ] **Émotion ou curiosité** — crée un manque (peur, surprise, question sans réponse)
- [ ] **Pas de marque ni de nom de firme** dans le hook
- [ ] **Si hook validé → production ; sinon → réécrire avec un autre patron**

## SCRIPT NARRATION (structure 15 s, 38-42 mots max)
- **0-1,2 s** : HOOK choc (chiffre, erreur, question) — verrouillé par le module Hook
- **1,2-4 s** : problème / mise en situation
- **4-9 s** : explication — 1 seule idée, vocabulaire débutant
- **9-13 s** : règle à retenir
- **13-15 s** : **CTA UNIQUE FIXE (exact, à dire tel quel en fin de narration)** — "Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com." (jamais un autre CTA, jamais reformulé, jamais omis. La narration totale doit tenir dans ~15 s pour que ce CTA soit entièrement audible — ~35-40 mots + CTA.)

## DESCRIPTION IG (format fixe)
accroche émoji → lignes "👉" → "🎓 abonne-toi" → bloc liens complet (Phidias / lucaspropfirm.fr / PropLog / Newsletter / Affiliation / Limova PROFILM30). Dire "jusqu'à -80 %", jamais garanti.

### Bloc de liens (aligné, 1 ligne par lien — TOUJOURS COMPLET, jamais tronqué)
**FORMAT OBLIGATOIRE : chaque ligne du bloc de liens est SÉPARÉE par un retour à la ligne (saut de ligne). Jamais collées sur une seule ligne.**
```
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidias : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
📒 Journal de trading PropLog : https://www.proplog.fr/
📰 Newsletter lucaspropfirm : https://lucaspropfirm.fr/newsletters.html
📰 Newsletter Proplog : https://proplog.fr/newsletter/
🤝 Affiliation : https://lucaspropfirm.fr/Affiliation.html
🎁 Limova code promo PROFILM30 : https://limova.ai/?linkId=lp_079563&sourceId=lucas-lansmant&tenantId=limova
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
🤖 Wisewand.ai (EN) (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/en/?fpr=lucas
```
**IMPORTANT :**
- Le bloc de liens de TOUTE description (YouTube/TikTok/IG/X/LinkedIn) doit toujours contenir les 9 lignes, y compris Wisewand (FR + EN) et Newsletter Proplog.
- **Chaque lien est sur sa propre ligne** (retour à la ligne entre chaque). Ne jamais tout coller sur une seule ligne.
- Structure complète d'une description : ligne d'accroche → une ligne vide → contenu (1-2 lignes) → une ligne vide → bloc de liens (9 lignes, chacune sur sa ligne).

### Exemple — Éducation
```
📉 Le trading, tout le monde en parle. Mais c'est quoi exactement ?
👉 Acheter un actif quand son prix baisse, pour le revendre quand il monte. Et l'inverse.
🎓 On reconstruit les bases, une brique par jour — abonne-toi.
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidias : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
📒 Journal de trading PropLog : https://www.proplog.fr/
📰 Newsletter lucaspropfirm : https://lucaspropfirm.fr/newsletters.html
📰 Newsletter Proplog : https://proplog.fr/newsletter/
🤝 Affiliation : https://lucaspropfirm.fr/Affiliation.html
🎁 Limova code promo PROFILM30 : https://limova.ai/?linkId=lp_079563&sourceId=lucas-lansmant&tenantId=limova
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
🤖 Wisewand.ai (EN) (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/en/?fpr=lucas
```

## RÈGLE DE VALIDATION
Proposer d'abord le **concept + script + prompt complet**, attendre la **validation utilisateur**, puis **confirmer les crédits AVANT toute génération**. Ne jamais générer sans double validation.

## Règles
- Langue : français. Codes **LUCAS** et **PROFILM30** complets, jamais modifiés.
- Réduction Phidias : toujours "jusqu'à -80 %" (jamais garanti), vérifier l'offre officielle avant publication.
- Ne pas mélanger avec les liens Proplog-only (Proplog a son propre CTA : https://www.proplog.fr/ et https://proplog.fr/newsletter/).
---
name: lucaspropfirm-short-description
description: |
  Source de vérité CRÉATIVE des shorts lucaspropfirm (trading Futures ES/NQ, prop firms, audience FR). Charger pour tout ce qui touche au CONTENU d'un short : format technique, univers visuel, règles anti-IP des prompts, recette de prompt vidéo (8 blocs en français, anti-générique, exemple figé), module hook, script de narration (CTA oral court + CTA écrit complet), zones sûres 9:16, description IG/TikTok/YouTube (bloc de liens 10 lignes). Pour la procédure d'exécution (génération, montage voix, sous-titres) → skill lucaspropfirm-shorts-generation. Pour l'orchestration, la recherche de concept et le journal → skill lucaspropfirm-shorts-pipeline.
---

# Spec créative des shorts lucaspropfirm

> Périmètre : **source de vérité pour tout le contenu** (visuel, prompt, narration, description). Il ne décrit PAS l'exécution (voir `lucaspropfirm-shorts-generation`) ni l'orchestration (voir `lucaspropfirm-shorts-pipeline`).
> **Précédence** : les skills LP généralistes (`hook-generator-lp`, `reels-scripter-lp`, `legendes-ig-lp`, `createur-de-poste`) peuvent servir à **générer des candidats** (hooks, scripts, légendes). En cas de conflit, **ce skill gagne** : checklist hook, CTA, bloc de liens, anti-IP.

## CONTEXTE COMPTE
@lucaspropfirm01 — trading **Futures ES/NQ**, prop firms, audience FR débutante/intermédiaire. Objectif : vues + commentaires → Discord gratuit → conversion Phidias (code **LUCAS**) et Discord Pro/Élite.

## FORMAT TECHNIQUE (non négociable)
- Modèle : **Seedance 2.0 Mini, 720p, 9:16, 15 secondes — FIGÉ, ne jamais proposer un autre modèle ni une autre résolution.** La qualité vient du prompt (recette ci-dessous), pas du modèle.
- **Aucun texte lisible** à l'écran dans la vidéo générée
- Narration TTS voix **"Julian"** en français (moteur ElevenLabs ; jamais `voice_change`)
- La vidéo est générée **muette** (`generate_audio=false`) ; la voix est montée en post-prod (jamais en référence audio dans la génération).

## UNIVERS VISUEL — "marché financier vivant" · FUTURISTE PREMIUM
Style : animation 3D stylisée **futuriste de haute qualité** (rendu cinématique, type film de science-fiction financier), bleu nuit profond + accents or/lime, **SANS visage humain**, ambiance premium fintech. **Matériaux riches** (verre fumé, métal brossé, chrome, surfaces réfléchissantes, lumières HDR), **éclairage cinématique** (rim light bleu froid + halos or/lime + bokeh, jamais plat), **détails fintech** (micro-textures, particules lumineuses, hologrammes abstraits, HUD flottants sans texte lisible), **échelle et profondeur** (volumes monumentaux ou intimes avec profondeur de champ et couches FG/MG/BG), **mouvement fluide** (dolly lent, transitions organiques). Cohérent avec la charte branding (bleu nuit + lime-jaune, logo LP rond).

### Cohérence transversale
- Même palette bleu nuit + or/lime sur tous les shorts ; rouge/vert = signaux uniquement.
- Aucun texte lisible généré dans la vidéo (sous-titres ajoutés au montage).
- Signature finale (au montage) : logo LP rond lime sur les **2 dernières secondes** + son de validation.
- **Encart de fin (au montage, dernière seconde)** : « CODE : LUCAS chez phidiaspropfirm.com » et « Discord & formation : lucaspropfirm.fr ». C'est là que vit le **CTA écrit complet**.

### Zones sûres 9:16 (720×1280) — rien d'important hors de ces zones
- **Sous-titres** : bas de l'image, dans la safe zone Reels (bas 16,7 %, côtés 11 %), 2 lignes max.
- **Logo LP** : haut-gauche (≈ 6 % de marge, ≈ 10 % du haut).
- **Encart de fin** : centré dans le **tiers haut** (≈ 14-24 % du haut) — jamais en bas (UI TikTok/Reels + sous-titres).
- Colonne droite (≈ 12 %) réservée aux icônes plateforme ; **hook visuel centré**.

## RÈGLES ANTI-IP / ANTI-REFUS (obligatoires dans TOUT prompt visuel)
Higgsfield/Seedance renvoie **"Rejected due to copyright restrictions."** dès qu'un prompt évoque l'argent ou un élément réel. C'est un vrai rejet IP, pas un rate-limit.
- **AUCUNE évocation d'argent, gain, paiement, retrait, versement, profit, pièce, monnaie, récompense, salaire, capital.** Remplacer par un objet abstrait : « colis abstrait de verre », « objet qui se déplie », « escalier de lumière », « flux de particules ».
- **AUCUNE marque, firme, société, site, personne** (interdit : Phidias, LucasPropfirm, prop firm, nom d'échange, plateforme). Visuel 100 % abstrait et générique.
- **AUCUNE référence réelle précise** : pas de « Futures ES/NQ », pas de tick value chiffrée, pas d'horaires boursiers, pas de chiffres de marché. Tout est métaphorique.
- **AUCUN texte, chiffre, logo ou UI simulée** généré par le modèle (texte en post-prod uniquement).
- **MOTS DÉCLENCHEURS À BANNIR** : trader, broker, trading floor, candlestick (EN), Bloomberg, terminal, market data, exchange, portfolio, payout, payment, withdrawal, money, coin, gain, profit, price tag, reward, salaire, capital, argent. → remplacer par « bougies de verre », « écrans abstraits », « ville de verre », « mécanisme », « flux », « colonnes lumineuses », « colis abstrait », « structure qui se révèle ».
- **✅ AUTORISÉ — bougies/chandeliers en verre abstrait** (corps + mèches en verre lumineux doré/lime sur bleu nuit) : c'est **l'IDENTITÉ VISUELLE DU PROJET** (« océan de chandeliers », « mer de bougies de verre », « une bougie en verre »). Autorisées TANT QUE : aucun chiffre, aucune interface de trading réaliste, aucune valeur affichée. La bougie de verre SANS interface = autorisée ; la bougie DANS un graphique chiffré réaliste = refus.
- Tout concept financier est formulé par **métaphore abstraite** (résistance → « plafond lumineux » ; support → « un sol » ; levier → balance sans montant ; news → tempête abstraite). Les chiffres/montants sont autorisés **uniquement en narration TTS**, jamais à l'écran.

## PROMPT VIDÉO — RECETTE (8 blocs, en français, non générique)

### Langue et forme
- **Le prompt est écrit en français.** Narration en français. (Seedance est entraîné surtout en anglais/chinois : si un même prompt donne **deux** plans faibles, tester sa traduction anglaise à l'identique et noter le résultat au journal — le français reste la règle.)
- **130-200 mots**, **8 blocs dans cet ordre, une ligne par bloc**, jamais de paragraphe libre :
  `CONTEXTE DE SCÈNE → PREMIÈRE IMAGE → OPTIQUE → CAMÉRA → LUMIÈRE → PHYSIQUE → TIMING DE L'ACTION → AUDIO`
- Seedance n'a **pas de negative prompt** : « aucune personne, aucun visage, aucun texte, aucun chiffre, aucun symbole » s'écrit **dans** le CONTEXTE, positivement.

### Ce que chaque bloc doit contenir
| Bloc | Attendu | À éviter |
|---|---|---|
| CONTEXTE DE SCÈNE | Le lieu, l'atmosphère, **3 matériaux nommés**, la phrase d'exclusion (personne/texte/chiffre) | Adjectifs vides (« magnifique », « futuriste » seul) |
| PREMIÈRE IMAGE (0-1,2 s) | **Le hook en image** : un objet, un cadrage, un micro-événement lisible sans le son | Un plan d'ensemble neutre |
| OPTIQUE | Focale, profondeur de champ, bokeh, flare | « cinématique » sans précision |
| CAMÉRA | **Un** mouvement précis (travelling arrière, contre-plongée, tilt, plan fixe final) et sa révélation | Plusieurs mouvements empilés |
| LUMIÈRE | Rim light bleu froid + halos or/lime, brume volumétrique, contraste | « bien éclairé », lumière plate |
| PHYSIQUE | **Un événement physique** (empilement, fissure, chute, pulsation, ondulation) avec inertie et reflets cohérents | Mouvement flottant sans cause |
| TIMING DE L'ACTION | Format imposé `0-1,2 s … / 1,2-4 s … / 4-8,5 s … / 8,5-12 s … / 12-15 s …` — **un événement visuel par temps** ; le temps **8,5-12 s porte la règle du script** par un signal fort | Une action continue sans temps |
| AUDIO | Design sonore uniquement (bourdonnement, tintements) ; **pas de musique, pas de voix** (voix en TTS après) | Musique avec paroles |

### Anti-générique (obligatoire)
- **Une signature visuelle par short**, dérivée du concept après la recherche : un objet ou un phénomène qu'on ne retrouve dans **aucun** autre short du journal (`shorts/production-log.md`, colonne « famille de plan »). Ex. escalier de lumière, ligne rouge poursuivante, plafond de verre qui se fissure, balance de verre sans poids.
- **Une seule métaphore** par short ; jamais deux univers mélangés.
- **Test du sujet** : si le prompt pourrait servir tel quel à un autre sujet, il est générique → réécrire.
- **Mots interdits (génériques)** : « magnifique », « futuriste » seul, « particules abstraites » seules, « ville futuriste », « hologramme » sans objet précis, « ambiance tech », « graphique », « données ».
- **Obligatoires** : 3 matériaux nommés · 1 échelle assumée (intime ou monumentale) · 1 événement physique · 1 mouvement caméra · 1 point de lumière signature.
- Le visuel **raconte** la règle du script (temps 8,5-12 s) — ce n'est pas une décoration derrière une voix.

### Checklist avant lancement (toutes les cases)
- [ ] Français · 130-200 mots · 8 blocs · une ligne par bloc
- [ ] Scan anti-IP = 0 mot banni ; phrase d'exclusion présente dans CONTEXTE
- [ ] Hook lisible en PREMIÈRE IMAGE sans le son
- [ ] TIMING en 5 temps alignés sur le script ; règle portée à 8,5-12 s
- [ ] Une seule métaphore ; signature visuelle absente du journal
- [ ] Aucun mot de la liste « génériques »

### Exemple de référence (style figé) — sujet « 1 tick »
```
CONTEXTE DE SCÈNE : Un océan sombre de bougies en verre lumineuses sous un ciel bleu nuit. Atmosphère de science-fiction financière haut de gamme : verre fumé, chrome brossé, reflets HDR. Aucune personne, aucun visage, aucun texte, aucun chiffre, aucun symbole dans l'image.
PREMIÈRE IMAGE (0-1,2 s) : Très gros plan sur une seule bougie en verre qui brille or ; une minuscule marche de lumière se détache de son bord et s'élève.
OPTIQUE : Rendu 35 mm anamorphique, faible profondeur de champ, bokeh doux, léger flare sur les reflets lime.
CAMÉRA : Lent travelling arrière avec une légère contre-plongée, révélant que la marche est la première d'un escalier de lumière monumental qui s'élève de la mer de bougies ; fin sur un plan large en contre-plongée, caméra fixe.
LUMIÈRE : Rim light bleu froid depuis l'horizon, halos or et lime chauds sur chaque marche, brume volumétrique, contraste cinématique, jamais plat.
PHYSIQUE : Les marches se matérialisent une à une avec une ondulation de verre ; les particules montent avec une inertie réaliste ; les reflets restent physiquement cohérents.
TIMING DE L'ACTION : 0-1,2 s bougie seule + première marche / 1,2-4 s trois marches s'empilent / 4-8,5 s l'escalier grandit pendant que la caméra recule / 8,5-12 s une marche pulse plus fort, un signal d'alerte / 12-15 s l'escalier se stabilise, caméra fixe.
AUDIO : Bourdonnement ambiant profond, tintements de verre doux sur chaque marche, pas de musique, pas de voix.
```

## MODULE HOOK (obligatoire avant toute production)
Le hook est la phrase d'accroche des 0-1,2 s. Il doit être compréhensible **sans le son** (appuyé par le visuel). **Aucun short ne part en production sans hook validé.**

### Les 4 patrons (choisir UN, alterner d'un post à l'autre — vérifier dans `shorts/production-log.md`)
1. **Question (Q)** : « Tu sais lire ce que le marché dit VRAIMENT ? »
2. **Chiffre choc (CH)** : « 1 tick = 12,50 $ » (vérifié)
3. **Erreur courante (ER)** : « ES + NQ en même temps ? Tu doubles ton risque »
4. **Contre-intuitif (CI)** : « Le prix affiché n'est pas le prix que tu paies »

### Check-list de validation du hook (toutes les cases)
- [ ] **1,2 s max** à l'oral
- [ ] **Compréhensible sans le son** (le premier plan illustre le hook)
- [ ] **Un seul patron** (Q, CH, ER ou CI), **différent du post précédent** (journal)
- [ ] **Zéro promesse de gain**, **zéro stat non sourcée** (banni : « 90 % des traders… »)
- [ ] **Sans jargon** non expliqué ; **pas de marque ni de firme** dans le hook
- [ ] **Émotion ou curiosité** (crée un manque)
- [ ] Validé → production ; sinon → réécrire avec un autre patron

## SCRIPT NARRATION (15 s)
**Budget : 34-38 mots au total, CTA oral inclus** (ElevenLabs lit à ≈ 2,4-2,6 mots/s ; la durée réelle est mesurée sur la voix par le gate de `shorts-generation` — c'est elle qui fait foi, pas le compte de mots).

| Temps | Contenu | Mots |
|---|---|---|
| 0-1,2 s | **HOOK** (verrouillé par le module Hook) | 3-6 |
| 1,2-4 s | problème / mise en situation | 6-8 |
| 4-8,5 s | explication — **1 seule idée**, vocabulaire débutant | 10-12 |
| 8,5-12 s | règle à retenir | 7-9 |
| 12-15 s | **CTA ORAL FIXE** (7 mots, dit tel quel) | 7 |

**CTA ORAL FIXE (fin de narration, jamais reformulé ni omis)** :
« Code LUCAS chez Phidias, détails sur lucaspropfirm.fr. »

**CTA ÉCRIT COMPLET (encart de fin + toutes les descriptions, jamais reformulé)** :
« Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com. »

> Pourquoi deux CTA : le CTA complet fait 20 mots ≈ 7-8 s de voix — impossible dans les 3 dernières secondes d'un 15 s sans couper. Il est donc **lu** (encart + description), et le CTA oral court porte le code + le site.

## DESCRIPTION (format fixe, toutes plateformes)
**CTA haut (4 lignes)** → accroche émoji → lignes "👉" → "🎓 abonne-toi" → **CTA écrit complet** → **bloc de liens complet (10 lignes)**. Dire « jusqu'à -80 % », jamais garanti.
- Le **CTA haut** est en toute première position : il reste visible avant le « … plus » des plateformes.
- **TikTok uniquement** : les liens ne sont pas cliquables → ajouter « 🔗 Tout est en bio » juste au-dessus du CTA haut.
- **Lien en bio de tous les comptes (IG, TikTok, YouTube, X)** : le SmartLink Metricool **https://t.mtrbio.com/lucaspropfirm** (10 boutons trackés, stats par bouton dans Metricool → Analytics → SmartLinks). Page de secours sur le domaine : `liens.html` du site (https://lucaspropfirm.fr/liens.html). Quand un post est programmé via Metricool, attacher le SmartLink (`smartLinkData`) pour le tracking.

### CTA haut (4 lignes — TOUJOURS en tête de description, texte exact)
```
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidias : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
```

### Bloc de liens (10 lignes — TOUJOURS COMPLET en bas, chaque lien sur SA propre ligne)
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
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
```
Structure : CTA haut (4 lignes) → ligne vide → accroche → contenu (1-2 lignes) → 🎓 abonne-toi → ligne vide → CTA écrit complet → ligne vide → bloc de liens (10 lignes). Ne jamais tronquer ni coller les liens sur une seule ligne. Le CTA haut et le bloc de liens se répètent volontairement (haut = visible sans dérouler ; bas = complet).

### Exemple complet — Éducation
```
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidias : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas

📉 Un tick, c'est combien, vraiment ?
👉 Chaque petit mouvement du marché a une valeur fixe. Et elle s'additionne vite.
👉 Connais la valeur du tick avant de cliquer.
🎓 On reconstruit les bases, une brique par jour — abonne-toi.

Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com.

🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidias : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
📒 Journal de trading PropLog : https://www.proplog.fr/
📰 Newsletter lucaspropfirm : https://lucaspropfirm.fr/newsletters.html
📰 Newsletter Proplog : https://proplog.fr/newsletter/
🤝 Affiliation : https://lucaspropfirm.fr/Affiliation.html
🎁 Limova code promo PROFILM30 : https://limova.ai/?linkId=lp_079563&sourceId=lucas-lansmant&tenantId=limova
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
🤖 Wisewand.ai (EN) (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/en/?fpr=lucas
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
```

## RÈGLE DE VALIDATION
Proposer d'abord **concept + hook + script + prompt complet + description**, attendre la **validation utilisateur**, puis **confirmer le coût (`get_cost`) AVANT toute génération**. Jamais de génération sans double validation.

## Règles
- Langue : français. Codes **LUCAS** et **PROFILM30** complets, jamais modifiés.
- Réduction Phidias : toujours « jusqu'à -80 % » (jamais garanti), vérifier l'offre officielle avant publication.
- Ne pas mélanger avec les liens Proplog-only (Proplog a son propre CTA : https://www.proplog.fr/ et https://proplog.fr/newsletter/).
- Interdits transversaux : Limova sur le compte trading, contenu EN sur le compte FR, 16:9, chandeliers génériques sans contexte, fausses interfaces broker, lifestyle richesse.

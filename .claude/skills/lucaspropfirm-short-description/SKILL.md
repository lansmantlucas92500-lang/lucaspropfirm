---
name: lucaspropfirm-short-description
description: |
  Source de vérité CRÉATIVE des shorts lucaspropfirm (trading Futures ES/NQ, prop firms, audience FR). Charger pour tout ce qui touche au CONTENU d'un short : format technique, univers visuel, règles anti-IP des prompts, structure de prompt vidéo, module hook, script de narration + CTA, description IG (émojis + bloc de liens). Pour la procédure d'exécution (génération, montage voix, sous-titres) → skill lucaspropfirm-shorts-generation. Pour l'orchestration et le choix du concept par recherche → skill lucaspropfirm-shorts-pipeline.
---

# Spec créative des shorts lucaspropfirm

> Périmètre : ce skill est la **source de vérité pour tout le contenu** (visuel, prompt, narration, description). Il ne décrit PAS la procédure d'exécution (voir `lucaspropfirm-shorts-generation`) ni l'orchestration (voir `lucaspropfirm-shorts-pipeline`).

## CONTEXTE COMPTE
@lucaspropfirm01 — trading **Futures ES/NQ**, prop firms, audience FR débutante/intermédiaire. Objectif : vues + commentaires → Discord gratuit → conversion Phidias (code **LUCAS**) et Discord Pro/Élite.

## FORMAT TECHNIQUE (non négociable)
- Modèle : **Seedance 2.0 Mini**, 720p, **9:16**, **15 secondes maximum**
- **Aucun texte lisible** à l'écran dans la vidéo générée
- Narration TTS voix **"Julian"** en français (jamais change_voice — Mini prononce mal le FR)
- La vidéo est générée **muette** (`generate_audio=false`) ; la voix Julian est montée en post-prod (jamais en référence audio dans la génération).

## UNIVERS VISUEL — "marché financier vivant" · FUTURISTE PREMIUM
Style : animation 3D stylisée **futuriste de haute qualité** (rendu cinématique, type film de science-fiction financier), bleu nuit profond + accents or/lime, **SANS visage humain**, ambiance premium fintech. **Matériaux riches** (verre fumé, métal brossé, chrome, surfaces réfléchissantes, lumières HDR), **éclairage cinématique** (rim light bleu froid + halos or/lime + bokeh, jamais plat), **détails fintech** (micro-textures, particules lumineuses, hologrammes abstraits, HUD flottants sans texte lisible), **échelle et profondeur** (volumes monumentaux ou intimes avec profondeur de champ et couches FG/MG/BG), **mouvement fluide** (dolly lent, transitions organiques). Cohérent avec la charte branding (bleu nuit + lime-jaune, logo LP rond).

### Cohérence transversale
- Même palette bleu nuit + or/lime sur tous les shorts ; rouge/vert = signaux uniquement.
- Aucun texte lisible généré dans la vidéo (sous-titres ajoutés au montage).
- Signature finale : logo LP rond lime sur les 2 dernières secondes + son de validation.
- **Encart de fin (au montage, dernière seconde)** : "CODE : LUCAS chez phidiaspropfirm.com" et "Discord & formation : lucaspropfirm.fr".

## RÈGLES ANTI-IP / ANTI-REFUS (obligatoires dans TOUT prompt visuel)
Higgsfield/Seedance renvoie **"Rejected due to copyright restrictions."** dès qu'un prompt évoque l'argent ou un élément réel. C'est un vrai rejet IP, pas un rate-limit.
- **AUCUNE évocation d'argent, gain, paiement, retrait, versement, profit, pièce, monnaie, récompense, salaire, capital.** Remplacer par un objet abstrait : « colis abstrait de verre », « objet qui se déplie », « escalier de lumière », « flux de particules ».
- **AUCUNE marque, firme, société, site, personne** (interdit : Phidias, LucasPropfirm, prop firm, nom d'échange, plateforme). Visuel 100 % abstrait et générique.
- **AUCUNE référence réelle précise** : pas de « Futures ES/NQ », pas de tick value chiffrée, pas d'horaires boursiers, pas de chiffres de marché. Tout est métaphorique.
- **AUCUN texte, chiffre, logo ou UI simulée** généré par le modèle (texte en post-prod uniquement).
- **MOTS DÉCLENCHEURS À BANNIR** : trader, broker, trading floor, candlestick (EN), Bloomberg, terminal, market data, exchange, portfolio, payout, payment, withdrawal, money, coin, gain, profit, price tag, reward, salaire, capital, argent. → remplacer par « bougies de verre », « écrans abstraits », « ville de verre », « mécanisme », « flux », « colonnes lumineuses », « colis abstrait », « structure qui se révèle ».
- **✅ AUTORISÉ — bougies/chandeliers en verre abstrait** (corps + mèches en verre lumineux doré/lime sur bleu nuit) : c'est **l'IDENTITÉ VISUELLE DU PROJET** (« océan de chandeliers », « mer de bougies de verre », « une bougie en verre »). Autorisées TANT QUE : aucun chiffre, aucune interface de trading réaliste, aucune valeur affichée. La bougie de verre SANS interface = autorisée ; la bougie DANS un graphique chiffré réaliste = refus.
- Tout concept financier est formulé par **métaphore abstraite** (résistance → « plafond lumineux » ; support → « un sol » ; levier → balance sans montant ; news → tempête abstraite). Les chiffres/montants sont autorisés **uniquement en narration TTS**, jamais à l'écran.

## STRUCTURE DE PROMPT VIDÉO (8 blocs, dans cet ordre)
`SCENE CONTEXT → FIRST FRAME → OPTICS → CAMERA → LIGHTING → PHYSICS → ACTION TIMING → AUDIO` (design sonore ; la voix est ajoutée après en TTS).

## MODULE HOOK (obligatoire avant toute production)
Le hook est la phrase d'accroche des 0-1,2 s. Il doit être compréhensible **sans le son** (appuyé par le visuel). **Aucun short ne part en production sans hook validé.**

### Les 4 patrons (choisir UN, alterner d'un post à l'autre)
1. **Question (Q)** : « Tu sais lire ce que le marché dit VRAIMENT ? »
2. **Chiffre choc (CH)** : « 1 tick = 12,50 $ » (vérifié)
3. **Erreur courante (ER)** : « ES + NQ en même temps ? Tu doubles ton risque »
4. **Contre-intuitif (CI)** : « Le prix affiché n'est pas le prix que tu paies »

### Check-list de validation du hook (toutes les cases)
- [ ] **1,2 s max** à l'oral
- [ ] **Compréhensible sans le son** (le premier plan illustre le hook)
- [ ] **Un seul patron** (Q, CH, ER ou CI)
- [ ] **Zéro promesse de gain**, **zéro stat non sourcée** (banni : « 90 % des traders… »)
- [ ] **Sans jargon** non expliqué ; **pas de marque ni de firme** dans le hook
- [ ] **Émotion ou curiosité** (crée un manque)
- [ ] Validé → production ; sinon → réécrire avec un autre patron

## SCRIPT NARRATION (15 s, 38-42 mots max)
- **0-1,2 s** : HOOK choc (verrouillé par le module Hook)
- **1,2-4 s** : problème / mise en situation
- **4-9 s** : explication — 1 seule idée, vocabulaire débutant
- **9-13 s** : règle à retenir
- **13-15 s** : **CTA UNIQUE FIXE (exact, jamais reformulé ni omis)** — « Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com. »

## DESCRIPTION IG (format fixe)
accroche émoji → lignes "👉" → "🎓 abonne-toi" → **bloc de liens complet**. Dire « jusqu'à -80 % », jamais garanti.

### Bloc de liens (9 lignes — TOUJOURS COMPLET, chaque lien sur SA propre ligne)
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
Structure : accroche → ligne vide → contenu (1-2 lignes) → ligne vide → bloc de liens (9 lignes). Ne jamais tronquer ni coller les liens sur une seule ligne.

## RÈGLE DE VALIDATION
Proposer d'abord **concept + script + prompt complet**, attendre la **validation utilisateur**, puis **confirmer les crédits AVANT toute génération**. Jamais de génération sans double validation.

## Règles
- Langue : français. Codes **LUCAS** et **PROFILM30** complets, jamais modifiés.
- Réduction Phidias : toujours « jusqu'à -80 % » (jamais garanti), vérifier l'offre officielle avant publication.
- Ne pas mélanger avec les liens Proplog-only (Proplog a son propre CTA : https://www.proplog.fr/ et https://proplog.fr/newsletter/).

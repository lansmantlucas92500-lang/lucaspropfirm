---
name: "lucaspropfirm-shorts-generation"
description: "Produces lucaspropfirm French trading education shorts on Higgsfield/Seedance 2.0 Mini with copyright-safe prompts and mandatory Julian voice montage; use whenever generating, relaunching, or debugging lucaspropfirm shorts."
---
# lucaspropfirm Shorts Generation (corrected pipeline)

Standing procedure for producing the 35 lucaspropfirm shorts. Built from
the 2026-08 session where ~1h was lost to copyright rejections, missing
voice, and credit-wasting retry loops. Follow every rule — none is optional.

## 1. Pipeline (one short, end to end)

```
script(38-42 mots) → narration Julian (TTS FR) → vidéo Seedance 2.0 Mini
(prompt copyright-safe) → MONTAGE ffmpeg (voix+vidéo) → VÉRIF audio →
SOUS-TITRES automatiques (burn) → vérif sous-titres → livrable
```

- A short is NOT a deliverable until the Julian voice is fused AND verified.
- Fusion via ffmpeg is mandatory and never skipped. Verify an `aac`/audio
  stream exists AND that the audio is the Julian narration (not silence).
- Do NOT re-ask for validation on every step once a production mandate is
  given — proceed within it (see double-validation rule in memory).

## 2bis. SOUS-TITRES AUTOMATIQUES (obligatoires, après le montage voix)

Chaque short livré DOIT avoir ses sous-titres brûlés (burned) dans l'image.
Utiliser le skill `video-subtitler` (dossier scripts : /home/.hermes/skills/video-subtitler) :

1. **Transcrire** sur l'audio le plus propre (la narration montée) :
   `python3 scripts/audio_to_captions.py video.mp4 --srt caps.srt --mixed --language fr`
   (timings TOUJOURS mesurés depuis l'audio réel, jamais estimés. Si le texte
   narré existe (script 38-42 mots), le passer en `--script` pour que les mots
   affichés correspondent exactement à la narration.)
2. **Vérifier la transcription avant de brûler** : contrôler la présence de
   toutes les phrases de la narration (spot-check 3 indices) ; ne JAMAIS brûler
   une transcription incomplète.
3. **Brûler** avec le style par défaut des shorts (UGC/TikTok) :
   `python3 scripts/subtitle_paper_burn.py --in video.mp4 --srt caps.srt --out final_subbed.mp4 --style bold --font-key tiktok`
   (ou `clean` si dépendances fines).
4. **Vérifier le burn** : durée audio == durée vidéo (±0,2 s), sous-titres
   présents et lisibles sur frames d'échantillon.
5. Renommer en `final_subbed.mp4` comme livrable final. Garder le `.srt` à côté.

Règle : un short sans sous-titres n'est PAS livré comme finalisé (SURTOUT
sur TikTok/Shorts où les captions sont essentielles). En cas d'indisponibilité
de Whisper : livrer sans sous-titres et le signaler (jamais bloquer la
livraison).

## 2. Anti-copyright rules (THE headline fix)

Higgsfield/Seedance rejects prompts with **"Rejected due to copyright
restrictions."** This is a REAL rejection type (confirmed by screenshot), NOT
a rate-limit. It is triggered by financial/monetary imagery.

### NEVER evoke in a video prompt
argent, gain, paiement, retrait, versement, profit, pièce, monnaie, récompense,
salaire, capital, payout, payment, withdrawal, money, coin, gain, profit,
price tag, reward; brands (Phidias, LucasPropfirm, Bloomberg); real instruments
(Futures ES/NQ, tick values, market hours); simulated text/UI/logos/charts.

### Use ONLY abstract visual metaphors
- ❌ "colis payout / sablier de pièces" → ✅ "colis abstrait de verre franchissant
  des portiques lumineux"
- ❌ "étiquette de prix / coûts cachés" → ✅ "structure de verre qui se déplie en
  volets"
- ❌ "escalier de pièces/ticks" → ✅ "escalier de lumière"
- ❌ "trailing drawdown" → ✅ "ligne rouge poursuivante / limite"
- ✅ generic vocab: bougies de verre, écrans abstraits, ville de verre, colonnes
  lumineuses, mécanisme, flux, colis abstrait, structure qui se révèle.

### ✅ AUTORISÉ : bougies / chandeliers en verre abstrait
Les **bougies et chandeliers en verre abstrait** (corps + mèches comme formes de
verre lumineux, doré/lime sur bleu nuit) sont **AUTORISÉS et constituent
l'identité visuelle du projet** (ex. "océan de chandeliers", "mer de bougies de
verre", "une bougie en verre gravée"). Ils restent autorisés TANT QUE :
- **AUCUN chiffre** (pas de valeurs de prix, pas de $, pas de montants)
- **AUCUNE interface de trading réaliste** (pas de graphique broker, pas de
  fausse plateforme, pas de lignes d'axes avec valeurs)
- **AUCUNE valeur affichée** sur ou autour des bougies

La distinction : la bougie de verre **sans chiffres et sans interface réaliste**
= autorisée. La bougie **dans un faux graphique avec prix/valeurs lisibles** =
refus IP. Ne jamais bannir les bougies par erreur — elles sont l'identité visuelle
du projet ; c'est le contexte chiffré/réaliste qui est interdit.

## 3. Failure handling — STOP, do not loop

- When a generation fails, treat it as a copyright/prompt problem first.
- Do NOT auto-retry in a loop — it burns credits without result.
- Fix the prompt (remove any monetary term) and show the user the reformulated
  prompt before relaunching.
- If the same concept keeps failing, skip it and note it; do not hammer.

## 4. Concurrency caution

The account appears capped around ~8 simultaneous jobs. Launching big batches
(7 at once) produced near-total failures in this session. Prefer sequential:
1 video → wait for `completed` → short pause → next. If the user insists on a
batch of 7, warn that failure rate is high and credits are consumed on failure.

## 5. Script contract (reference)

- 38-42 mots, hook in 0-1,2 s (NOT 0-3 s), 5-beat structure:
  0-1,2 / 1,2-4 / 4-9 / 9-13 / 13-15.
- CTA UNIQUE FIXE en fin de narration (obligatoire, jamais remplacé) :
  « Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr,
  pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com. »
  (La narration totale ~35-40 mots + ce CTA doit tenir dans ~15 s.)
- BANNED phrase: « 90% des traders échouent… » (unsourced stat).
- Prompt structure (8 blocs): SCENE CONTEXT → FIRST FRAME → OPTICS → CAMERA →
  LIGHTING → PHYSICS → ACTION TIMING → AUDIO.

## 6. Concept selection (reference)

- **Aucune rotation programmée.** Le concept/angle de chaque short est choisi par
  **recherche web + analyse de ce qui fonctionne** pour le sujet (hooks, formats,
  angles d'analyse technique, audience FR). Rechercher avant de proposer ; jamais
  2 vidéos identiques.
- Anti-IP : zéro chiffre à l'écran, pas d'interface broker réaliste, bougies en
  verre abstraites = identité visuelle autorisée.
- X post description format + codes (LUCAS, PROFILM30, « jusqu'à -80 % ») live
  in memory.
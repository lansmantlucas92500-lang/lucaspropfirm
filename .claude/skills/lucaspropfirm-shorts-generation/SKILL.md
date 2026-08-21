---
name: lucaspropfirm-shorts-generation
description: "Procédure d'EXÉCUTION des shorts lucaspropfirm sur Higgsfield/Seedance 2.0 Mini : loi anti-échecs (1 job à la fois), génération muette, montage voix Julian obligatoire, sous-titres, gestion des échecs. Charger pour générer, relancer ou débuguer un short. Règles créatives (anti-IP, prompt, script) → skill lucaspropfirm-short-description."
---

# lucaspropfirm — génération des shorts (procédure d'exécution)

> Périmètre : ce skill décrit **COMMENT produire** un short techniquement. Les règles de CONTENU (anti-IP, structure de prompt 8 blocs, script + CTA, description IG) vivent dans `lucaspropfirm-short-description` — s'y référer, ne pas les redupliquer ici.

## 1. Pipeline (un short, de bout en bout)

```
script (voir short-description) → narration Julian (TTS FR) → vidéo Seedance 2.0 Mini muette
→ MONTAGE ffmpeg (voix + vidéo) → VÉRIF audio → SOUS-TITRES burn → vérif → livrable
```

Séquence stricte, un short à la fois :
**narration(i) → vidéo muette(i) → montage voix(i) → vérif(i) → sous-titres(i) → livraison(i) → narration(i+1).**
Un short n'est PAS un livrable tant que la voix Julian n'est pas fusionnée ET vérifiée.

## 2. Loi de génération anti-échecs (non négociable)
- **JAMAIS de batch.** Lancer **1 seule vidéo à la fois** via `generate_video` avec un seul job, puis attendre le résultat (`job_status` / `jobs_wait`) AVANT la suivante.
- **Pourquoi :** compte plafonné à **~8 jobs simultanés** ; lancer plusieurs vidéos d'un coup → `429 rate_limit` en cascade et crédits brûlés sur échec.
- **Même règle pour l'audio** : narration TTS générée 1 voix à la fois.
- Paramètres de soumission : `model=seedance_2_0_mini`, `aspect_ratio=9:16`, `resolution=720p`, `duration=15`, **`params.generate_audio=false` OBLIGATOIRE** (booléen littéral ; défaut backend = true → si omis → rejet IP). **Aucune image / audio / référence** dans `medias` (text-to-video pur).

## 3. Montage voix Julian (obligatoire, jamais sauté)
1. Générer la narration **TTS Julian** (voice_id Julian, script 38-42 mots + CTA exact).
2. Générer la vidéo **muette**.
3. **Monter la voix sur la vidéo** (ffmpeg, mapper uniquement la piste TTS).
4. **Vérifier** (audio_analyze) : stream `aac` présent, narration audible et non coupée (pas de silence).
5. Seulement alors → passer aux sous-titres.

## 4. Sous-titres automatiques (obligatoires, après le montage voix)
Chaque short livré DOIT avoir ses sous-titres brûlés (skill `video-subtitler`) :
1. **Transcrire** l'audio monté (jamais estimer les timings). Passer le texte narré en `--script` pour un match exact :
   `python3 scripts/audio_to_captions.py video.mp4 --srt caps.srt --mixed --language fr`
2. **Vérifier la transcription** (spot-check 3 phrases) avant de brûler ; jamais brûler une transcription incomplète.
3. **Brûler** (style UGC/TikTok) :
   `python3 scripts/subtitle_paper_burn.py --in video.mp4 --srt caps.srt --out final_subbed.mp4 --style bold --font-key tiktok`
4. **Vérifier le burn** : durée audio == durée vidéo (±0,2 s), sous-titres lisibles sur frames d'échantillon.
5. Livrable final = `final_subbed.mp4` (+ `.srt` à côté).
- Si Whisper indisponible : livrer sans sous-titres et le signaler — jamais bloquer la livraison.

## 5. Gestion des échecs — STOP, ne pas boucler
- Un rejet est d'abord un **problème d'IP/prompt**, pas un rate-limit. Vérifier le prompt contre les règles anti-IP de `short-description` (terme monétaire ? marque ? interface réaliste ?).
- **Ne jamais auto-retenter en boucle** : ça brûle des crédits sans résultat.
- En cas d'échec d'un job : attendre **40-60 s**, corriger le prompt si besoin, puis **retenter UNE fois**. En cas de `429` : pause **90 s**.
- Si le même concept échoue de façon répétée : le noter et passer à autre chose, ne pas s'acharner.
- Ne déclarer un short terminé que si son job vidéo est `completed` ET la voix vérifiée.

## 6. Validation
Double validation utilisateur (idée + coût affiché) avant tout crédit — voir la règle de validation dans `short-description`. Une fois le mandat de production donné, exécuter la séquence sans re-demander à chaque étape.

---
name: lucaspropfirm-shorts-generation
description: "Procédure d'EXÉCUTION des shorts lucaspropfirm sur Higgsfield (MCP) : paramètres figés Seedance 2.0 Mini + voix Julian, loi anti-échecs (1 job à la fois), génération muette, gate de débit TTS, montage voix + sous-titres dans le sandbox Higgsfield (scripts $HF_WORKFLOWS), vérifications, gestion des échecs. Charger pour générer, relancer ou débuguer un short. Règles créatives (anti-IP, prompt, script, CTA) → skill lucaspropfirm-short-description."
---

# lucaspropfirm — génération des shorts (procédure d'exécution)

> Périmètre : **COMMENT produire** un short avec les outils réels du MCP Higgsfield. Les règles de CONTENU (anti-IP, prompt 8 blocs, script + CTA, description) sont dans `lucaspropfirm-short-description` ; l'orchestration et le journal dans `lucaspropfirm-shorts-pipeline`.

## 0. Outils réels (noms exacts du MCP Higgsfield)

| Besoin | Outil | Note |
|---|---|---|
| Voix Julian (TTS) | `generate_audio` | 1 seule ligne par appel |
| Vidéo | `generate_video` | 1 seul job par appel |
| Attendre un job | `jobs_wait` (≤ 15 s par appel, reboucler) | puis `show_generation_by_ids` |
| Coût sans dépenser | `get_cost: true` dans les params | **obligatoire avant chaque génération** |
| Shell média (ffmpeg, ffprobe, faster-whisper, polices) | `sandbox_exec` | sandbox distant Higgsfield — **jamais le shell local** |
| Exporter un fichier du sandbox | `media_upload` (avant) → `curl PUT` (dans la commande) → `media_confirm` (après HTTP 200) | |
| Gate viralité / force du hook | `virality_predictor` (action `create`, media = job_id vidéo) | |
| QC IA scène par scène | `video_analysis_create` (media_id **uploadé**) → `video_analysis_status` | 3-5 min |
| Publier TikTok | `tiktok_prepare_publish` → `tiktok_publish` | URL Higgsfield obligatoire |
| Solde | `balance` | |

Scripts préinstallés dans le sandbox : `$HF_WORKFLOWS/subtitles/scripts/` (`fetch_fonts.sh`, `audio_to_captions.py`, `subtitle_paper_burn.py`, `burn_caps_clean.sh`) et `$HF_WORKFLOWS/narrator/scripts/speech_metrics.sh`. Polices système : `/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf`, `Metropolis-ExtraBold.ttf`.

## 1. Paramètres figés (vérifiés sur le catalogue)

### Vidéo — `generate_video`
```json
{ "model": "seedance_2_0_mini", "prompt": "<prompt 8 blocs, anti-IP>",
  "aspect_ratio": "9:16", "resolution": "720p", "duration": 15,
  "bitrate_mode": "high", "genre": "drama",
  "generate_audio": false, "get_cost": true }
```
- `generate_audio: false` **obligatoire** (défaut backend = `true` → si omis, audio natif + risque de rejet IP).
- **`medias` uniquement pour le personnage Lucas** (§ Personnage récurrent ci-dessous). Sinon text-to-video pur. `audio_references` reste l'ancienne méthode abandonnée : jamais de référence audio.
- Mini = 480p/720p max, 4-15 s. `bitrate_mode: high` = netteté à 720p pour un surcoût nul. `genre: drama` = ambiance cinématique (ou `epic`).
- **Coût mesuré : 37,5 crédits** par vidéo 15 s (solde de référence 1 229 crédits ≈ 32 vidéos).
- Le `prompt` est **en français** (recette et exemple dans `short-description`).
- **Modèle figé : `seedance_2_0_mini` 720p — ne jamais proposer `seedance_2_0`, `seedance_2_5` ni une autre résolution.** La qualité se joue dans le prompt.
- `use_unlim: true` uniquement si l'allocation « unlimited » est active (`models_explore` → `unlim.available`) ; sinon omettre.

### Personnage récurrent « Lucas » — références d'identité

Le personnage à l'effigie de Lucas est verrouillé par **référence d'image**, pas par description
textuelle : décrire « homme de 25 ans en costume » redonne un visage différent à chaque
génération, ce qui est pire que pas de personnage du tout.

`seedance_2_0_mini` accepte nativement les rôles `start_image`, `end_image`, `image_references`,
`video_references` (vérifié sur `models_explore action=get`, tags `reference` · `identity` ·
`consistent`). C'est la voie retenue.

**Le personnage est déjà créé et validé par Lucas (03/09) — ne pas le régénérer.**

| | |
|---|---|
| Fiche 3 vues (`image_references`) | `b5fb893b-ee5a-43de-82f3-d785f478f20e` |
| Element réutilisable | `3b929346-d7ab-4590-b5d6-a090681e6ffe` (`lucas-trader`) |
| Signalement | 23 ans, costume bleu nuit deux pièces, chemise blanche, cravate soie bleu nuit, ceinture cuir brun, derbies noires, montre acier |

Deux voies d'appel, **essayer `image_references` en premier** (documenté pour la variante Mini) :
```json
"medias": [ { "role": "image_references", "id": "b5fb893b-ee5a-43de-82f3-d785f478f20e" } ]
```
ou, en repli, le placeholder Element inséré directement dans le texte du prompt :
`<<<3b929346-d7ab-4590-b5d6-a090681e6ffe>>>`. Ne jamais combiner les deux dans une même soumission.

**Modèles écartés pour la création de personnage** (ne pas réessayer sans raison) : `soul_cast`
ignore le prompt et rend un personnage de 40-45 ans avec sa propre biographie ; `nano_banana_pro`
est routé vers `nano_banana_2` et échoue sans message ; Marketing Studio est une galerie de
gabarits publicitaires partant d'une image produit, pas un créateur de personnage.
La fiche retenue vient de `seedream_v4_5`, 16:9, 1 crédit.

**Si Lucas fournit un jour ses vraies photos** (elles remplacent la fiche générée) :
1. Lucas fournit **4 à 8 photos** de lui : plan taille et plan large, de face, de trois-quarts et
   de profil, lumières différentes, **en costume**, visage net, sans lunettes de soleil, sans
   autre personne dans le cadre. Le cadrage des photos conditionne le rendu : des photos serrées
   donnent des plans serrés, donc en fournir au moins deux en pied ou à mi-corps.
2. Upload : `media_upload_widget` (surface d'upload officielle) ou `media_upload` → PUT des
   octets → `media_confirm`. Conserver les `media_id` **dans `shorts/assets/README.md`** : ils
   sont réutilisés à chaque short, ce n'est pas à refaire.
3. Génération : ajouter le bloc `medias` à la soumission figée, sans rien changer d'autre.
```json
{ "model": "seedance_2_0_mini", "prompt": "<prompt 8 blocs>",
  "aspect_ratio": "9:16", "resolution": "720p", "duration": 15,
  "bitrate_mode": "high", "genre": "drama", "generate_audio": false,
  "medias": [ { "role": "image_references", "id": "<media_id Lucas 1>" },
              { "role": "image_references", "id": "<media_id Lucas 2>" } ],
  "get_cost": true }
```
4. Dans le prompt, le personnage se désigne par sa **fonction dans le plan**, jamais par une
   description physique qui entrerait en concurrence avec la référence : « l'homme en costume
   sombre s'avance vers le mur d'écrans », pas « un homme brun de 25 ans, mâchoire carrée… ».

**Piste alternative à tester une fois** : `show_reference_elements action=create` crée un Element
réutilisable appelé par `<<<uuid>>>` directement dans le prompt. La documentation de l'outil liste
« Seedance 2.0 » parmi les modèles compatibles **sans préciser la variante Mini** : à valider sur
un short avant d'en faire la méthode par défaut. En cas de doute, `image_references` fait foi.

**Limites à connaître, et à ne pas masquer à Lucas :**
- La ressemblance est **approchante, pas identique**, et peut dériver sur 15 s. Contrôler le
  visage sur les frames (§ 10) à chaque short.
- Le personnage **ne parle pas face caméra** : la vidéo est muette et la voix est montée après.
  Un avatar qui parle relève d'un autre pipeline (lip-sync), pas de celui-ci.
- Coût inchangé : **37,5 crédits** par short. Les références n'ajoutent rien.

### Voix — `generate_audio`
```json
{ "model": "text2speech_v2", "variant": "elevenlabs",
  "voice_type": "preset", "voice_id": "95429266-c0ac-4137-a209-63b8812b0f23",
  "prompt": "<narration complète, CTA oral inclus>", "get_cost": true }
```
- **Julian = preset `95429266-c0ac-4137-a209-63b8812b0f23`** (masculin). Coût mesuré : **0,15 crédit** (ElevenLabs) / 0,3 (`seed_audio`).
- Moteur principal : **ElevenLabs** (meilleur FR, débit naturel ≈ 2,4-2,6 mots/s). Fallback : `model: "seed_audio"` + même `voice_type`/`voice_id` (débit ≈ 3,3 mots/s, param `speech_rate` disponible).
- Jamais `voice_change` (mauvaise prononciation FR).

## 2. Séquence (un short, de bout en bout)

```
A narration Julian → gate débit (speech_metrics) → B vidéo muette → C gate viralité
→ D montage voix (sandbox) → E sous-titres (sandbox) → F vérifs → G livraison + journal
```
Strictement **un short à la fois** : A→G terminé avant de relancer A pour le suivant. Un short n'est PAS un livrable tant que la voix n'est pas fusionnée ET vérifiée.

## 3. Loi anti-échecs (non négociable)
- **Jamais de batch** (`generate_video_batch` / `generate_audio_batch` interdits) : compte plafonné ≈ 8 jobs simultanés, un batch → `429` en cascade et crédits brûlés sur échec.
- Toujours `get_cost: true` d'abord, montrer le coût, **attendre le OK**, puis relancer sans `get_cost`.
- Attendre le `completed` (`jobs_wait` en boucle, `poll_after_seconds` respecté) avant tout autre job.

## 4. Étape A — Narration + gate de débit
1. `generate_audio` (JSON §1) → `job_id` → `jobs_wait` → URL audio.
2. **Gate** dans le sandbox. ⚠️ **`speech_metrics.sh` seul MENT sur ce moteur.** Higgsfield renvoie un MP3 ElevenLabs de **longueur fixe** (mesuré : 15,386 s / 246 639 octets, identique quel que soit le texte), rempli en fin de piste par un bruit de fond **au-dessus de -35 dB**. `speech_metrics` compte ce remplissage comme de la parole et annonce systématiquement ~15,4 s. La mesure qui fait foi est le **rognage par énergie** :
```bash
curl -fsSL "$VOICE_URL" -o voice.mp3
# durée de PAROLE réelle : rogne UNIQUEMENT le remplissage de fin.
# Meme filtre qu'au montage (§7) pour mesurer exactement ce qui sera monte.
ffmpeg -v error -i voice.mp3 -af "areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_duration=0.1,areverse" -y voice_tail.wav
ffprobe -v error -show_entries format=duration -of csv=p=0 voice_tail.wav   # <= 14,3 s
# débit, à titre indicatif seulement
bash $HF_WORKFLOWS/narrator/scripts/speech_metrics.sh voice.mp3 --words <N> --max-wps 2.9 --json
```
   Critères : durée de `voice_trim.wav` ≤ **14,3 s** ; débit dans la bande naturelle **2,4-2,6 mots/s**.
   - Trop long ou `RUSHED` → **réécrire le script avec moins de mots** (jamais accélérer la voix), régénérer.
   - **Toujours monter `voice_tail.wav`**, jamais le MP3 brut : sinon 2,5 s de bruit de fond audible traînent sur la fin du short.
3. **Vérifier la prononciation** par transcription Whisper (les domaines surtout). Écrire les domaines **espacés** dans le texte TTS pour une lecture correcte en français : `Phidias propfirm point com` et `Lucas propfirm point F R`. Repère mesuré : le CTA parlé complet dure **~5 s**, soit un tiers du short.

## 5. Étape B — Vidéo muette
1. `generate_video` avec `get_cost: true` → afficher le coût → OK utilisateur.
2. Relancer sans `get_cost` → `job_id` → `jobs_wait` jusqu'à `completed` → URL vidéo.
3. Rejet « copyright restrictions » = **problème de prompt**, voir §10.

## 6. Étape C — Gate viralité (avant de dépenser du temps de montage)
`virality_predictor` `{action:"create", params:{model:"virality_predictor", medias:[{role:"video", id:"<job_id vidéo>"}]}}`.
Lire *hook strength* et *retention risk*. Hook faible → revoir le premier plan / le prompt avant montage (la vidéo est à 37,5 crédits : mieux vaut régénérer qu'habiller un plan mou).

## 7. Étape D — Montage voix (sandbox)
Le sandbox est **détruit ~10 s après chaque appel** : une seule commande chaînée, en `background:true` (bail 15 min), résultats exportés dans la même commande.

Préparer d'abord l'export : `media_upload {filename:"lp_short_<slug>_montage.mp4"}` → `upload_url` + `media_id`.
```bash
set -e; mkdir -p /home/user/w && cd /home/user/w
curl -fsSL "$VIDEO_URL" -o video.mp4 && curl -fsSL "$VOICE_URL" -o voice.mp3
# voix sur vidéo : la piste audio native est ignorée, la voix est paddée à la durée vidéo
# rognage de FIN uniquement : inverser, couper le silence de tete, re-inverser.
# NE JAMAIS utiliser silenceremove stop_periods=-1 : il supprime AUSSI les pauses
# entre les phrases et la narration devient hachee.
ffmpeg -y -i voice.mp3 -af "areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_duration=0.1,areverse" voice_tail.wav
ffmpeg -y -i video.mp4 -i voice_tail.wav -filter_complex "[1:a]apad[a]" \
  -map 0:v:0 -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest \
  -movflags +faststart montage.mp4
curl -f -X PUT --upload-file montage.mp4 "$UPLOAD_URL" && echo UPLOADED
```
Puis `media_confirm {media_id, type:"video"}`. (Encart de fin + logo : §9, à insérer ici une fois les assets fournis.)

## 8. Étape E — Sous-titres brûlés (sandbox, obligatoires)
Écrire le manifest du script, un bloc par temps. ⚠️ **Le manifest contient le texte ÉCRIT, pas le texte prononcé.** Le TTS reçoit `Phidias propfirm point com` (prononciation), le sous-titre doit afficher `Phidiaspropfirm.com`. Avec le texte prononcé dans le manifest, le script **refuse de brûler** (similarité Whisper/script sous 0,750) — c'est une protection, pas un bug : corriger le manifest, jamais baisser `--minimum-similarity`.
```json
{ "blocks": [ {"vo_line": "<hook>"}, {"vo_line": "<problème>"}, {"vo_line": "<explication>"},
              {"vo_line": "<règle>"}, {"vo_line": "<CTA oral>"} ] }
```
Préparer l'export : `media_upload {filename:"lp_short_<slug>_final_subbed.mp4"}`.
```bash
set -e; cd /home/user/w   # (ou re-télécharger montage.mp4 si nouveau sandbox)
cat > script_manifest.json <<'EOF'
<manifest JSON>
EOF
bash $HF_WORKFLOWS/subtitles/scripts/fetch_fonts.sh --quiet
python3 $HF_WORKFLOWS/subtitles/scripts/audio_to_captions.py montage.mp4 \
  --srt caps.srt --language fr --script script_manifest.json --max-words 4 --max-chars 26
cat caps.srt
python3 $HF_WORKFLOWS/subtitles/scripts/subtitle_paper_burn.py \
  --in montage.mp4 --srt caps.srt --out final_subbed.mp4 --style bold --font-key tiktok
curl -f -X PUT --upload-file final_subbed.mp4 "$UPLOAD_URL" && echo UPLOADED
```
- `--script` aligne les mots affichés sur le texte écrit (Whisper ne sert qu'au timing → zéro substitution).
- **Vérifier `caps.srt` avant de valider** : toutes les phrases présentes, CTA oral inclus, aucun mot inventé.
- Style `bold` = capitales blanches, contour noir, safe zone Reels (bas 16,7 %, côtés 11 %), 2 lignes max. Police TikTok Sans téléchargée par `fetch_fonts.sh` ; fallback automatique Montserrat.
- Paramètres retenus : `--max-words 6 --max-chars 34` (avec 4/26 le texte se hache).
- **Regrouper le CTA à la main avant de brûler.** Le tokeniseur coupe les domaines au point et affiche des blocs absurdes du type « COM, DÉTAILS SUR LUCASPROPFIRM. ». Après génération du SRT, fusionner la queue en **deux blocs** en réutilisant les timings mesurés : `Code LUCAS chez Phidiaspropfirm.com` puis `détails sur lucaspropfirm.fr`.
- Code de sortie **2** = Whisper indisponible → livrer `montage.mp4` sans sous-titres **et le signaler** (ne jamais bloquer).
- Premier run : Whisper télécharge le modèle `small` (lent) → `background:true` et poller le log ; `--model base` si trop lent.

## 9. Encart de fin + logo (assets, voir `shorts/assets/README.md`)
Une fois `logo_lp.png` et `ding.wav` uploadés sur Higgsfield (URLs permanentes notées dans le README), ajouter dans la commande du §7 (720×1280) :
```bash
curl -fsSL "$LOGO_URL" -o logo.png && curl -fsSL "$DING_URL" -o ding.wav
ffmpeg -y -i video.mp4 -i voice.mp3 -i logo.png -i ding.wav -filter_complex "\
[2:v]scale=120:-1[lg];\
[0:v][lg]overlay=x=43:y=128:enable='between(t,13,15)'[v1];\
[v1]drawtext=fontfile=/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf:text='CODE LUCAS chez Phidiaspropfirm.com':fontcolor=0xC8FF00:fontsize=34:x=(w-text_w)/2:y=190:enable='between(t,14,15)',\
drawtext=fontfile=/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf:text='Discord & formation : lucaspropfirm.fr':fontcolor=white:fontsize=30:x=(w-text_w)/2:y=240:enable='between(t,14,15)'[v];\
[1:a]apad[voice];[3:a]adelay=13000|13000[ding];[voice][ding]amix=inputs=2:normalize=0[a]" \
-map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart montage.mp4
```
Positions = zones sûres 9:16 (logo haut-gauche, encart centré dans le tiers haut, sous-titres en bas). **Tester une fois sur frames, puis figer.**

## 10. Étape F — Vérifications (sandbox, avant livraison)
```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 final_subbed.mp4            # 15.0 ± 0.2
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 final_subbed.mp4   # aac
ffmpeg -i final_subbed.mp4 -af silencedetect=n=-35dB:d=1.0 -f null - 2>&1 | grep silence_start   # aucun silence ≥ 1 s avant la fin de la parole
ffmpeg -y -i final_subbed.mp4 -vf "select='eq(n,20)+eq(n,200)+eq(n,430)'" -vsync vfr f_%02d.jpg   # 3 frames
```
Uploader les 3 frames (`media_upload` image) et les afficher : **aucun texte généré, aucun chiffre, aucune interface de courtier réaliste, aucune marque ; sous-titres lisibles ; logo/encart dans les zones sûres.** QC IA optionnel : `video_analysis_create` sur le `media_id` final (3-5 min).

**Si le plan contient un personnage** (autorisé depuis le 03/09, visage compris), extraire en plus
une frame où le visage est visible et l'inspecter :
```bash
ffmpeg -y -i final_subbed.mp4 -vf "select='eq(n,110)+eq(n,320)'" -vsync vfr face_%02d.jpg
```
- Yeux, bouche, dents ou mains déformés → **relancer** avec le personnage plus loin, de profil ou
  de dos. Un visage raté est la signature « vidéo IA » la plus reconnaissable : il annule tout le
  travail d'ancrage trading.
- Lèvres qui bougent → relancer : la vidéo est muette et la voix est montée après, la
  synchronisation ne peut pas tomber juste.
- Ne jamais livrer un visage douteux en pariant sur le petit format mobile.

## 11. Étape G — Livraison + journal
- Livrable = `final_subbed.mp4` (URL Higgsfield) + `caps.srt` + narration texte + description (skill `short-description`).
- Écrire la ligne dans `shorts/production-log.md` (date, slug, concept, patron hook, job_ids, coût, statut, URL) — c'est ce qui rend applicables les règles de variété.
- Publication TikTok : `tiktok_accounts` → `tiktok_prepare_publish {connector_id, mode:"DIRECT_POST"|"UPLOAD_TO_DRAFT", media_type:"VIDEO", video_url:<URL Higgsfield>, title, description, is_aigc:true}` → choix utilisateur → `tiktok_publish`.

## 12. Gestion des échecs — STOP, ne pas boucler
- Rejet vidéo = **d'abord un problème de prompt** : relire contre les règles anti-IP (`short-description`) — terme monétaire ? marque ? interface réaliste ? chiffre ? Corriger, **montrer le prompt reformulé**, relancer **une fois**.
- Échec technique : attendre 40-60 s puis retenter une fois. `429` : pause 90 s.
- Même concept échoue 2 fois → le noter dans le journal et passer au suivant.
- Un job n'est « terminé » que `completed` ET voix vérifiée (§10).

## 13. Validation & crédits
Double validation (idée → coût via `get_cost`) avant tout crédit — règle dans `short-description`. Mandat de production donné = exécuter A→G sans re-demander à chaque étape. Ne pas lancer une vidéo si le solde restant après coût < 3 vidéos (≈ 115 crédits) sans l'avoir dit.

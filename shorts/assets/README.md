# Assets de marque — shorts lucaspropfirm

Fichiers attendus dans ce dossier (à fournir par Lucas) :

| Fichier | Spécification | Usage |
|---|---|---|
| `logo_lp.png` | Logo LP rond lime, fond transparent, ≥ 512×512 | Signature de fin, 2 dernières secondes (haut-gauche) |
| `ding.wav` | Son de validation court (< 1 s), 48 kHz | Mixé à t = 13 s |

## Mise en ligne (une seule fois)
Le sandbox Higgsfield ne lit pas ce dépôt : chaque asset doit être **uploadé une fois** sur Higgsfield, puis son URL permanente notée ici.

1. `media_upload {filename:"logo_lp.png"}` → `upload_url` + `media_id` → `curl -f -X PUT --upload-file logo_lp.png "<upload_url>"` → `media_confirm {media_id, type:"image"}`.
2. Idem pour `ding.wav` (`type:"audio"`).
3. Reporter les URLs ci-dessous. Elles alimentent `$LOGO_URL` / `$DING_URL` dans `lucaspropfirm-shorts-generation` §9.

| Asset | URL Higgsfield | Date |
|---|---|---|
| logo_lp.png | *(à compléter)* | |
| ding.wav | *(à compléter)* | |

## Zones sûres 9:16 (720×1280) — rappel
- Logo : x ≈ 43 px, y ≈ 128 px, largeur 120 px.
- Encart de fin : centré, y ≈ 190-240 px (tiers haut).
- Sous-titres : bas 16,7 % (géré par `subtitle_paper_burn.py --style bold`).
- Colonne droite ≈ 12 % : réservée aux icônes plateforme.

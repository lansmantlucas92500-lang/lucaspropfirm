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

## Références d'identité — personnage Lucas

Photos de Lucas servant de `image_references` à `seedance_2_0_mini` (voir `shorts-generation`
§ « Personnage récurrent »). À fournir : **4 à 8 photos**, plan taille et plan large, de face,
trois-quarts et profil, lumières variées, **en costume sombre**, visage net, sans lunettes de
soleil, personne d'autre dans le cadre. Au moins deux photos en pied ou à mi-corps, sinon le
modèle ne produit que des plans serrés.

Une fois uploadées (`media_upload_widget`, ou `media_upload` → PUT → `media_confirm`), inscrire
ici les `media_id` : ils sont réutilisés à chaque short et ne se régénèrent pas.

| # | Cadrage | media_id | Date |
|---|---|---|---|
| 1 | | _à remplir_ | |
| 2 | | _à remplir_ | |
| 3 | | _à remplir_ | |
| 4 | | _à remplir_ | |

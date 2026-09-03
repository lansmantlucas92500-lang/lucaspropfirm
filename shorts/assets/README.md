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

### Personnage généré (aucune photo réelle fournie)

Faute de photos de Lucas, le personnage est **inventé** : il ne ressemble pas à Lucas, il joue
Lucas. Fiche générée le 03/09, à réutiliser telle quelle comme `image_references`.

| Élément | Valeur |
|---|---|
| Statut | **VALIDÉ par Lucas le 03/09 — figé, ne pas régénérer sans son accord** |
| Fiche | `b5fb893b-ee5a-43de-82f3-d785f478f20e` (job_id, utilisable directement en `image_references`) |
| Element réutilisable | `3b929346-d7ab-4590-b5d6-a090681e6ffe` · nom `lucas-trader` · appelé par `<<<3b929346-d7ab-4590-b5d6-a090681e6ffe>>>` dans le prompt |
| Modèle | `seedream_v4_5`, 16:9, 2560×1440, 1 crédit |
| Contenu | 3 vues : plan pied de face · plan pied trois-quarts · portrait poitrine |
| Signalement | homme de 23 ans, costume bleu nuit deux pièces, chemise blanche, cravate soie bleu nuit, ceinture cuir brun, derbies noires, montre acier |
| URL | https://d8j0ntlcm91z4.cloudfront.net/user_3E8yhsJjI3mbJ5NVjpVcBCeo5JF/hf_20260903_122401_b5fb893b-ee5a-43de-82f3-d785f478f20e.png |

**Modèles écartés, et pourquoi** — ne pas les réessayer sans raison :
- `soul_cast` : **ignore le prompt**. Il a rendu un personnage de 40-45 ans avec sa propre
  biographie inventée ; le champ `prompt` revient vide dans les paramètres du job. Bon format de
  fiche, aucun contrôle.
- `nano_banana_pro` : la requête est routée vers `nano_banana_2` et le job a échoué sans message.
- **Marketing Studio** : galerie de gabarits publicitaires (UGC talking-head, packshots, posters)
  qui part d'une **image produit**. Ne crée pas de personnage réutilisable.

Si Lucas fournit un jour ses vraies photos, elles remplacent cette fiche ici même :

| # | Cadrage | media_id | Date |
|---|---|---|---|
| 1 | | _à remplir_ | |
| 2 | | _à remplir_ | |

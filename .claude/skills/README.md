# Skills du projet LucasPropfirm

## Skills maison — production des shorts

| Skill | Role |
|---|---|
| `lucaspropfirm-shorts-pipeline` | Orchestration : concept, gates, programmation Metricool, journal. |
| `lucaspropfirm-short-description` | Source de verite creative : visuel, avatar Lucas, prompt 8 blocs, script, description. |
| `lucaspropfirm-shorts-generation` | Execution : Seedance 2.0 Mini, voix Julian, gate TTS, montage et sous-titres. |

Ils passent par le **MCP Higgsfield**, deja connecte. Rien a installer.

## Les skills officiels Higgsfield n'ont pas besoin d'etre installes

Le depot `higgsfield-ai/skills` pilote la **CLI**. Installe le 19/09, puis retire le meme jour :
le MCP Higgsfield **sert deja les memes skills en natif**, cablees sur ses propres outils.

On les charge avec `get_workflow_instructions`, sans rien copier dans le repo. Le catalogue
complet s'obtient en appelant l'outil sans argument, puis
`get_workflow_instructions({ workflow: "<nom>" })` pour charger celle qu'il faut.

| Skill CLI du depot | Equivalent natif MCP |
|---|---|
| `higgsfield-brandkit` | workflow `brand-asset-creation` |
| `higgsfield-generate` | outils `generate_image` / `generate_video` / `generate_audio` / `generate_3d`, `models_explore`, `jobs_wait` ; workflows `ad-multiplier`, `ugc-*` |
| `higgsfield-product-photoshoot` | workflow `product-photoshoot` |
| `higgsfield-youtube-thumbnail` | workflow `thumbnail-generation` |
| `higgsfield-video-explainer` | workflow `faceless-video` (+ `narrator`, `subtitles`) |
| `higgsfield-soul-id` | modeles `soul_2` / `soul_v2` avec le parametre `soul_id`, outil `show_characters`, workflow `character-sheet` |
| `higgsfield-websites` | workflow `website-builder-flow` + outils `create_website` / `deploy_website` / `publish_website` |
| `higgsfield-marketplace-cards` | **aucun equivalent MCP** a ce jour |

Verifie le 19/09 : la copie CLI de `higgsfield-brandkit` et le workflow natif
`brand-asset-creation` ont la **meme liste de fichiers `references/`**. Meme skill, deux cablages.
La copie CLI ne mentionne aucun outil MCP et appelle la CLI dix fois ; la version native appelle
`sandbox_exec`, `generate_image_batch`, `models_explore`, `media_upload`, et **ses scripts sont
deja installes dans le sandbox**. La version native est celle qui est maintenue.

`_higgsfield-upstream/cli-reference/` garde les huit dossiers en **lecture seule**, hors du
chemin des skills chargeables : un agent ne peut plus les charger et tenter une commande CLI
absente, mais la documentation reste consultable pour comparer lors d'une mise a jour.

## Lequel utiliser pour un short

**Famille maison, toujours.** Elle porte l'avatar verrouille, la charte lumineuse, le budget de
34 tokens parles, le lexique visuel trading et le format de description. Les workflows Higgsfield
generiques ne connaissent aucune de ces regles.

Les workflows natifs servent a ce que la famille maison ne couvre pas :
- `brand-asset-creation` : **la piste pour produire enfin `logo_lp.png`**, qui manque depuis le
  debut et bloque l'encart de fin des shorts.
- `soul_2` + `soul_id` : un avatar entraine sur de vraies photos de Lucas, au lieu du personnage
  genere actuel qui ne lui ressemble pas. Demande des photos.
- `thumbnail-generation` : couvertures de Shorts et miniatures YouTube.
- `faceless-video` : formats longs narres, au-dela des 15 s.

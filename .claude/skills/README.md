# Skills du projet LucasPropfirm

Deux familles cohabitent ici. **Elles ne passent pas par le meme canal Higgsfield**, c'est le
point a comprendre avant d'en utiliser une.

## 1. Skills maison — production des shorts (canal MCP)

| Skill | Role |
|---|---|
| `lucaspropfirm-shorts-pipeline` | Orchestration : concept, gates, programmation Metricool, journal. |
| `lucaspropfirm-short-description` | Source de verite creative : visuel, avatar Lucas, prompt 8 blocs, script, description. |
| `lucaspropfirm-shorts-generation` | Execution : Seedance 2.0 Mini, voix Julian, gate TTS, montage et sous-titres. |

Ils appellent Higgsfield par le **MCP** (`mcp__Higgsfield__*`) deja connecte a cette session.
Rien a installer. C'est la chaine qui a produit tous les shorts publies a ce jour.

## 2. Skills officiels Higgsfield — installes le 19/09 (canal CLI)

Depot `higgsfield-ai/skills`, version 0.12.0 : `higgsfield-generate`, `higgsfield-brandkit`,
`higgsfield-soul-id`, `higgsfield-video-explainer`, `higgsfield-youtube-thumbnail`,
`higgsfield-product-photoshoot`, `higgsfield-marketplace-cards`, `higgsfield-websites`.

**Ils pilotent la CLI `higgsfield`, pas le MCP.** Sans la CLI installee et authentifiee, aucun
des huit ne fonctionne. Deux etapes, a faire par Lucas sur sa machine :

```
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
higgsfield auth login
```

Verification : `higgsfield account status` doit afficher l'email, le plan et les credits.

## Lequel utiliser pour un short

**Pour un short LucasPropfirm, c'est la famille 1, toujours.** Elle porte l'avatar verrouille,
la charte lumineuse, le budget de 34 tokens parles, le lexique visuel trading et le format de
description avec le bloc de 11 liens. `higgsfield-generate` genere une video mais ne connait
aucune de ces regles : l'utiliser pour un short produirait un plan hors charte, sans avatar et
sans CTA.

La famille 2 sert a ce que la famille 1 ne couvre pas :
- `higgsfield-youtube-thumbnail` : couvertures de Shorts et miniatures YouTube.
- `higgsfield-video-explainer` : formats longs narres, au-dela des 15 s.
- `higgsfield-brandkit` : logo et charte. **C'est la piste pour produire enfin `logo_lp.png`**,
  qui manque depuis le debut et bloque l'encart de fin des shorts.
- `higgsfield-soul-id` : entrainement d'un vrai Soul sur des photos de Lucas. Remplacerait
  l'avatar genere actuel, qui ne lui ressemble pas. Demande des photos.
- `higgsfield-websites`, `higgsfield-product-photoshoot`, `higgsfield-marketplace-cards` :
  hors perimetre des shorts.

`_higgsfield-upstream/` garde le README, l'INSTALL, le COOKBOOK et le VERSION du depot d'origine
pour retrouver la provenance et comparer lors d'une mise a jour.

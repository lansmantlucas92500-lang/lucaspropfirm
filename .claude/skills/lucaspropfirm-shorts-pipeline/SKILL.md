---
name: lucaspropfirm-shorts-pipeline
description: |-
  Orchestration d'un short trading LucasPropfirm — de l'idée au livrable publié. Lecture du journal de production, choix du concept par RECHERCHE EN LIGNE (protocole en 3 requêtes, aucun catalogue, jamais deux shorts identiques), gates (hook, coût, viralité), publication, journal, mesure. Charger pour planifier/piloter une production. Le contenu (anti-IP, prompt, script, description) → skill lucaspropfirm-short-description. La procédure d'exécution (génération, montage voix, sous-titres) → skill lucaspropfirm-shorts-generation.
---

# LucasPropfirm — orchestration des shorts 15 s

> Périmètre : **la carte du pipeline**, le **choix du concept** et le **journal**. Il ne redonne pas les règles créatives (voir `lucaspropfirm-short-description`) ni la procédure d'exécution (voir `lucaspropfirm-shorts-generation`).

## Contexte fixe
- Comptes : TikTok/IG @lucaspropfirm01, YouTube @lucasPropfirm2026.
- Univers : « marché financier vivant », faceless premium, bleu nuit + lime/or (détaillé dans `short-description`).
- Journal de production : `shorts/production-log.md` (à la racine du repo). Assets de marque : `shorts/assets/`.
- Baselines : recalculer à chaque nouvel audit — ne jamais réutiliser d'anciennes stats comme actuelles.

## Étapes (idée → livrable publié)
| # | Étape | Où | Gate |
|---|---|---|---|
| 0 | **Lire le journal** `shorts/production-log.md` : derniers concepts, dernier patron de hook, échecs IP récents | ici | — |
| 1 | **Choix du concept** par recherche en ligne (protocole ci-dessous) | ici | concept ≠ des 10 derniers ; patron hook ≠ du précédent |
| 2 | **Contenu** — hook, script (34-38 mots, CTA oral), prompt 8 blocs, description | `short-description` | checklist hook ✔ |
| 3 | **Validation utilisateur** — concept + hook + script + prompt + description, puis **coût** (`get_cost`) | ici | OK explicite ×2 |
| 4 | **Exécution** — narration → gate débit → vidéo muette → gate viralité → montage → sous-titres → vérifs | `shorts-generation` | `speech` ≤ 14,3 s ; `completed` ; frames propres |
| 5 | **Publication** — TikTok via `tiktok_prepare_publish`/`tiktok_publish` ; IG/YouTube : livrer fichier + description | `shorts-generation` §11 | description complète (CTA haut 4 lignes + CTA écrit + 10 liens) |
| 6 | **Journal + mesure** — écrire la ligne du journal ; noter la variable testée | ici | ligne écrite |

## Choix du concept — protocole de recherche (aucun catalogue, aucune rotation)
**Aucun template d'idées.** Chaque concept sort d'une recherche faite **au moment de la production** :
1. **3 requêtes minimum** (WebSearch) :
   - « *[sujet]* trading débutant » (ce que le public FR demande) ;
   - « *[sujet]* short / tiktok / reels » (formats et hooks qui tournent) ;
   - 2-3 comptes FR de la niche (prop firms, futures) — ce qu'ils ont posté récemment sur le sujet.
2. **Extraire 3 hooks performants** observés + l'angle qui les différencie (peur, surprise, erreur, chiffre).
3. **Choisir UN angle** pour UNE idée ; le reformuler dans le patron de hook imposé par l'alternance.
4. **Noter la source** (URL/compte) dans le journal. Jamais copier un hook mot pour mot.
5. Le visuel reste une métaphore abstraite (anti-IP dans `short-description`) : le terme technique est porté par la narration, jamais par l'image.

**Règle de variété** : jamais 2 posts consécutifs de la même famille de plan ni du même patron de hook ; jamais 2 vidéos identiques (le journal fait foi).

## Contrat de script (rappel — détail dans short-description)
UNE idée par vidéo ; 34-38 mots CTA oral inclus ; durée verrouillée sur la parole mesurée (jamais accélérer la voix — réécrire) ; hook à 0-1,2 s compréhensible sans le son ; CTA oral fixe en fin, CTA écrit complet sur l'encart et la description. Zéro promesse de gains ; « jusqu'à -80 % » jamais garanti ; pas de nom de firme dans les vidéos éducatives.

## Journal — `shorts/production-log.md`
Une ligne par short, écrite à l'étape 6 (et une ligne « échec » si un concept est abandonné) : date · slug · concept · patron hook (Q/CH/ER/CI) · famille de plan · source recherche · job_id voix · job_id vidéo · coût · statut · URL publiée · variable testée. **Sans journal, les règles d'alternance sont inapplicables.**

## Mesure
- Tester **UNE seule variable par post** (patron de hook, famille de plan, heure, longueur du hook) ; seuils relatifs à la médiane du compte.
- Ne jamais comparer TikTok/IG/YT entre elles, ni prendre les vues pour organiques sans ratio like/vue.
- `virality_predictor` (étape 4) donne une lecture *avant* publication ; les stats réelles *après* — noter les deux dans le journal pour calibrer.

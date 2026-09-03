# Journal de production — shorts lucaspropfirm

Une ligne par short (ou par concept abandonné). Lu à l'étape 0 du pipeline, écrit à l'étape 6.
Patrons de hook : **Q** question · **CH** chiffre choc · **ER** erreur courante · **CI** contre-intuitif — jamais deux fois le même patron d'affilée.
Familles de plan utilisées : puits + ligne rouge poursuivante · portail + sol stable · fragmentation de verre · balance de verre.
> ⚠️ Ces 4 familles sont **trop abstraites** : aucune ne se lit comme du trading. Depuis le
> LEXIQUE VISUEL TRADING (skill `short-description`), chaque plan doit contenir au moins un
> chandelier de verre (géométrie décrite), une courbe de lumière, une grille de niveaux, un mur
> d'écrans ou une salle de marchés, visible dès la première image.

| Date pub | Slug | Concept (1 idée) | Hook | Registre | Famille de plan | Source recherche | Job voix | Job vidéo | Coût | Statut | Variable testée |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-03 10h | drawdown-trailing | Le seuil d'échec monte avec les gains | CI | abstrait | puits + ligne rouge poursuivante | PropFirmsCompared, CerclePPM | 41b31435 | 3adc7729 | 37,80 | programmé | patron hook |
| 2026-09-04 10h | promo-phidias-e2l | Le prix d'apprendre sur son propre argent (PROMO) | Q | abstrait | portail + sol stable | MaPropFirm guide Phidias 2026 | cc6d5179 | 31cfbb0e | 37,80 | programmé | patron hook |
| 2026-09-05 10h | points-vs-ticks-nq | 20 points NQ = 400 $, pas 100 $ | CH | abstrait | fragmentation de verre | Nexural, TestMax (tick values) | da912b90 | e8011d6e | 37,65 | programmé | patron hook |
| 2026-09-06 10h | regle-coherence | Le meilleur jour bloque le retrait | ER | abstrait | balance de verre | Thor, Portail Propfirm | 500a1bc6 | 5a1fd7f9 | 37,65 | programmé | patron hook |

| 2026-09-07 10h | rollover-trimestriel | Le contrat change quatre fois par an | CI | scène réelle | salle des marchés + tubes lumineux | test technique interne | abdd2e9e | b118b47a | 76,50 | programmé | registre scène réelle + avatar |
Statuts : `livré` · `programmé` · `publié` · `échec-IP` (prompt rejeté 2×) · `échec-tech` · `abandonné`.

## Short test du 03/09 — ce qu'il a prouvé et ce qu'il a cassé
**Validé** : le filtre IP laisse passer une salle des marchés ; l'avatar tient son identité sur
15 s via `image_references` ; la chaîne voix + sous-titres est opérationnelle de bout en bout.
**Cassé** : le budget de 36 mots était compté sur le texte écrit alors que le TTS lit les domaines
épelés (CTA = 14 tokens, pas 7). Deux prises rejetées au gate avant de tomber à 20 tokens de
contenu. Règle réécrite en tokens parlés.
**Cassé** : un lieu nommé sans son mobilier produit autre chose. « Salle de marchés » sans bureaux
ni écrans a donné un **musée** (v1, 37,50 crédits perdus). Corrigé en v2 par la liste du mobilier.
**Persistant** : les objets flottants sans support sont réinterprétés à chaque fois (bougie de
cire, vitrine, tube suspendu). Préférer un élément intégré au décor.

## Écarts constatés sur ce lot (à corriger au prochain)
- **Short 3** : « bougie de verre » a été rendu par Seedance comme une **bougie de cire avec flamme**, pas un chandelier de trading. Le mot est ambigu en français. Décrire désormais la géométrie : « bloc de verre vertical lumineux, corps rectangulaire, fine tige au-dessus et en dessous ».
- **Débit TTS non déterministe** : entre 2,44 et 2,97 mots/s d'une prise à l'autre pour un même nombre de mots. Viser 36 mots maximum (CTA parlé compris) pour absorber une lecture lente.
- **Encart de fin non appliqué** : `logo_lp.png` et `ding.wav` manquent dans `shorts/assets/`.

## Programmation Metricool (brand LucasPropfirm, blogId 6758811)

Les 4 shorts sont programmés à 10h00 Europe/Paris, **un seul post par jour couvrant 6 réseaux**
(X, Facebook, Instagram, LinkedIn, TikTok, YouTube), texte long identique partout — X Premium
lève la limite de 280 caractères.

| Date | uuid Metricool | Réseaux | Déclarations |
|---|---|---|---|
| 03/09 10h | 5236506896588555897 | 6 | IG isAiGenerated · TikTok isAigc · YT isAiGeneratedContent |
| 04/09 10h | 7661303632687221310 | 6 | idem + TikTok `commercialContentOwnBrand` (post promo) |
| 05/09 10h | 6784933572646685926 | 6 | idem |
| 06/09 10h | 4332100868684008824 | 6 | idem |

> Les identifiants numériques (`id`) changent à chaque mise à jour Metricool ; **seuls les uuid sont stables** — c'est eux qu'il faut réutiliser.

4 anciens posts « X seul » (textes courts) ont été **passés en brouillon** pour éviter le doublon
sur X : uuid -3538718069285106599, -7947203799857544241, 1850340961992197192, 3247207329314064201.
L'API Metricool n'expose pas de suppression : ces 4 brouillons sont à supprimer à la main dans le planner.

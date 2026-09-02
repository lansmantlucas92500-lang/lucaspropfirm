# Journal de production — shorts lucaspropfirm

Une ligne par short (ou par concept abandonné). Lu à l'étape 0 du pipeline, écrit à l'étape 6.
Patrons de hook : **Q** question · **CH** chiffre choc · **ER** erreur courante · **CI** contre-intuitif — jamais deux fois le même patron d'affilée.
Familles de plan utilisées : puits + ligne rouge poursuivante · portail + sol stable · fragmentation de verre · balance de verre.

| Date pub | Slug | Concept (1 idée) | Hook | Famille de plan | Source recherche | Job voix | Job vidéo | Coût | Statut | Variable testée |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-03 10h | drawdown-trailing | Le seuil d'échec monte avec les gains | CI | puits + ligne rouge poursuivante | PropFirmsCompared, CerclePPM | 41b31435 | 3adc7729 | 37,80 | programmé | patron hook |
| 2026-09-04 10h | promo-phidias-e2l | Le prix d'apprendre sur son propre argent (PROMO) | Q | portail + sol stable | MaPropFirm guide Phidias 2026 | cc6d5179 | 31cfbb0e | 37,80 | programmé | patron hook |
| 2026-09-05 10h | points-vs-ticks-nq | 20 points NQ = 400 $, pas 100 $ | CH | fragmentation de verre | Nexural, TestMax (tick values) | da912b90 | e8011d6e | 37,65 | programmé | patron hook |
| 2026-09-06 10h | regle-coherence | Le meilleur jour bloque le retrait | ER | balance de verre | Thor, Portail Propfirm | 500a1bc6 | 5a1fd7f9 | 37,65 | programmé | patron hook |

Statuts : `livré` · `programmé` · `publié` · `échec-IP` (prompt rejeté 2×) · `échec-tech` · `abandonné`.

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

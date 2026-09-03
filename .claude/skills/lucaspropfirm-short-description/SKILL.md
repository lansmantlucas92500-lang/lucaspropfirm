---
name: lucaspropfirm-short-description
description: |
  Source de vérité CRÉATIVE des shorts lucaspropfirm (trading Futures ES/NQ, prop firms, audience FR). Charger pour tout ce qui touche au CONTENU d'un short : format technique, univers visuel, règles anti-IP des prompts, LEXIQUE VISUEL TRADING obligatoire (chandeliers, courbes, murs d'écrans, salle de marchés — le short doit se voir comme du trading), AVATAR LUCAS présent par défaut dans tous les shorts, recette de prompt vidéo (8 blocs en français, anti-générique, exemple figé), module hook, script de narration (CTA oral court + CTA écrit complet), règles ANTI-IA et ancrage trading obligatoire (mots interdits, marqueurs concrets), zones sûres 9:16, description IG/TikTok/YouTube (bloc de liens 11 lignes). Pour la procédure d'exécution (génération, montage voix, sous-titres) → skill lucaspropfirm-shorts-generation. Pour l'orchestration, la recherche de concept et le journal → skill lucaspropfirm-shorts-pipeline.
---

# Spec créative des shorts lucaspropfirm

> Périmètre : **source de vérité pour tout le contenu** (visuel, prompt, narration, description). Il ne décrit PAS l'exécution (voir `lucaspropfirm-shorts-generation`) ni l'orchestration (voir `lucaspropfirm-shorts-pipeline`).
> **Précédence** : les skills LP généralistes (`hook-generator-lp`, `reels-scripter-lp`, `legendes-ig-lp`, `createur-de-poste`) peuvent servir à **générer des candidats** (hooks, scripts, légendes). En cas de conflit, **ce skill gagne** : checklist hook, CTA, bloc de liens, anti-IP.

## CONTEXTE COMPTE
@lucaspropfirm01 — trading **Futures ES/NQ**, prop firms, audience FR débutante/intermédiaire. Objectif : vues + commentaires → Discord gratuit → conversion Phidias (code **LUCAS**) et Discord Pro/Élite.

## FORMAT TECHNIQUE (non négociable)
- Modèle : **Seedance 2.0 Mini, 720p, 9:16, 15 secondes — FIGÉ, ne jamais proposer un autre modèle ni une autre résolution.** La qualité vient du prompt (recette ci-dessous), pas du modèle.
- **Aucun texte lisible** à l'écran dans la vidéo générée
- Narration TTS voix **"Julian"** en français (moteur ElevenLabs ; jamais `voice_change`)
- La vidéo est générée **muette** (`generate_audio=false`) ; la voix est montée en post-prod (jamais en référence audio dans la génération).

## UNIVERS VISUEL — DEUX REGISTRES, UNE SEULE LUMIÈRE

Un short se tourne dans **l'un des deux registres**, jamais les deux à la fois :

**A. Scène réelle** (par défaut depuis le 03/09) — un lieu que le spectateur reconnaît, avec un
élément du LEXIQUE VISUEL TRADING intégré à la scène : salle de marchés, toit d'immeuble à
l'aube, parc au petit matin, rue mouillée la nuit, café vide, couloir vitré de bureau.
L'élément trading fait **partie du décor**, il n'est pas collé par-dessus : une courbe de lumière
qui court au-dessus des arbres du parc · une rangée de chandeliers de verre posée sur une table
de café · un mur d'écrans au fond d'une salle · une grille de niveaux projetée sur le bitume.

**B. Abstrait fintech** — l'univers d'origine : volumes de verre, plaines de chandeliers,
architectures lumineuses, sans lieu réel. À garder pour les concepts que rien ne rend
littéralement (une mécanique invisible, un seuil, une règle).

**Charte lumineuse commune aux deux registres — c'est elle qui fait la marque, pas le décor :**
- Dominante **bleu nuit profond** + accents **or / lime**. En extérieur de jour, choisir des
  heures qui donnent cette dominante naturellement : **aube, crépuscule, ciel couvert froid,
  nuit éclairée**. Jamais un plein soleil de midi, jamais une dominante verte ou chaude.
- **Éclairage cinématique** : rim light bleu froid, halos or/lime, brume volumétrique, bokeh.
  Jamais plat, jamais une lumière de caméra de téléphone.
- **Matériaux riches** nommés (verre fumé, métal brossé, chrome, béton mouillé, feuillage humide).
- **Échelle et profondeur** : couches premier plan / milieu / arrière-plan, profondeur de champ.
- **Mouvement fluide** : un seul mouvement de caméra, lent, avec une révélation.
- Rouge et vert **uniquement en signaux ponctuels**, jamais en dominante.

> **Test de la vignette** : deux shorts côte à côte, l'un dans un parc, l'autre dans une salle de
> marchés, doivent se reconnaître comme venant du même compte. Si ce n'est pas le cas, c'est la
> lumière qui a dérivé, pas le lieu.

### PERSONNAGE RÉCURRENT « LUCAS » (décision du 03/09)
Le personnage central des shorts est **Lucas, 23 ans, jeune trader en costume bleu nuit et
cravate**, allure sobre et assurée. Personnage **généré et validé le 03/09** : il ne ressemble pas
au vrai Lucas, il le joue. **Il apparaît dans TOUS les shorts par défaut** — quand Lucas demande
un short, l'avatar y est, sans qu'il ait à le préciser et sans lui poser la question. Un short
sans personnage est l'exception et relève d'une demande explicite de sa part. Références figées dans `shorts-generation` § « Personnage récurrent ». Il est le fil conducteur d'un short à l'autre, pas une
figuration : c'est lui qui traverse la salle de marchés, qui s'arrête devant le mur d'écrans, qui
marche dans le parc au petit matin pendant que la courbe de lumière court au-dessus des arbres.

**Son identité est verrouillée par référence photo**, jamais par description écrite : une
description physique produit un visage différent à chaque génération. La procédure technique
(`image_references`, `media_id` à conserver, alternative Element) est dans `shorts-generation`
§ « Personnage récurrent ». Dans le prompt, il se désigne par sa fonction dans le plan
(« l'homme en costume sombre s'avance vers le mur d'écrans »), jamais par ses traits.

**Cohérence entre shorts** : toujours le costume bleu nuit, chemise blanche, cravate soie bleu
nuit, montre acier ; même registre de posture, même façon d'occuper le cadre. C'est ce qui crée la reconnaissance, au même titre que la charte lumineuse.

### CADRAGE DES PERSONNAGES (garde-fous techniques)
Seedance 2.0 Mini en 720p rend mal les visages : les garde-fous ci-dessous ne sont pas du
confort, ce sont eux qui évitent le rendu « vidéo IA » que ces shorts cherchent justement à fuir.
Ils s'appliquent au personnage Lucas comme à toute autre présence humaine.
- **Cadrage** : plan large, plan taille ou plan américain. **Jamais de gros plan serré sur un
  visage** — c'est là que le modèle échoue le plus visiblement.
- **Le personnage ne parle pas face caméra.** La vidéo est générée muette et la voix est montée
  après : des lèvres qui bougent sans synchronisation trahissent immédiatement le montage.
  Décrire une action, un regard, une posture, jamais une parole.
- **Un seul personnage par plan** au maximum ; au-delà, des silhouettes hors focus.
- **Contre-jour, profil, trois-quarts** plutôt que face pleine lumière : le modèle s'en sort
  mieux et l'image est plus cinématographique.
- **Aucune marque visible** sur les vêtements, aucun logo, aucun écran de téléphone lisible.
- **Aucune célébrité, aucun sosie, aucune personne réelle autre que Lucas lui-même** (dont l'effigie est utilisée avec son accord, c'est son propre compte). Les figurants restent des silhouettes génériques.
- **Contrôle qualité obligatoire** (`shorts-generation`) : inspecter les frames où le visage est
  visible. Yeux, bouche ou mains déformés → relancer avec le personnage plus loin ou de dos.
  Ne jamais livrer un visage raté en pensant que ça passera sur mobile.

### Cohérence transversale
- Même palette bleu nuit + or/lime sur tous les shorts ; rouge/vert = signaux uniquement.
- Aucun texte lisible généré dans la vidéo (sous-titres ajoutés au montage).
- Signature finale (au montage) : logo LP rond lime sur les **2 dernières secondes** + son de validation.
- **Encart de fin (au montage, dernière seconde)** : « CODE LUCAS chez Phidiaspropfirm.com » et « Discord & formation : lucaspropfirm.fr ». Nom de domaine **toujours en entier**, jamais « Phidias » seul. C'est là que vit le **CTA écrit complet**.

### Zones sûres 9:16 (720×1280) — rien d'important hors de ces zones
- **Sous-titres** : bas de l'image, dans la safe zone Reels (bas 16,7 %, côtés 11 %), 2 lignes max.
- **Logo LP** : haut-gauche (≈ 6 % de marge, ≈ 10 % du haut).
- **Encart de fin** : centré dans le **tiers haut** (≈ 14-24 % du haut) — jamais en bas (UI TikTok/Reels + sous-titres).
- Colonne droite (≈ 12 %) réservée aux icônes plateforme ; **hook visuel centré**.

## RÈGLES ANTI-IP / ANTI-REFUS (obligatoires dans TOUT prompt visuel)
Higgsfield/Seedance renvoie **"Rejected due to copyright restrictions."** dès qu'un prompt évoque l'argent ou un élément réel. C'est un vrai rejet IP, pas un rate-limit.
- **AUCUNE évocation d'argent, gain, paiement, retrait, versement, profit, pièce, monnaie, récompense, salaire, capital.** Remplacer par un objet abstrait : « colis abstrait de verre », « objet qui se déplie », « escalier de lumière », « flux de particules ».
- **AUCUNE marque, firme, société, site, personne** (interdit : Phidias, LucasPropfirm, prop firm, nom d'échange, plateforme). Visuel 100 % abstrait et générique.
- **AUCUNE référence réelle précise** : pas de « Futures ES/NQ », pas de tick value chiffrée, pas d'horaires boursiers, pas de chiffres de marché. Tout est métaphorique.
- **AUCUN texte, chiffre, logo ou UI simulée** généré par le modèle (texte en post-prod uniquement).
- **MOTS DÉCLENCHEURS À BANNIR** : trader, broker, trading floor, candlestick (EN), Bloomberg, terminal, market data, exchange, portfolio, payout, payment, withdrawal, money, coin, gain, profit, price tag, reward, salaire, capital, argent. → remplacer par les formulations françaises du **LEXIQUE VISUEL TRADING** ci-dessous (« blocs verticaux de verre à corps rectangulaire et tige fine », « longue ligne de lumière qui monte par paliers », « salle sombre aux rangées de pupitres face à un mur de panneaux lumineux », « colonnes de tuiles de verre »). Le mot anglais déclenche, la description française passe.
- **✅ AUTORISÉ — tout le LEXIQUE VISUEL TRADING** (chandeliers de verre, courbes de lumière, grilles et niveaux, murs d'écrans, salle de marchés vide, carnet abstrait) décrit comme **objet physique**, jamais comme capture d'écran. C'est **l'IDENTITÉ VISUELLE DU PROJET**. Autorisé TANT QUE : aucun chiffre, aucune valeur affichée, aucune interface de courtier réaliste, aucun nom de marché. Une rangée de chandeliers de verre = autorisée ; la même rangée dans une fenêtre de logiciel chiffrée = refus.
- Tout concept financier est formulé par **métaphore abstraite** (résistance → « plafond lumineux » ; support → « un sol » ; levier → balance sans montant ; news → tempête abstraite). Les chiffres/montants sont autorisés **uniquement en narration TTS**, jamais à l'écran.

## LEXIQUE VISUEL TRADING (obligatoire — le short doit SE VOIR comme du trading)

Les règles anti-IP ci-dessus poussent naturellement vers l'abstraction pure, et c'est un piège :
un puits, un portail, une balance ne disent **rien** du trading. Un spectateur doit reconnaître
l'univers en une demi-seconde, sans le son. **Ce qui déclenche un refus IP, c'est l'argent, les
marques, les tickers réels et les interfaces de courtier réalistes — pas la forme d'un graphique.**
On peut donc montrer des chandeliers, des courbes, des murs d'écrans et une salle de marchés,
à condition de les décrire comme des **objets physiques**, jamais comme une capture d'écran.

**Règle bloquante : au moins UN élément de ce lexique dans chaque short, et il apparaît dans la
PREMIÈRE IMAGE (0-1,2 s).** Un short sans aucun de ces éléments ne part pas en production.

| Élément | Comment l'écrire (français, sûr) | Piège |
|---|---|---|
| **Chandeliers** | « blocs verticaux de verre lumineux, **corps rectangulaire large**, **fine tige verticale au-dessus et en dessous**, alignés en rangée sur une grille » | **Ne jamais écrire « bougie » seul** : le modèle rend une bougie de cire avec une flamme (erreur constatée le 05/09). Toujours décrire la géométrie. |
| **Courbe / ligne de prix** | « longue ligne de lumière continue qui monte par paliers puis retombe brutalement, tracée dans le vide, épaisseur constante » | Pas « courbe de prix », pas « cours » : décrire le tracé et son mouvement. |
| **Grille et niveaux** | « grille lumineuse fine au sol et en fond, lignes horizontales de niveau qui traversent le cadre », « un plafond lumineux horizontal », « un sol lumineux horizontal » | Pas d'axes chiffrés, pas de graduation lisible. |
| **Mur d'écrans** | « mur incurvé de panneaux lumineux empilés du sol au plafond, contenus abstraits, aucun texte, aucun chiffre » | Ne pas nommer une plateforme ni un terminal. |
| **Salle de marchés** | « grande salle sombre aux longues rangées de pupitres alignés face à un mur de panneaux lumineux, reflets sur les surfaces » — vide, ou avec une personne debout de dos et des silhouettes hors focus | En anglais « trading floor » est un mot déclencheur. En français, décrire le lieu. |
| **Carnet / flux d'ordres** | « deux colonnes verticales de tuiles de verre qui s'empilent et se vident en alternance, l'une froide l'autre chaude » | Pas de chiffres, pas de niveaux affichés. |
| **Bandeau défilant** | « long bandeau lumineux horizontal qui défile lentement, motifs abstraits, aucun texte lisible » | Pas de ticker nommé. |
| **Horloge de séance** | « grand cadran de verre sans chiffres dont un seul repère lumineux avance » | Pas d'heure affichée, pas d'horaire réel. |

**Rouge et vert** : autorisés uniquement comme signaux ponctuels (une bougie qui vire, une ligne
de perte), jamais comme palette dominante. La palette reste bleu nuit + or/lime.

**La signature visuelle unique de chaque short se construit DANS ce lexique, pas à côté.**
La variété vient de l'angle, de l'échelle et de l'événement physique (une rangée de chandeliers
vue du sol · une seule courbe traversant une salle vide · un mur d'écrans qui s'éteint rangée
par rangée), pas du remplacement du trading par une métaphore de développement personnel.

## PROMPT VIDÉO — RECETTE (8 blocs, en français, non générique)

### Langue et forme
- **Le prompt est écrit en français.** Narration en français. (Seedance est entraîné surtout en anglais/chinois : si un même prompt donne **deux** plans faibles, tester sa traduction anglaise à l'identique et noter le résultat au journal — le français reste la règle.)
- **130-200 mots**, **8 blocs dans cet ordre, une ligne par bloc**, jamais de paragraphe libre :
  `CONTEXTE DE SCÈNE → PREMIÈRE IMAGE → OPTIQUE → CAMÉRA → LUMIÈRE → PHYSIQUE → TIMING DE L'ACTION → AUDIO`
- Seedance n'a **pas de negative prompt** : les exclusions s'écrivent **dans** le CONTEXTE, positivement. Phrase type sans personnage : « Aucune personne, aucun texte, aucun chiffre, aucun symbole dans l'image. » Avec personnage : « Aucun texte, aucun chiffre, aucun logo, aucune marque dans l'image ; le personnage ne parle pas. »

### Ce que chaque bloc doit contenir
| Bloc | Attendu | À éviter |
|---|---|---|
| CONTEXTE DE SCÈNE | Le lieu, l'atmosphère, **3 matériaux nommés**, la phrase d'exclusion (personne/texte/chiffre) | Adjectifs vides (« magnifique », « futuriste » seul) |
| PREMIÈRE IMAGE (0-1,2 s) | **Le hook en image** : un objet, un cadrage, un micro-événement lisible sans le son | Un plan d'ensemble neutre |
| OPTIQUE | Focale, profondeur de champ, bokeh, flare | « cinématique » sans précision |
| CAMÉRA | **Un** mouvement précis (travelling arrière, contre-plongée, tilt, plan fixe final) et sa révélation | Plusieurs mouvements empilés |
| LUMIÈRE | Rim light bleu froid + halos or/lime, brume volumétrique, contraste | « bien éclairé », lumière plate |
| PHYSIQUE | **Un événement physique** (empilement, fissure, chute, pulsation, ondulation) avec inertie et reflets cohérents | Mouvement flottant sans cause |
| TIMING DE L'ACTION | Format imposé `0-1,2 s … / 1,2-4 s … / 4-8,5 s … / 8,5-12 s … / 12-15 s …` — **un événement visuel par temps** ; le temps **8,5-12 s porte la règle du script** par un signal fort | Une action continue sans temps |
| AUDIO | Design sonore uniquement (bourdonnement, tintements) ; **pas de musique, pas de voix** (voix en TTS après) | Musique avec paroles |

### Anti-générique (obligatoire)
- **Une signature visuelle par short**, dérivée du concept après la recherche : un objet ou un phénomène qu'on ne retrouve dans **aucun** autre short du journal (`shorts/production-log.md`, colonne « famille de plan »). Ex. une rangée de chandeliers de verre vue du sol · une courbe unique qui traverse une salle de marchés vide · un mur d'écrans qui s'éteint rangée par rangée · un plafond lumineux qui se fissure au-dessus d'une grille. **La signature doit rester lisible comme du trading** (voir LEXIQUE VISUEL TRADING) : une métaphore qui n'évoque plus le marché est rejetée, même si elle est belle.
- **Une seule métaphore** par short ; jamais deux univers mélangés.
- **Test du sujet** : si le prompt pourrait servir tel quel à un autre sujet, il est générique → réécrire.
- **Mots interdits (génériques)** : « magnifique », « futuriste » seul, « particules abstraites » seules, « ville futuriste », « hologramme » sans objet précis, « ambiance tech », « graphique » ou « données » **posés seuls sans géométrie décrite** (un graphique s'écrit avec le LEXIQUE VISUEL TRADING : forme, matière, disposition).
- **Obligatoires** : 3 matériaux nommés · 1 échelle assumée (intime ou monumentale) · 1 événement physique · 1 mouvement caméra · 1 point de lumière signature.
- Le visuel **raconte** la règle du script (temps 8,5-12 s) — ce n'est pas une décoration derrière une voix.

### Checklist avant lancement (toutes les cases)
- [ ] Français · 130-200 mots · 8 blocs · une ligne par bloc
- [ ] Scan anti-IP = 0 mot banni ; phrase d'exclusion présente dans CONTEXTE
- [ ] Hook lisible en PREMIÈRE IMAGE sans le son
- [ ] TIMING en 5 temps alignés sur le script ; règle portée à 8,5-12 s
- [ ] Une seule métaphore ; signature visuelle absente du journal
- [ ] Aucun mot de la liste « génériques »
- [ ] **Au moins un élément du LEXIQUE VISUEL TRADING, présent dès la PREMIÈRE IMAGE**
- [ ] Si le plan contient des chandeliers : **géométrie décrite** (corps rectangulaire + tige), jamais « bougie » seul
- [ ] Registre choisi (scène réelle **ou** abstrait fintech), jamais les deux
- [ ] Charte lumineuse respectée : dominante bleu nuit + or/lime, jamais plein soleil de midi
- [ ] **Personnage Lucas présent** (défaut de tous les shorts) : `image_references` jointes, costume bleu nuit, désigné par sa fonction et non par ses traits
- [ ] Cadrage du personnage : pas de gros plan visage, il ne parle pas, aucune marque visible

### Exemple de référence (style figé) — sujet « 1 tick »
```
CONTEXTE DE SCÈNE : Une plaine sombre couverte de blocs verticaux de verre lumineux, corps rectangulaire large et fine tige verticale au-dessus et en dessous, alignés en rangées serrées sur une grille lumineuse, sous un ciel bleu nuit. Atmosphère de science-fiction financière haut de gamme : verre fumé, chrome brossé, reflets HDR. Aucune personne, aucun visage, aucun texte, aucun chiffre, aucun symbole dans l'image.
PREMIÈRE IMAGE (0-1,2 s) : Très gros plan sur un seul bloc de verre doré, corps rectangulaire et tige fine, posé sur la grille ; une minuscule marche de lumière se détache de son bord et s'élève.
OPTIQUE : Rendu 35 mm anamorphique, faible profondeur de champ, bokeh doux, léger flare sur les reflets lime.
CAMÉRA : Lent travelling arrière avec une légère contre-plongée, révélant que la marche est la première d'un escalier de lumière monumental qui s'élève de la plaine de blocs de verre ; fin sur un plan large en contre-plongée, caméra fixe.
LUMIÈRE : Rim light bleu froid depuis l'horizon, halos or et lime chauds sur chaque marche, brume volumétrique, contraste cinématique, jamais plat.
PHYSIQUE : Les marches se matérialisent une à une avec une ondulation de verre ; les particules montent avec une inertie réaliste ; les reflets restent physiquement cohérents.
TIMING DE L'ACTION : 0-1,2 s bloc de verre seul + première marche / 1,2-4 s trois marches s'empilent / 4-8,5 s l'escalier grandit pendant que la caméra recule / 8,5-12 s une marche pulse plus fort, un signal d'alerte / 12-15 s l'escalier se stabilise, caméra fixe.
AUDIO : Bourdonnement ambiant profond, tintements de verre doux sur chaque marche, pas de musique, pas de voix.
```

## MODULE HOOK (obligatoire avant toute production)
Le hook est la phrase d'accroche des 0-1,2 s. Il doit être compréhensible **sans le son** (appuyé par le visuel). **Aucun short ne part en production sans hook validé.**

### Les 4 patrons (choisir UN, alterner d'un post à l'autre — vérifier dans `shorts/production-log.md`)
1. **Question (Q)** : « Tu sais lire ce que le marché dit VRAIMENT ? »
2. **Chiffre choc (CH)** : « 1 tick = 12,50 $ » (vérifié)
3. **Erreur courante (ER)** : « ES + NQ en même temps ? Tu doubles ton risque »
4. **Contre-intuitif (CI)** : « Le prix affiché n'est pas le prix que tu paies »

### Check-list de validation du hook (toutes les cases)
- [ ] **1,2 s max** à l'oral
- [ ] **Compréhensible sans le son** (le premier plan illustre le hook)
- [ ] **Un seul patron** (Q, CH, ER ou CI), **différent du post précédent** (journal)
- [ ] **Zéro promesse de gain**, **zéro stat non sourcée** (banni : « 90 % des traders… »)
- [ ] **Sans jargon** non expliqué ; **pas de marque ni de firme** dans le hook
- [ ] **Émotion ou curiosité** (crée un manque)
- [ ] Validé → production ; sinon → réécrire avec un autre patron

## SCRIPT NARRATION (15 s)
**Budget : 33-36 mots au total, CTA oral inclus** (ElevenLabs lit à ≈ 2,4-2,6 mots/s ; la durée réelle est mesurée sur la voix par le gate de `shorts-generation` — c'est elle qui fait foi, pas le compte de mots).
⚠️ **Les deux noms de domaine du CTA sont lourds à l'oral** (« Phidiaspropfirm point com » ≈ 1,6 s, « lucaspropfirm point F R » ≈ 1,5 s) : le CTA parlé occupe **~4,5 s à lui seul**. Le contenu ne dispose donc que de **26-29 mots**. Ne jamais rogner le CTA pour gagner du temps — raccourcir le contenu.

| Temps | Contenu | Mots |
|---|---|---|
| 0-1,2 s | **HOOK** (verrouillé par le module Hook) | 5-6 |
| 1,2-4 s | problème / mise en situation | 6-8 |
| 4-7,5 s | explication — **1 seule idée**, vocabulaire débutant | 7-9 |
| 7,5-10,5 s | règle à retenir | 5-7 |
| 10,5-15 s | **CTA ORAL FIXE** (7 mots, ~4,5 s, dit tel quel) | 7 |

**Ancrage** : sur les 26-29 mots de contenu, au moins **un marqueur concret** (instrument, chiffre, plateforme, moment de séance ou mécanique prop firm nommée) — voir « ANTI-IA & ANCRAGE TRADING ». Les mots interdits de cette liste valent aussi pour la narration.

**CTA ORAL FIXE (fin de narration, jamais reformulé ni omis)** :
« Code LUCAS chez Phidiaspropfirm.com, détails sur lucaspropfirm.fr. »
> Toujours dire **Phidiaspropfirm.com** en entier — jamais « Phidias » seul. Idem à l'écrit (encart de fin, descriptions).

**CTA ÉCRIT COMPLET (encart de fin + toutes les descriptions, jamais reformulé)** :
« Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com. »

> Pourquoi deux CTA : le CTA complet fait 20 mots ≈ 7-8 s de voix — impossible dans les 3 dernières secondes d'un 15 s sans couper. Il est donc **lu** (encart + description), et le CTA oral court porte le code + le site.

## DESCRIPTION (format fixe, toutes plateformes)
**CTA haut (5 lignes)** → accroche émoji → lignes "👉" → "🎓 abonne-toi" → **CTA écrit complet** → **bloc de liens complet (11 lignes)**. Dire « jusqu'à -80 % », jamais garanti.
- Le **CTA haut** est en toute première position : il reste visible avant le « … plus » des plateformes.
- **JAMAIS de tiret cadratin (—) ni de tiret demi-cadratin (–) dans une description.** C'est la signature typographique la plus reconnaissable d'un texte écrit par une IA. Utiliser un point, une virgule, un deux-points ou un point médian (·). Même règle pour les scripts de narration et les légendes.
### ANTI-IA & ANCRAGE TRADING (bloc bloquant — une description qui échoue ici se réécrit)

Deux défauts vont ensemble et se corrigent ensemble : ça **sonne IA**, et ça **ne parle pas de trading**.
Une description abstraite est toujours une description qui sonne IA, parce que l'IA écrit à vide.
La cure est la même : mettre du concret dedans.

**1. Ancrage obligatoire — au moins 2 marqueurs concrets DIFFÉRENTS par description**, dont au
moins un dans l'accroche ou la première ligne « 👉 ». Piocher dans :
- **instrument nommé** : ES · NQ · MES · MNQ · CL · GC (pas « le marché », pas « ton actif ») ;
- **chiffre vérifiable** : valeur du tick (ES 12,50 $ · NQ 5 $ · MES 1,25 $ · MNQ 0,50 $),
  taille du drawdown, seuil de profit, nombre de contrats, montant d'un stop en dollars ;
- **plateforme réelle** : Tradovate · ATAS · DeepCharts · Sierra Chart · NinjaTrader ;
- **moment de séance** : ouverture NY 15h30, cash open, RTH, overnight, jour de rollover ;
- **mécanique prop firm nommée précisément** : drawdown EOD / intraday / trailing, seuil de
  profit, jours minimums, règle de cohérence, délai de payout.

> **Test de l'ancrage** : masquer le CTA haut, le CTA écrit et le bloc de liens. S'il ne reste
> ni instrument, ni chiffre, ni plateforme, ni mécanique nommée → la description est creuse,
> on la réécrit. Une description qui pourrait servir à un compte de développement personnel
> n'est pas une description de trading.

**2. Mots et tournures interdits** (signature IA en français) :
- *Ouvertures* : « Bienvenue dans », « Découvre », « Plongeons dans », « Parlons de »,
  « Spoiler », « Et devine quoi », « Voici pourquoi ».
- *Liants de dissertation* : « en effet », « de plus », « par ailleurs », « ainsi »,
  « en conclusion », « pour résumer », « il est important de », « il est essentiel de »,
  « n'oublie pas que ».
- *Superlatifs creux* : « incontournable », « révolutionnaire », « game changer », « la clé »,
  « le secret », « ultime », « puissant », « redoutable », « imparable », « véritable ».
- *Verbes marketing* : « booster », « maîtriser », « débloquer », « libérer ton potentiel »,
  « passer au niveau supérieur », « optimiser », « maximiser ».
- *Adjectifs jetables* : « crucial », « essentiel », « fondamental », « incroyable », « énorme ».
- *Stats inventées* : « 90 % des traders », « la plupart des traders », « beaucoup de traders »
  sans source. Si le chiffre n'est pas sourçable, écrire la mécanique, pas la statistique.
- *Tournure « ce n'est pas X, c'est Y »* : interdite comme effet de style. **Autorisée
  uniquement quand les deux côtés sont des chiffres réels** (« ce n'est pas 100 $, c'est 400 $ »).

**3. Rythme non robotique.** L'IA écrit des phrases de même longueur, parfaitement parallèles.
Casser ça : les deux lignes « 👉 » ne font pas la même longueur, une phrase courte (3-5 mots)
au moins par description, tutoiement systématique, une phrase nominale ou incomplète autorisée.
Zéro symétrie décorative.

**4. La ligne « 🎓 » annonce un contenu, pas un slogan.** Elle nomme le sujet du prochain post
ou ce que le spectateur saura faire. Bannis : « Chaque jour, une règle décortiquée »,
« Les bases qui sauvent un compte », « Les règles qu'on découvre trop tard » — ce sont des
slogans interchangeables. Écrire plutôt : « 🎓 Demain : pourquoi le drawdown EOD se gère à la
clôture, pas en séance. Abonne-toi. »

**5. Même exigence pour la narration** (`SCRIPT NARRATION`) : sur les 26-29 mots de contenu,
au moins **un** marqueur concret. Un short de 15 s sans instrument, sans chiffre et sans
mécanique nommée ne se distingue d'aucun autre compte.

**Avant / après** (cas réels du lot du 03-06/09) :

| Creux (rejeté) | Ancré (accepté) |
|---|---|
| Plus tu gagnes, plus tu es proche de l'échec. | Tu passes de 50 000 à 52 000 $. Ton seuil d'échec vient de monter de 2 000 $ avec toi. |
| Ta marge d'erreur rétrécit à mesure que tu réussis. | En trailing, le seuil suit ton plus haut. À +2 000 $, la même perte qui passait hier te ferme le compte. |
| Tu es rentable, ton retrait est refusé. Bienvenue dans la règle de cohérence. | Ton retrait est refusé alors que tu es à +3 000 $ : un seul jour pèse 60 % de tes gains, la règle de cohérence plafonne souvent à 30-50 %. |
| Les bases qui sauvent un compte. Abonne-toi. | Demain : la valeur du tick sur MES et MNQ, pour dimensionner un stop en micro. Abonne-toi. |

- **TikTok uniquement** : les liens ne sont pas cliquables → ajouter « 🔗 Tout est en bio » juste au-dessus du CTA haut.
- **Lien en bio de tous les comptes (IG, TikTok, YouTube, X)** : le SmartLink Metricool **https://t.mtrbio.com/lucaspropfirm** (URL courte à utiliser partout ; redirige vers la page finale https://t-sml.mtrbio.com/public/smartlink/lucaspropfirm — 10 boutons trackés, stats par bouton dans Metricool → Analytics → SmartLinks). Page de secours sur le domaine : `liens.html` du site (https://lucaspropfirm.fr/liens.html). Quand un post est programmé via Metricool, attacher le SmartLink (`smartLinkData`) pour le tracking.

### CTA haut (5 lignes — TOUJOURS en tête de description, texte exact)
```
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidiaspropfirm.com : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
📊 Metricool (gestion de réseaux sociaux) : https://i.mtr.cool/lucas
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
```

### Bloc de liens (11 lignes — TOUJOURS COMPLET en bas, chaque lien sur SA propre ligne)
```
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidiaspropfirm.com : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
📒 Journal de trading PropLog : https://www.proplog.fr/
📰 Newsletter lucaspropfirm : https://lucaspropfirm.fr/newsletters.html
📰 Newsletter Proplog : https://proplog.fr/newsletter/
🤝 Affiliation : https://lucaspropfirm.fr/Affiliation.html
🎁 Limova code promo PROFILM30 : https://limova.ai/?linkId=lp_079563&sourceId=lucas-lansmant&tenantId=limova
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
🤖 Wisewand.ai (EN) (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/en/?fpr=lucas
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
📊 Metricool (gestion de réseaux sociaux) : https://i.mtr.cool/lucas
```
Structure : CTA haut (5 lignes) → ligne vide → accroche → contenu (1-2 lignes) → 🎓 abonne-toi → ligne vide → CTA écrit complet → ligne vide → bloc de liens (11 lignes). Ne jamais tronquer ni coller les liens sur une seule ligne. Le CTA haut et le bloc de liens se répètent volontairement (haut = visible sans dérouler ; bas = complet).

### Exemple complet — Éducation
```
🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidiaspropfirm.com : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
📊 Metricool (gestion de réseaux sociaux) : https://i.mtr.cool/lucas
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas

📉 Un tick sur ES, c'est 12,50 $. Sur NQ, 5 $.
👉 Même stop de 8 ticks : 100 $ sur ES, 40 $ sur NQ. Ce n'est pas le même trade.
👉 Regarde la valeur du tick de TON contrat avant de poser le stop, pas celle du gars qui poste son setup.
🎓 Demain : la valeur du tick sur MES et MNQ, pour dimensionner un stop en micro. Abonne-toi.

Pour avoir les détails des prop firms, rendez-vous sur lucaspropfirm.fr, pour le Discord et la formation. Code LUCAS chez Phidiaspropfirm.com.

🔑 Code 𝗟𝗨𝗖𝗔𝗦 → jusqu'à -80 % chez Phidiaspropfirm.com : https://phidiaspropfirm.com
📌 Discord & formation : https://lucaspropfirm.fr
📒 Journal de trading PropLog : https://www.proplog.fr/
📰 Newsletter lucaspropfirm : https://lucaspropfirm.fr/newsletters.html
📰 Newsletter Proplog : https://proplog.fr/newsletter/
🤝 Affiliation : https://lucaspropfirm.fr/Affiliation.html
🎁 Limova code promo PROFILM30 : https://limova.ai/?linkId=lp_079563&sourceId=lucas-lansmant&tenantId=limova
🤖 Wisewand.ai (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/?fpr=lucas
🤖 Wisewand.ai (EN) (rédacteur IA optimisé SEO) code promo LUCAS10 → -10 % : https://wisewand.ai/en/?fpr=lucas
🎬 Higgsfield (génération vidéo IA) : https://higgsfield.ai?fpr=lucas17
📊 Metricool (gestion de réseaux sociaux) : https://i.mtr.cool/lucas
```

## RÈGLE DE VALIDATION
Proposer d'abord **concept + hook + script + prompt complet + description**, attendre la **validation utilisateur**, puis **confirmer le coût (`get_cost`) AVANT toute génération**. Jamais de génération sans double validation.

## Règles
- Langue : français. Codes **LUCAS** et **PROFILM30** complets, jamais modifiés.
- La firme se nomme **Phidiaspropfirm.com** en entier partout (narration, encart, descriptions) — jamais « Phidias » seul.
- Réduction Phidiaspropfirm.com : toujours « jusqu'à -80 % » (jamais garanti, dépend du type de compte), vérifier l'offre officielle avant publication.
- Ne pas mélanger avec les liens Proplog-only (Proplog a son propre CTA : https://www.proplog.fr/ et https://proplog.fr/newsletter/).
- Interdits transversaux : Limova sur le compte trading, contenu EN sur le compte FR, 16:9, chandeliers génériques sans contexte, fausses interfaces broker, lifestyle richesse.

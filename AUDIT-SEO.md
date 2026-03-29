# Audit SEO - lucaspropfirm.fr

**Date :** 29 mars 2026
**Site audite :** https://lucaspropfirm.fr
**Methode :** Analyse du code source (repo) + crawl du site en production

---

## Resume Executif

Le site lucaspropfirm.fr est un site d'affiliation pour Phidias Propfirm. Le site en production est bien plus developpe que le fichier HTML du repo. L'audit couvre les deux aspects.

| Categorie | Score | Commentaire |
|-----------|-------|-------------|
| Meta Tags & Head | 7/10 | Production OK, repo tres incomplet |
| Contenu & Headings | 8/10 | Bonne hierarchie, contenu riche |
| Donnees Structurees | 9/10 | 7 schemas JSON-LD en production |
| Performance | 6/10 | CSS inline, chatbot bloquant |
| Images & Alt Text | 5/10 | Alt text manquant sur plusieurs images |
| Liens Internes | 8/10 | 120+ pages, bon maillage |
| Mobile | 7/10 | Responsive mais tableaux problematiques |
| Technique (robots, sitemap) | 9/10 | robots.txt + 2 sitemaps |
| Accessibilite | 5/10 | ARIA labels manquants |
| Securite | 6/10 | HTTPS OK, CSP manquant |

**Score Global : 70/100**

---

## 1. ANALYSE DES META TAGS

### Site en Production (lucaspropfirm.fr)

**Ce qui est bien :**
- Title optimise : "Prop Firm Futures France | Avis Trading & Code LUCAS -80%"
- Google Analytics (G-41RKJMVN72) en place
- Facebook Pixel (1153100996843556) en place
- Langue declaree : fr, en, es

**Ce qui manque ou est a ameliorer :**
- [ ] Meta description : non detectee explicitement dans le `<head>` - **CRITIQUE**
- [ ] Balise canonical `<link rel="canonical">` : absente ou non visible - **CRITIQUE**
- [ ] Open Graph tags (og:title, og:description, og:image, og:url, og:type) : incomplets
- [ ] Twitter Card tags : absents
- [ ] Meta robots : absent (par defaut index,follow, mais mieux de le specifier)
- [ ] Theme-color pour mobile : absent

### Fichier HTML du Repo (lucas-propfirm-site.html)

**Problemes CRITIQUES :**
- [ ] Aucune meta description
- [ ] Aucune balise canonical
- [ ] Aucun Open Graph tag
- [ ] Aucune donnee structuree (JSON-LD)
- [ ] Aucun robots meta tag
- [ ] Aucune Twitter Card
- [ ] Pas de favicon reference

---

## 2. HIERARCHIE DES TITRES (HEADINGS)

### Production
- **H1 :** "Lance-toi dans le trading Futures avec les meilleures conditions du marche" - Unique et pertinent
- **H2 :** "Pourquoi Trader Prop Firm avec Nous?", "Choisis Ton Compte Trading Phidias", "Rejoins le Discord Trading Prop Firm" - Bien structures
- Hierarchie H1 > H2 > H3 respectee

### Repo
- **H1 :** "LUCAS PROPFIRM" - Trop generique, pas de mot-cle cible
- **H2 :** 5 titres de section bien structures
- **H3 :** Sous-sections correctes
- Hierarchie respectee

**Recommandation :**
- [ ] Repo : Reformuler le H1 avec des mots-cles cibles (ex: "Prop Firm Trading Futures - Code Promo LUCAS -80%")

---

## 3. DONNEES STRUCTUREES (SCHEMA.ORG)

### Production - EXCELLENT
7 schemas JSON-LD implementes :
1. **Organization** - Lucas Propfirm, partenaire affilie Phidias
2. **WebSite** - Schema du site
3. **Product** - Code Promo Phidias -80% avec le code LUCAS
4. **Person** - Lucas, Trader Finance & Affilie
5. **FAQPage** - 7 questions frequentes
6. **ProfessionalService** - Services d'affiliation
7. **BreadcrumbList** - Navigation

### Repo - ABSENT
- [ ] Aucun schema JSON-LD - **A ajouter**

---

## 4. PERFORMANCE

### Points positifs
- Scripts analytics charges en asynchrone/differe
- Chatbot (Limova) charge avec un delai de 5 secondes
- Animations CSS (GPU-accelerated)
- IntersectionObserver pour lazy animations

### Points negatifs
- [ ] **CSS inline massif** (~620 lignes dans le `<style>`) - Externaliser dans un fichier .css pour le cache navigateur
- [ ] **JavaScript inline** (~54 lignes) - Externaliser dans un fichier .js
- [ ] **Chatbot iframe** charge du contenu externe (CLS risk)
- [ ] **Pas de preconnect/prefetch** pour les domaines tiers (Google Analytics, Facebook)
- [ ] **Pas de compression d'images** visible (SVG non optimises)

### Core Web Vitals (estimation)
| Metrique | Estimation | Statut |
|----------|-----------|--------|
| LCP (Largest Contentful Paint) | ~2-3s | Moyen |
| FID (First Input Delay) | < 100ms | Bon |
| CLS (Cumulative Layout Shift) | ~0.15-0.25 | A risque (chatbot, banniere sticky) |

**Recommandations :**
- [ ] Ajouter `<link rel="preconnect" href="https://www.googletagmanager.com">`
- [ ] Ajouter `<link rel="preconnect" href="https://connect.facebook.net">`
- [ ] Externaliser CSS et JS pour ameliorer le cache
- [ ] Ajouter `font-display: swap` pour les polices

---

## 5. IMAGES & ATTRIBUTS ALT

### Production
| Image | Alt Text | Statut |
|-------|----------|--------|
| favicon.svg (logo) | "Lucas Propfirm logo - partenaire affilie Phidias Propfirm" | OK |
| og-image.jpg | Non specifie | MANQUANT |
| cover-*.svg (blog) | Non specifie | MANQUANT |
| avis-phidias.svg | Non specifie | MANQUANT |

### Repo
- **Aucune image** dans le HTML (uniquement emojis et CSS)
- Pas de favicon reference

**Recommandations :**
- [ ] Ajouter des alt text descriptifs a toutes les images
- [ ] Ajouter des images reelles (logo, screenshots) pour enrichir le contenu
- [ ] Optimiser les SVG (compression, minification)
- [ ] Ajouter `loading="lazy"` sur les images below-the-fold

---

## 6. MAILLAGE INTERNE & LIENS

### Production - BON
- **120+ pages indexees** dans le sitemap
- Sections riches : avis prop firms, guides, strategies, fiscalite
- Liens vers Discord VIP, blog, guides
- Liens affilies vers member.phidiaspropfirm.com

### Repo - FAIBLE
- Navigation par ancres (#accueil, #avantages, #comptes, #contact)
- Un seul lien externe (lien affilie Phidias)
- Pas de lien vers d'autres pages internes
- Pas de footer avec liens utiles

**Recommandations :**
- [ ] Ajouter `rel="nofollow sponsored"` aux liens affilies
- [ ] Varier les anchor texts des liens affilies (pas toujours "DECOUVRIR")
- [ ] Ajouter un footer avec liens vers mentions legales, politique de confidentialite
- [ ] Ajouter des liens internes vers le blog et les guides

---

## 7. FICHIERS TECHNIQUES

### robots.txt - BON
- Allow: / (tout le site accessible)
- Dossiers techniques bloques (node_modules, _private, etc.)
- Crawl-delay de 10s pour AhrefsBot, SemrushBot, MJ12bot
- 2 sitemaps declares (sitemap.xml + sitemap-images.xml)
- Host: https://lucaspropfirm.fr

### Sitemap - EXCELLENT
- 120+ URLs referencies
- Priorites bien definies (1.0 pour homepage, 0.3 pour mentions legales)
- Dates de mise a jour recentes (mars 2026)
- Sitemap images separe

---

## 8. MOBILE & RESPONSIVE

### Points positifs
- Viewport meta tag present
- Media queries pour tablettes/mobile (max-width: 768px)
- Menu hamburger sur mobile
- Chatbot responsive (90% de largeur sur mobile)

### Points negatifs
- [ ] Tableaux de prix potentiellement debordants sur petit ecran
- [ ] Elements en position fixe (chatbot) pouvant masquer du contenu
- [ ] Taille de police non verifiee pour lisibilite mobile

---

## 9. ACCESSIBILITE

### Problemes identifies
- [ ] Alt text manquant sur images de blog
- [ ] Contraste : texte dore sur fond sombre a verifier (ratio WCAG)
- [ ] Champ honeypot ("Ne pas remplir") sans label clair
- [ ] Chatbot sans label ARIA
- [ ] Cards depliables sans `aria-controls`/`aria-expanded`

### Points positifs
- Skip link vers `#main-content` present
- FAQ avec markup Schema.org
- Champs de formulaire avec `required`

---

## 10. CONTENU & MOTS-CLES

### Mots-cles cibles (detectes)
- "prop firm futures france"
- "code promo phidias"
- "trader finance"
- "trading prop firm"
- "avis phidias propfirm"

### Recommandations contenu
- [ ] Ajouter une meta description optimisee (150-160 caracteres) avec mots-cles principaux
- [ ] Diversifier les ancres de liens (pas toujours le meme texte)
- [ ] Reduire la repetition du message "Code Promo LUCAS" (8+ fois sur la page)
- [ ] Ajouter du contenu E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

---

## 11. SECURITE & HTTPS

- [x] HTTPS actif
- [ ] Content Security Policy (CSP) : absent
- [ ] Headers de securite (X-Frame-Options, X-Content-Type-Options) : non verifies
- [x] Domaines tiers de confiance (Google, Facebook)

---

## PLAN D'ACTION PRIORITAIRE

### Priorite CRITIQUE (Impact SEO immediat)
1. **Ajouter une meta description** sur toutes les pages
2. **Ajouter une balise canonical** sur chaque page
3. **Completer les Open Graph tags** (og:title, og:description, og:image, og:url)
4. **Ajouter les alt text** manquants sur toutes les images

### Priorite HAUTE (Impact SEO moyen terme)
5. **Ajouter les Twitter Card tags**
6. **Externaliser CSS/JS** pour ameliorer le cache et les performances
7. **Ajouter preconnect** pour les domaines tiers
8. **Ajouter rel="nofollow sponsored"** aux liens affilies

### Priorite MOYENNE (Optimisation continue)
9. **Ameliorer l'accessibilite** (ARIA labels, contrastes)
10. **Reduire le CLS** (stabiliser le chatbot et la banniere)
11. **Optimiser les images** (compression, lazy loading)
12. **Diversifier les anchor texts** des liens

### Priorite BASSE (Nice to have)
13. **Ajouter des breadcrumbs visuels** (le schema existe deja)
14. **Implementer un service worker** pour le cache offline
15. **Ajouter hreflang** si versions multilingues prevues

---

## CORRECTIONS APPLIQUEES AU FICHIER HTML DU REPO

Les corrections suivantes ont ete identifiees pour `lucas-propfirm-site.html` :
- Ajout de meta description
- Ajout de balise canonical
- Ajout des Open Graph tags
- Ajout des Twitter Card tags
- Ajout du schema JSON-LD (Organization, Product, FAQPage)
- Ajout de meta robots
- Ajout de favicon reference
- Ajout de rel="nofollow sponsored" sur les liens affilies
- Ajout de preconnect pour domaines tiers

Voir le commit associe pour les changements appliques.

#!/usr/bin/env python3
"""Refonte des pages internes lucaspropfirm.fr dans le design dark + neon green.

Stratégie : extraction du contenu <main> (ou heuristique pour les vieilles pages),
ré-habillage complet dans le shell du nouvel index.html (head, CSS, header, footer, JS),
conservation des metas SEO/JSON-LD et des scripts interactifs propres à chaque page.
"""
import re, sys, json, pathlib, colorsys, html as htmlmod

REPO = pathlib.Path('/home/user/lucaspropfirm')
SCRATCH = pathlib.Path('/tmp/claude-0/-home-user-lucaspropfirm/b7529ed5-1ed9-5596-90c1-47ef76569d2a/scratchpad')
SCRAPE = SCRATCH / 'scrape'
DIST = SCRATCH / 'dist'

INDEX = (REPO / 'index.html').read_text(encoding='utf-8')
CONTENT_CSS = (REPO / 'tools' / 'content.css').read_text(encoding='utf-8')

# ---------- Extraction des briques du design system ----------
CSS_FULL = re.search(r'<style>(.*?)</style>', INDEX, re.S).group(1)
THEME_INIT = re.search(r'<script>try\{.*?</script>', INDEX, re.S).group(0)
SPRITE = re.search(r'<svg aria-hidden="true" style="display:none".*?</svg>', INDEX, re.S).group(0)
SKIP_LINK = '<a class="skip-link" href="#main">{label}</a>'
HEADER_FR = re.search(r'<header class="site-header".*?</header>', INDEX, re.S).group(0)
FOOTER_FR = re.search(r'<footer class="site-footer">.*?\n</footer>', INDEX, re.S).group(0)
MAIN_JS = re.search(r'</footer>\s*(<script>\s*\(function \(\).*?</script>)', INDEX, re.S).group(1)

# Le brand pointe vers #accueil sur la home ; sur les pages internes → racine de la langue
def _fix_brand(shell, home):
    return shell.replace('href="#accueil"', f'href="{home}"')

# ---------- Traductions du shell ----------
NAV_T = {
    'en': {'Blog &amp; Avis': 'Blog &amp; Reviews', 'Comparateur': 'Comparator',
           'Affiliation': 'Affiliates', 'Newsletter': 'Newsletter'},
    'es': {'Blog &amp; Avis': 'Blog y Reseñas', 'Comparateur': 'Comparador',
           'Affiliation': 'Afiliación', 'Newsletter': 'Newsletter'},
}
FOOTER_T = {
    'en': {
        '>Apprendre<': '>Learn<', '>Outils<': '>Tools<', '>Le site<': '>Site<',
        'Dossier Phidias&nbsp;2.0': 'Phidias&nbsp;2.0 file', 'Prix avec le code LUCAS': 'Prices with code LUCAS',
        'Avis Phidias': 'Phidias review', 'Comparateur prop firms': 'Prop firm comparator',
        'Voir Phidias': 'See Phidias', 'Commencer ici': 'Start here',
        'Formation Funded en 30&nbsp;Jours': 'Funded in 30&nbsp;Days course',
        'Prop firm futures en France': 'Futures prop firms in France', 'Risk management': 'Risk management',
        'Glossaire': 'Glossary', 'Fiscalité France': 'France taxation', 'Blog': 'Blog',
        'Calculateur de position': 'Position calculator', 'Calculateur prop firm': 'Prop firm calculator',
        'Récap Macro ES/NQ': 'ES/NQ Macro recap', 'Guide 5&nbsp;erreurs': '5&nbsp;mistakes guide',
        'Tous les outils gratuits': 'All free tools', 'À propos': 'About',
        'Affiliations &amp; partenaires': 'Affiliates &amp; partners', 'Politique éditoriale': 'Editorial policy',
        'Mentions légales': 'Legal notice', 'Confidentialité': 'Privacy', 'CGU': 'Terms', 'Plan du site': 'Sitemap',
        'Aller au contenu': 'Skip to content',
    },
    'es': {
        '>Apprendre<': '>Aprender<', '>Outils<': '>Herramientas<', '>Le site<': '>El sitio<',
        'Dossier Phidias&nbsp;2.0': 'Dossier Phidias&nbsp;2.0', 'Prix avec le code LUCAS': 'Precios con el código LUCAS',
        'Avis Phidias': 'Reseña Phidias', 'Comparateur prop firms': 'Comparador de prop firms',
        'Voir Phidias': 'Ver Phidias', 'Commencer ici': 'Empieza aquí',
        'Formation Funded en 30&nbsp;Jours': 'Curso Funded en 30&nbsp;Días',
        'Prop firm futures en France': 'Prop firms de futuros en Francia', 'Risk management': 'Gestión de riesgo',
        'Glossaire': 'Glosario', 'Fiscalité France': 'Fiscalidad Francia', 'Blog': 'Blog',
        'Calculateur de position': 'Calculadora de posición', 'Calculateur prop firm': 'Calculadora prop firm',
        'Récap Macro ES/NQ': 'Resumen Macro ES/NQ', 'Guide 5&nbsp;erreurs': 'Guía 5&nbsp;errores',
        'Tous les outils gratuits': 'Todas las herramientas gratis', 'À propos': 'Sobre mí',
        'Affiliations &amp; partenaires': 'Afiliaciones y socios', 'Politique éditoriale': 'Política editorial',
        'Mentions légales': 'Aviso legal', 'Confidentialité': 'Privacidad', 'CGU': 'Términos', 'Plan du site': 'Mapa del sitio',
        'Aller au contenu': 'Ir al contenido',
    },
}
FOOTER_LEGAL_T = {
    'en': "Futures trading involves a risk of capital loss. Content on this site is general and educational; it is not personalised financial advice. No gain, payout, LIVE transition or evaluation pass is guaranteed. Some links are affiliated (Phidias, Whop): LucasPropfirm may earn a commission at no extra cost to you. Displayed prices and discounts are dated (July 2026); each platform's official checkout prevails.",
    'es': "El trading de futuros implica riesgo de pérdida de capital. El contenido de este sitio es general y educativo; no constituye asesoramiento financiero personalizado. No se garantiza ninguna ganancia, payout, paso a LIVE ni aprobación de evaluación. Algunos enlaces son de afiliados (Phidias, Whop): LucasPropfirm puede percibir una comisión sin coste extra para ti. Los precios y descuentos mostrados están fechados (julio 2026); prevalece el checkout oficial de cada plataforma.",
}

def build_shell(lang):
    home = {'fr': '/', 'en': '/en/', 'es': '/es/'}[lang]
    header, footer = HEADER_FR, FOOTER_FR
    if lang != 'fr':
        # préfixer les liens internes
        def prefix(m):
            return f'href="/{lang}{m.group(1)}"'
        header = re.sub(r'href="(/[a-zA-Z0-9-]+\.html)"', prefix, header)
        footer = re.sub(r'href="(/[a-zA-Z0-9-]+\.html)"', prefix, footer)
        for k, v in NAV_T[lang].items():
            header = header.replace(f'>{k}<', f'>{v}<')
        for k, v in FOOTER_T[lang].items():
            footer = footer.replace(k, v)
        # paragraphe légal traduit (sans la phrase Limova, absente des pages internes)
        footer = re.sub(r'<p>Le trading de futures.*?</p>', '<p>' + FOOTER_LEGAL_T[lang] + '</p>', footer, flags=re.S)
    else:
        footer = footer.replace(' Un assistant conversationnel tiers (Limova) peut être chargé sur cette page.', '')
    header = _fix_brand(header, home)
    footer = _fix_brand(footer, home)
    # le sélecteur de langue est réinjecté par page → placeholder
    header = re.sub(
        r'<li class="lang-switch lang-switch--mobile"[^>]*>.*?</li>',
        '<li class="lang-switch lang-switch--mobile" aria-label="Choix de la langue">{LANGSWITCH}</li>',
        header, flags=re.S)
    header = re.sub(
        r'<div class="lang-switch"[^>]*>.*?</div>',
        '<div class="lang-switch" aria-label="Choix de la langue">{LANGSWITCH}</div>',
        header, flags=re.S)
    return header, footer

SHELLS = {lang: build_shell(lang) for lang in ('fr', 'en', 'es')}
SKIP_LABELS = {'fr': 'Aller au contenu', 'en': 'Skip to content', 'es': 'Ir al contenido'}

# ---------- Metas à reprendre depuis la page d'origine ----------
META_KEEP_NAMES = {'description', 'robots', 'author', 'keywords', 'twitter:card', 'twitter:title',
                   'twitter:description', 'twitter:image', 'twitter:site', 'twitter:creator'}
META_KEEP_PROPS_PREFIX = ('og:', 'article:')

def extract_head_bits(html):
    head_m = re.search(r'<head.*?</head>', html, re.S)
    head = head_m.group(0) if head_m else html[:6000]
    bits = {'title': '', 'metas': [], 'links': [], 'ldjson': [], 'plausible': ''}
    tm = re.search(r'<title>(.*?)</title>', head, re.S)
    bits['title'] = tm.group(1).strip() if tm else 'LucasPropfirm'
    for m in re.finditer(r'<meta\s[^>]*>', head):
        tag = m.group(0)
        name = re.search(r'name="([^"]+)"', tag)
        prop = re.search(r'property="([^"]+)"', tag)
        if name and name.group(1).lower() in META_KEEP_NAMES:
            bits['metas'].append(tag)
        elif prop and prop.group(1).lower().startswith(META_KEEP_PROPS_PREFIX):
            bits['metas'].append(tag)
    for m in re.finditer(r'<link\s[^>]*>', head):
        tag = m.group(0)
        if 'rel="canonical"' in tag or 'rel="alternate"' in tag or "rel='canonical'" in tag:
            bits['links'].append(tag)
    # JSON-LD : dans tout le document (head + body)
    for m in re.finditer(r'<script type="application/ld\+json">.*?</script>', html, re.S):
        bits['ldjson'].append(m.group(0))
    pm = re.search(r'<script[^>]*src="https://plausible\.io[^"]*"[^>]*>\s*</script>', head)
    if pm:
        bits['plausible'] = pm.group(0)
    return bits

# ---------- Nettoyage du contenu ----------
def remove_balanced(text, start_regex, tagname='div'):
    """Retire les blocs <tag ...>...</tag> (imbrication suivie) dont l'ouverture matche start_regex."""
    while True:
        m = re.search(start_regex, text)
        if not m:
            return text
        depth = 0
        removed = False
        for tm in re.finditer(r'<' + tagname + r'\b|</' + tagname + '>', text[m.start():]):
            depth += -1 if tm.group(0).startswith('</') else 1
            if depth == 0:
                text = text[:m.start()] + text[m.start() + tm.end():]
                removed = True
                break
        if not removed:
            return text

COOKIE_JS = re.compile(r'cookieBanner|cookieConsent|cookieAccept|cookieReject|cookie_consent', re.I)
SHELL_JS = re.compile(r'lp-rotbar|lp_rotbar|stickyCode|sticky-code|scrollProgress|scroll-progress'
                      r'|backToTop|back-to-top|read-progress|readProgress|promoPop|promo-pop', re.I)

def clean_content(content):
    # bannières cookies héritées (markup + scripts + liens externes obsolètes)
    content = remove_balanced(content, r'<div[^>]*(?:cookie-banner|cookieBanner|CookieConsent)[^>]*>')
    # widgets du vieux shell restés dans le contenu (code sticky, barres de progression, back-to-top, popups promo)
    content = remove_balanced(content, r'<div[^>]*(?:sticky-code|stickyCode|scroll-progress|scrollProgress|read-progress|back-to-top|backToTop|promo-pop|promoPop)[^>]*>')
    content = re.sub(r'<(?:button|a)[^>]*(?:back-to-top|backToTop)[^>]*>.*?</(?:button|a)>', '', content, flags=re.S)
    content = re.sub(r'<script[^>]*src="[^"]*(?:script\.min\.js|cookies-handler)[^"]*"[^>]*>\s*</script>', '', content)
    # barre promo rotative de l'ancien shell (style + script auto-injecté)
    content = re.sub(r'<style id="lp-rotbar-css">.*?</style>', '', content, flags=re.S)
    def drop_cookie_script(m):
        return '' if (COOKIE_JS.search(m.group(0)) or SHELL_JS.search(m.group(0))) else m.group(0)
    content = re.sub(r'<script(?![^>]*ld\+json)[^>]*>.*?</script>', drop_cookie_script, content, flags=re.S)
    # tables sans conteneur scrollable → enveloppées (anti-débordement mobile)
    out, pos = [], 0
    for m in re.finditer(r'<table\b.*?</table>', content, re.S):
        before = content[max(0, m.start() - 220):m.start()]
        out.append(content[pos:m.start()])
        if re.search(r'table-wrap|table-scroll', before):
            out.append(m.group(0))
        else:
            out.append('<div class="table-wrap">' + m.group(0) + '</div>')
        pos = m.end()
    out.append(content[pos:])
    return ''.join(out)

# ---------- Extraction du contenu ----------
def extract_content(html, path):
    m = re.search(r'<main\b[^>]*>(.*)</main>', html, re.S)
    if m:
        inner = m.group(1)
        if '<h1' not in inner:
            # le hero (avec le h1) est parfois placé avant <main> : on le rapatrie
            bm = re.search(r'<body[^>]*>', html)
            body_start = bm.end() if bm else 0
            pre = html[body_start:m.start()]
            shell = re.search(r'<(?:header|nav)\b[^>]*>.*?</(?:header|nav)>', pre, re.S)
            hero = pre[shell.end():] if shell else pre
            hero = re.sub(r'<style\b.*?</style>', '', hero, flags=re.S)
            hero = re.sub(r'<script\b.*?</script>', '', hero, flags=re.S)
            if '<h1' in hero:
                inner = hero.strip() + '\n' + inner
        return inner, 'main'
    # heuristique vieilles pages : body moins le bloc shell de tête et le footer final
    bm = re.search(r'<body[^>]*>(.*)</body>', html, re.S)
    if not bm:
        return None, 'no-body'
    body = bm.group(1)
    # retirer le premier bloc nav/header proche du début (shell)
    LEAD = 12000
    lead = body[:LEAD]
    nav_m = re.search(r'<nav\b[^>]*>.*?</nav>', lead, re.S)
    hdr_m = re.search(r'<header\b[^>]*>.*?</header>', lead, re.S)
    first = None
    if nav_m and (not hdr_m or nav_m.start() <= hdr_m.start()):
        first = nav_m
    elif hdr_m:
        first = hdr_m
    if first:
        # retrouver le bloc complet dans body (lead peut le tronquer)
        tag = 'nav' if first is nav_m else 'header'
        full = re.search(r'<' + tag + r'\b[^>]*>.*?</' + tag + '>', body, re.S)
        if full and full.start() < LEAD:
            body = body[:full.start()] + body[full.end():]
    # retirer le dernier footer
    footers = list(re.finditer(r'<footer\b[^>]*>.*?</footer>', body, re.S))
    if footers:
        last = footers[-1]
        body = body[:last.start()] + body[last.end():]
    # retirer les <style>/<link rel=stylesheet> égarés dans le body et les scripts
    # (les scripts après contenu sont gérés séparément sur la page d'origine complète)
    body = re.sub(r'<style\b.*?</style>', '', body, flags=re.S)
    return body, 'heuristic'

# ---------- Scripts de page à conserver ----------
DROP_SRC_HINTS = ('script.min.js', 'cookies-handler', 'chatbot-loader')

def page_scripts(html, content):
    """Scripts hors <main> à conserver : leurs références DOM doivent résoudre dans le contenu."""
    kept, dropped = [], []
    # zone : tout le body sauf le contenu déjà extrait
    bm = re.search(r'<body[^>]*>(.*)</body>', html, re.S)
    if not bm:
        return kept, dropped, False
    body = bm.group(1)
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', body, re.S):
        attrs, code = m.group(1), m.group(2)
        if 'ld+json' in attrs:
            continue
        if m.group(0) in content:
            continue  # déjà dans le contenu extrait
        src = re.search(r'src="([^"]+)"', attrs)
        if src:
            if 'plausible.io' in src.group(1):
                continue  # déjà repris en head
            dropped.append('EXT:' + src.group(1)[:60])
            continue
        if COOKIE_JS.search(code) or SHELL_JS.search(code):
            dropped.append('INL:shell/cookie')
            continue
        refs = set(re.findall(r'getElementById\(["\']([\w-]+)', code))
        refs |= set(re.findall(r'querySelector(?:All)?\(["\']\s*[.#]?([\w-]+)', code))
        refs |= set(re.findall(r'getElementsByClassName\(["\']([\w-]+)', code))
        if refs and any(r in content for r in refs):
            kept.append(m.group(0))
        else:
            dropped.append('INL:' + ','.join(sorted(refs))[:60])
    has_faq_btn = 'class="faq-question"' in content or "class='faq-question'" in content
    faq_handled = any('faq' in k for k in kept)
    return kept, dropped, (has_faq_btn and not faq_handled)

FAQ_FALLBACK_JS = """<script>
(function(){'use strict';
document.querySelectorAll('.faq-question').forEach(function(q){
  var item=q.closest('.faq-item')||q.parentElement;
  var a=item&&item.querySelector('.faq-answer');
  if(!a)return;
  q.setAttribute('aria-expanded','false');a.hidden=true;
  q.addEventListener('click',function(){
    var open=q.getAttribute('aria-expanded')==='true';
    q.setAttribute('aria-expanded',open?'false':'true');a.hidden=open;
  });
});})();
</script>"""

# ---------- Transformation colorimétrique universelle (clair → dark + neon) ----------
NAMED_COLORS = {'white': (255, 255, 255, None), 'black': (0, 0, 0, None)}

def _parse_color(tok):
    tok = tok.strip()
    m = re.fullmatch(r'#([0-9a-fA-F]{3})([0-9a-fA-F])?', tok)
    if m:
        h = m.group(1)
        a = int(m.group(2)*2, 16) / 255 if m.group(2) else None
        return int(h[0]*2, 16), int(h[1]*2, 16), int(h[2]*2, 16), a
    m = re.fullmatch(r'#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?', tok)
    if m:
        h = m.group(1)
        a = int(m.group(2), 16) / 255 if m.group(2) else None
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a
    m = re.fullmatch(r'rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)\s*(?:[,/]\s*([\d.]+%?)\s*)?\)', tok)
    if m:
        a = m.group(4)
        if a:
            a = float(a[:-1]) / 100 if a.endswith('%') else float(a)
        return int(m.group(1)), int(m.group(2)), int(m.group(3)), a
    m = re.fullmatch(r'hsla?\(\s*([\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%\s*(?:[,/]\s*([\d.]+%?)\s*)?\)', tok)
    if m:
        r, g, b = colorsys.hls_to_rgb(float(m.group(1)) / 360, float(m.group(3)) / 100, float(m.group(2)) / 100)
        a = m.group(4)
        if a:
            a = float(a[:-1]) / 100 if a.endswith('%') else float(a)
        return round(r * 255), round(g * 255), round(b * 255), a
    if tok.lower() in NAMED_COLORS:
        return NAMED_COLORS[tok.lower()]
    return None

def _from_hls(h, l, s, a):
    r, g, b = colorsys.hls_to_rgb(h, max(0, min(1, l)), max(0, min(1, s)))
    r, g, b = round(r*255), round(g*255), round(b*255)
    if a is not None and a < 0.999:
        return f'rgba({r},{g},{b},{round(a, 3)})'
    return f'#{r:02x}{g:02x}{b:02x}'

FG_PROPS = {'color', '-webkit-text-fill-color', 'caret-color', 'fill', 'stroke',
            'text-decoration-color', 'text-emphasis-color', 'column-rule-color'}

def transform_color(tok, prop=''):
    """Convertit une couleur du thème clair terracotta vers le thème dark + neon green.
    Consciente du rôle : un texte clair reste clair, un fond clair devient sombre."""
    parsed = _parse_color(tok)
    if not parsed:
        return tok
    r, g, b, a = parsed
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    deg = h * 360
    is_fg = prop in FG_PROPS
    is_bg = 'background' in prop or prop == 'background-image'
    if 'shadow' in prop:
        return tok if l < 0.5 else _from_hls(h, 0.0, 0.0, a if a is not None else 0.35)
    if s < 0.13:  # neutres
        if a is not None and a < 0.95:  # voiles translucides
            if is_fg:
                # texte translucide : toujours clair et assez opaque pour rester lisible
                return _from_hls(h, max(l, 0.85) if l > 0.5 else max(0.80, 1 - l), s, max(a, 0.75))
            return _from_hls(h, 1 - l, s, a)
        if is_fg:
            # texte : clair reste clair, sombre devient clair
            return _from_hls(h, max(l, 0.88), 0, a) if l > 0.65 else _from_hls(h, max(0.78, 1 - l), s, a)
        if is_bg:
            if l > 0.65:
                return _from_hls(0.42, max(0.04, min(0.10, 1 - l + 0.04)), 0.10, a)
            if l > 0.35:
                return _from_hls(h, 0.13, s, a)  # gris moyens : jamais de fond intermédiaire
            return tok  # fonds déjà sombres conservés
        # bordures / divers : inversion
        if l > 0.8:
            return _from_hls(h, max(0.10, min(0.18, 1 - l + 0.10)), s, a)
        return _from_hls(h, 1 - l, s, a) if l < 0.35 else tok
    if 5 <= deg <= 55:  # terracotta / gold / orange → vert neon
        H = 145 / 360
        if is_bg:
            if l > 0.6:
                return _from_hls(H, 0.13, 0.35, a)   # fonds teintés clairs → panneau vert sombre
            return _from_hls(H, 0.14, 0.48, a)       # panneaux/boutons pleins → panneau sombre
        if is_fg:
            return _from_hls(144 / 360, 0.62, 0.82, a) if l < 0.75 else _from_hls(H, 0.76, 0.90, a)
        # bordures et divers
        if l > 0.6:
            return _from_hls(H, 0.30, 0.45, a)
        return _from_hls(144 / 360, 0.58, 0.80, a) if l >= 0.35 else _from_hls(H, 0.37, 0.75, a)
    if deg < 5 or deg > 340:  # rouges (danger)
        if is_bg:
            return _from_hls(h, 0.15, 0.45, a) if l > 0.25 else tok
        return _from_hls(h, 0.72, min(s, 0.9), a) if l < 0.6 else tok
    if 180 <= deg <= 300:  # bleus / violets
        if is_bg:
            return _from_hls(h, 0.14, min(s, 0.5), a) if l > 0.25 else tok
        return _from_hls(h, 0.72, s, a) if l < 0.5 else tok
    # verts / jaunes déjà en place
    if is_bg:
        return _from_hls(h, 0.14, min(s, 0.5), a) if l >= 0.25 else tok
    return _from_hls(h, 0.62, s, a) if l < 0.6 else tok

COLOR_TOKEN = re.compile(r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)|\b(?:white|black)\b')

def classify_var_usages(css):
    """Rôle réel de chaque variable CSS d'après ses usages : {'--x': {'fg','bg',...}}."""
    usage = {}
    for m in re.finditer(r'([a-zA-Z-][\w-]*)\s*:\s*([^;}]+)', css):
        prop, value = m.group(1).lower(), m.group(2)
        if 'var(' not in value:
            continue
        if prop in FG_PROPS:
            role = 'fg'
        elif 'background' in prop:
            role = 'bg'
        elif 'border' in prop or 'outline' in prop or 'shadow' in prop:
            role = 'border'
        else:
            role = 'other'
        for var in re.findall(r'var\(\s*(--[\w-]+)', value):
            usage.setdefault(var, set()).add(role)
    # propagation à travers les indirections (--gradient: linear-gradient(var(--green)) …)
    defs = dict(re.findall(r'(--[\w-]+)\s*:\s*([^;}]+)', css))
    for _ in range(3):
        changed = False
        for var, roles in list(usage.items()):
            val = defs.get(var)
            if not val:
                continue
            for ref in re.findall(r'var\(\s*(--[\w-]+)', val):
                cur = usage.setdefault(ref, set())
                add = roles - cur
                if add:
                    cur |= add
                    changed = True
        if not changed:
            break
    return usage

def resolve_prop_role(prop, var_roles=None):
    """Rôle effectif d'une propriété ; les variables CSS sont classées par nom puis par usage réel."""
    p = prop.lower()
    if p.startswith('--'):
        if re.search(r'ink|text|fg|foreground|title|heading|label', p):
            return 'color'
        if re.search(r'paper|bg|background|surface|card|panel|fill', p):
            return 'background'
        if re.search(r'shadow', p):
            return 'box-shadow'
        roles = (var_roles or {}).get(prop, set())
        if 'bg' in roles:
            return 'background'   # les doubles usages reçoivent une jumelle __fg
        if 'fg' in roles:
            return 'color'
        return p  # bordures/accents : règles par défaut
    return p

_FG_PROPS_ALT = '|'.join(re.escape(p) for p in sorted(FG_PROPS))

def transform_css_colors(css):
    """Transforme toutes les couleurs d'un bloc CSS, déclaration par déclaration.
    Les variables utilisées à la fois en texte et en fond reçoivent une jumelle --x__fg."""
    var_roles = classify_var_usages(css)
    # double usage réel (texte ET fond) : prime sur la classification par nom (--ink en fond de bouton…)
    dual = {v for v, roles in var_roles.items() if 'fg' in roles and 'bg' in roles}

    def decl(m):
        raw_prop = m.group(2)
        prop = 'background' if raw_prop in dual else resolve_prop_role(raw_prop, var_roles)
        val = m.group(3)
        newval = COLOR_TOKEN.sub(lambda cm: transform_color(cm.group(0), prop), val)
        out = m.group(1) + raw_prop + ':' + newval
        if raw_prop in dual:
            fgval = COLOR_TOKEN.sub(lambda cm: transform_color(cm.group(0), 'color'), m.group(3))
            out += ';' + raw_prop + '__fg:' + fgval
        return out
    css = re.sub(r'([{;]\s*)(-{0,2}[a-zA-Z][\w-]*)\s*:\s*([^;}]+)', decl, css)
    # rediriger les usages texte des variables doubles vers leur jumelle
    for var in dual:
        css = re.sub(
            r'((?:[{;]\s*)(?:' + _FG_PROPS_ALT + r')\s*:[^;}]*?var\(\s*)' + re.escape(var) + r'(\s*[,)])',
            lambda mm: mm.group(1) + var + '__fg' + mm.group(2), css)
    return css

# ---------- Élagage des règles CSS du vieux shell ----------
SHELL_SEL = re.compile(
    r'\.(?:site-header|header-inner|header-actions|desktop-nav|language-nav|mobile-nav|mobile-nav-panel'
    r'|site-footer|footer-links|footer-grid|footer-brand|footer-bottom|footer-navigation|footer-inner'
    r'|brand|brand-mark|brand-copy|skip-link|cookie-banner|nav-toggle|main-nav|lang-switch|theme-toggle'
    r'|rm-header|rm-footer|menu-toggle|menu-btn|page-loader|sticky-code|scroll-progress|back-to-top|read-progress)\b'
    r'|#(?:lp-rotbar|cookieBanner|pageLoader|read-progress|mobile-menu|menuToggle|stickyCode|scrollProgress|backToTop)\b'
    r'|^\s*\.nav\b|,\s*\.nav\b|body\.menu-open')

def _iter_css_rules(css):
    """Itère (selecteur, corps, brut) sur les règles top-level ; les blocs @ sont retournés entiers."""
    i, n = 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j == -1:
            yield None, None, css[i:]
            return
        sel = css[i:j]
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        yield sel, css[j+1:k-1], css[i:k]
        i = k

def prune_shell_rules(css):
    out = []
    for sel, body, raw in _iter_css_rules(css):
        if sel is None:
            out.append(raw)
        elif sel.strip().startswith('@'):
            at = sel.strip().lower()
            if at.startswith('@media') or at.startswith('@supports'):
                out.append(sel + '{' + prune_shell_rules(body) + '}')
            else:  # @font-face, @keyframes… gardés tels quels
                out.append(raw)
        else:
            selectors = [s for s in sel.split(',') if s.strip()]
            kept_sel = [s for s in selectors if not SHELL_SEL.search(s)]
            if kept_sel:
                body2 = body
                # anti-espace fantôme : les paddings compensant l'ancien header fixe
                if any(re.fullmatch(r'\s*(body|html)\s*', s) for s in kept_sel):
                    body2 = re.sub(r'(?:padding|margin)-top\s*:[^;}]+;?', '', body2)
                out.append(','.join(kept_sel) + '{' + body2 + '}')
    return ''.join(out)

CSS_CACHE_DIR = SCRATCH / 'csscache'
CSS_URL_MAP = json.loads((CSS_CACHE_DIR / 'mapping.json').read_text()) if (CSS_CACHE_DIR / 'mapping.json').exists() else {}
_transformed_ext = {}

def _external_css(key):
    """CSS externe élagué + transformé, mis en cache par fichier."""
    if key not in _transformed_ext:
        raw = (CSS_CACHE_DIR / f'{key}.css').read_text(encoding='utf-8', errors='replace')
        _transformed_ext[key] = transform_css_colors(prune_shell_rules(raw))
    return _transformed_ext[key]

def collect_page_css(html, rel_full):
    """CSS d'origine de la page (liens externes + <style> inline), élagué du shell et passé au thème sombre."""
    import urllib.parse
    page_url = 'https://lucaspropfirm.fr/' + rel_full
    parts = []
    for m in re.finditer(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"|<link[^>]*href="([^"]+)"[^>]*rel="stylesheet"', html):
        href = m.group(1) or m.group(2)
        if href.startswith('http') and 'lucaspropfirm.fr' not in href:
            continue  # fontes Google externes : exclues (design sans requêtes tierces)
        key = CSS_URL_MAP.get(urllib.parse.urljoin(page_url, href))
        if key:
            parts.append(_external_css(key))
    inline = []
    for m in re.finditer(r'<style\b([^>]*)>(.*?)</style>', html, re.S):
        if 'lp-rotbar' in m.group(1):
            continue
        inline.append(m.group(2))
    if inline:
        parts.append(transform_css_colors(prune_shell_rules('\n'.join(inline))))
    return neutralize_entrance_anims('\n'.join(parts))

FONT_OVERLAY = ('main h1,main h2,main h3,main h4{font-family:var(--font-display);color:var(--text-1)}'
                'html,body{background:var(--bg-0)}'
                # animations d'entrée orphelines (leur JS d'origine a été retiré)
                'main .fade-in,main .fade-in-up,main .fade-up,main .fade-left,main .fade-right,'
                'main .reveal,main .rv,main [data-animate],main [data-aos],main .animate-on-scroll'
                '{opacity:1!important;transform:none!important}'
                # fil d'ariane : jamais étalé sur toute la largeur
                'main .breadcrumb,main .breadcrumbs{display:flex;flex-wrap:wrap;gap:7px;'
                'justify-content:flex-start;max-width:1180px;margin:14px auto;padding:0 24px}'
                # le shell garde ses couleurs même si le CSS de page redéfinit .btn/.badge
                '.site-header .btn--primary{background:var(--accent)!important;color:var(--accent-ink)!important}'
                '.site-header a,.site-footer a{text-decoration:none}')

def neutralize_entrance_anims(css):
    """Supprime les opacity:0 des règles d'animation d'entrée (fade/reveal/slide) devenues orphelines."""
    def fix(m):
        sel, body = m.group(1), m.group(2)
        if re.search(r'fade|reveal|animate|aos|slide-|-enter', sel, re.I) and 'opacity' in body:
            body = re.sub(r'opacity\s*:\s*0[^;}]*;?', 'opacity:1;', body)
            body = re.sub(r'transform\s*:\s*translate[^;}]*;?', '', body)
        return sel + '{' + body + '}'
    return re.sub(r'([^{}]+)\{([^{}]*)\}', fix, css)

# ---------- Correctif couleurs dans les styles inline du contenu ----------
def patch_inline_colors(content):
    def patch_style(m):
        style = m.group(1)
        def decl(dm):
            prop, val = resolve_prop_role(dm.group(1)), dm.group(2)
            return dm.group(1) + ':' + COLOR_TOKEN.sub(lambda cm: transform_color(cm.group(0), prop), val)
        return 'style="' + re.sub(r'([a-zA-Z-]+)\s*:\s*([^;]+)', decl, style) + '"'
    return re.sub(r'style="([^"]*)"', patch_style, content)

# ---------- Sélecteur de langue par page ----------
def langswitch_html(lang, rel):
    """rel = chemin relatif de page (ex. 'blog.html', 'index.html' pour la home de langue)"""
    targets = {}
    for l in ('fr', 'en', 'es'):
        base = '' if l == 'fr' else l + '/'
        if rel == 'index.html':
            targets[l] = '/' if l == 'fr' else f'/{l}/'
        else:
            cand = SCRAPE / base / rel if l != 'fr' else SCRAPE / rel
            targets[l] = f'/{base}{rel}' if cand.exists() else ('/' if l == 'fr' else f'/{l}/')
    parts = []
    for l in ('fr', 'en', 'es'):
        lab = l.upper()
        if l == lang:
            parts.append(f'<span aria-current="page">{lab}</span>')
        else:
            parts.append(f'<a href="{targets[l]}" hreflang="{l}" lang="{l}">{lab}</a>')
    return '\n          '.join(parts)

# ---------- Assemblage ----------
PAGE_TMPL = """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="theme-color" content="#070A08">
  <meta name="color-scheme" content="dark">
{metas}
{links}
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" sizes="any">
  <link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="/favicon-16x16.png" type="image/png" sizes="16x16">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="/manifest.json">
{plausible}
{ldjson}
  <style>{css}</style>
  <style data-page-css>{page_css}</style>
  {theme_init}
</head>
<body{body_attrs}>
{skip}
{sprite}
{header}
<main id="main">
{content}
</main>
{footer}
{main_js}
{page_scripts}
</body>
</html>
"""

def process(src: pathlib.Path, log):
    rel_full = src.relative_to(SCRAPE).as_posix()
    lang = 'en' if rel_full.startswith('en/') else 'es' if rel_full.startswith('es/') else 'fr'
    rel = rel_full.split('/', 1)[1] if lang != 'fr' else rel_full
    html = src.read_text(encoding='utf-8', errors='replace')

    content, how = extract_content(html, rel_full)
    if content is None:
        log.append((rel_full, 'ERREUR: pas de body'))
        return False
    content = clean_content(content)
    bits = extract_head_bits(html)
    kept, dropped, need_faq = page_scripts(html, content)
    content = patch_inline_colors(content)

    header, footer = SHELLS[lang]
    ls = langswitch_html(lang, rel)
    header = header.replace('{LANGSWITCH}', ls)

    # attributs data-* et class du body d'origine (utiles aux scripts conservés)
    battrs = ''
    bm = re.search(r'<body([^>]*)>', html)
    if bm:
        keep_attrs = re.findall(r'(data-[\w-]+="[^"]*"|class="[^"]*")', bm.group(1))
        keep_attrs = [a for a in keep_attrs if a != 'class="light-mode"']
        if keep_attrs:
            battrs = ' ' + ' '.join(keep_attrs)

    page = PAGE_TMPL.format(
        lang=lang,
        title=bits['title'],
        metas='\n'.join('  ' + t for t in bits['metas']),
        links='\n'.join('  ' + t for t in bits['links']),
        plausible=('  ' + bits['plausible']) if bits['plausible'] else '',
        ldjson='\n'.join('  ' + t for t in bits['ldjson']),
        css=CSS_FULL + '\n' + CONTENT_CSS,
        page_css=collect_page_css(html, rel_full) + FONT_OVERLAY,
        theme_init=THEME_INIT,
        body_attrs=battrs,
        skip=SKIP_LINK.format(label=SKIP_LABELS[lang]),
        sprite=SPRITE,
        header=header,
        content=content,
        footer=footer,
        main_js=MAIN_JS,
        page_scripts='\n'.join(kept) + ('\n' + FAQ_FALLBACK_JS if need_faq else ''),
    )
    out = DIST / rel_full
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding='utf-8')
    log.append((rel_full, f'OK [{how}] scripts:+{len(kept)}/-{len(dropped)}' + (' +faqjs' if need_faq else '')))
    return True

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    log = []
    ok = fail = 0
    for src in sorted(SCRAPE.rglob('*.html')):
        rel = src.relative_to(SCRAPE).as_posix()
        if rel == 'index.html':
            continue  # home validée : copiée telle quelle par le packaging
        if only and only not in rel:
            continue
        if process(src, log):
            ok += 1
        else:
            fail += 1
    (SCRATCH / 'refonte_log.txt').write_text('\n'.join(f'{r}\t{s}' for r, s in log), encoding='utf-8')
    print(f'OK={ok} FAIL={fail}')
    for r, s in log:
        if 'ERREUR' in s or 'heuristic' in s:
            print(f'  {r}: {s}')

if __name__ == '__main__':
    main()

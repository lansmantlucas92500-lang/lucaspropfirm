#!/usr/bin/env python3
"""Refonte des pages internes lucaspropfirm.fr dans le design dark + neon green.

Stratégie : extraction du contenu <main> (ou heuristique pour les vieilles pages),
ré-habillage complet dans le shell du nouvel index.html (head, CSS, header, footer, JS),
conservation des metas SEO/JSON-LD et des scripts interactifs propres à chaque page.
"""
import re, sys, json, pathlib, html as htmlmod

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
SHELL_JS = re.compile(r'lp-rotbar|lp_rotbar', re.I)

def clean_content(content):
    # bannières cookies héritées (markup + scripts + liens externes obsolètes)
    content = remove_balanced(content, r'<div[^>]*(?:cookie-banner|cookieBanner|CookieConsent)[^>]*>')
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
    lead = body[:2000]
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
        if full and full.start() < 2000:
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

# ---------- Correctif couleurs dans les styles inline du contenu ----------
BG_MAP = {  # anciennes couleurs claires → surfaces sombres (déclarations background)
    'fff': 'var(--surface)', 'ffffff': 'var(--surface)', 'fffdfb': 'var(--surface)',
    'fbf8f4': 'var(--bg-1)', 'f5eee8': 'var(--surface-2)', 'f8eee9': 'var(--surface-2)',
    'fff3ee': 'rgba(44,232,120,.08)', 'f7dfd6': 'rgba(44,232,120,.15)',
}
FG_MAP = {  # anciens textes sombres → textes clairs (déclarations color)
    '211b18': 'var(--text-1)', '000': 'var(--text-1)', '000000': 'var(--text-1)',
    '222': 'var(--text-1)', '333': 'var(--text-1)', '1a1a1a': 'var(--text-1)',
    '625954': 'var(--text-2)', '444': 'var(--text-2)', '555': 'var(--text-2)',
    '867a73': 'var(--text-3)', '666': 'var(--text-3)', '777': 'var(--text-3)',
}
ANY_MAP = {  # accents et bordures, quel que soit le contexte
    'dc7353': 'var(--accent)', 'b94f32': 'var(--accent-bright)',
    'eaded6': 'var(--border)', 'd9c8bd': 'var(--border-strong)', 'efc8b9': 'var(--border-accent)',
}

def patch_inline_colors(content):
    def patch_style(m):
        style = m.group(1)
        def decl(dm):
            prop, val = dm.group(1), dm.group(2)
            low = val.lower()
            for hexv, new in ANY_MAP.items():
                low = low.replace('#' + hexv, new)
            hm = re.fullmatch(r'\s*#([0-9a-f]{3}|[0-9a-f]{6})\s*', low)
            if hm:
                h = hm.group(1)
                if 'background' in prop and h in BG_MAP:
                    low = BG_MAP[h]
                elif prop.strip() == 'color' and h in FG_MAP:
                    low = FG_MAP[h]
            return prop + ':' + low
        style = re.sub(r'([a-z-]+)\s*:\s*([^;]+)', decl, style)
        return 'style="' + style + '"'
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
    if how == 'heuristic':
        # les pages les plus anciennes n'ont pas de conteneur : on borne la largeur
        content = '<div class="container" style="padding-block:40px">\n' + content + '\n</div>'
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

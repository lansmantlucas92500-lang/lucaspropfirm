#!/usr/bin/env python3
"""Répare les défauts de contraste résiduels : injecte des overrides ciblés
(<style data-contrast-fix>) dans les pages listées par contrast_report.json."""
import json, re, sys, pathlib, colorsys

SCRATCH = pathlib.Path('/tmp/claude-0/-home-user-lucaspropfirm/b7529ed5-1ed9-5596-90c1-47ef76569d2a/scratchpad')
DIST = SCRATCH / 'dist'
REPORT = SCRATCH / 'contrast_report.json'

def rel_lum(r, g, b):
    def f(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def pick_color(fg_str, bg_str):
    """Couleur de remplacement : claire de même famille sur fond sombre, encre sombre sur fond clair."""
    bg = [float(x) for x in bg_str.split(',')[:3]]
    if rel_lum(*bg) > 0.45:
        return '#06180d'  # fond clair → encre sombre
    m = re.findall(r'[\d.]+', fg_str)
    if not m:
        return '#e6ece7'
    r, g, b = float(m[0]) / 255, float(m[1]) / 255, float(m[2]) / 255
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    deg = h * 360
    if s < 0.13:
        return '#e6ece7'
    if 80 <= deg <= 170:
        return '#a7ffcd'
    if deg < 15 or deg > 340:
        return '#ffb4b4'
    if 15 <= deg < 80:
        return '#ffe1a8'
    return '#bcd0ff'

# Cas particuliers : même classe posée sur des fonds différents dans la même page —
# une couleur unique ne peut pas convenir, on force un fond propre à l'élément.
SPECIAL = {
    '3-setups-es-nq-trading-futures.html':
        'main a.button.button--secondary{background:rgba(4,23,12,.5)!important;'
        'color:#a7ffcd!important;border:1px solid rgba(167,255,205,.35)!important}',
}

def main():
    rep = json.loads(REPORT.read_text())
    pages = 0
    rules_total = 0
    for page, fails in rep.items():
        rules = {}
        for f in fails:
            sel = f.get('sel')
            if not sel or f['sig'] == 'ERROR':
                continue
            if '.' not in sel:
                continue  # jamais de sélecteur nu (a, span…) : trop large, dégâts collatéraux
            if not re.fullmatch(r'[a-zA-Z][\w-]*(?:\.[A-Za-z_][\w-]*)+|\.[A-Za-z_][\w-]*(?: [a-zA-Z][\w-]*(?:\.[A-Za-z_][\w-]*)*)?', sel):
                continue
            rules[f'main {sel}'] = pick_color(f['color'], f['bg'])
        if not rules:
            continue
        path = DIST / page
        html = path.read_text(encoding='utf-8')
        # fusionner avec les overrides d'une itération précédente ; si un sélecteur
        # échoue encore malgré sa réparation, escalader vers le contraste maximal
        prev_rules = {}
        prev = re.search(r'<style data-contrast-fix>(.*?)</style>', html, re.S)
        if prev:
            for pm in re.finditer(r'([^{}]+)\{color:([^;!]+)!important\}', prev.group(1)):
                prev_rules[re.sub(r'^body ', '', pm.group(1).strip())] = pm.group(2)
        for sel in list(rules):
            if sel in prev_rules:
                rules[sel] = '#06180d' if rules[sel] == '#06180d' else '#ffffff'
        merged = dict(prev_rules)
        merged.update(rules)
        css = ''.join(f'body {sel}{{color:{col}!important}}' for sel, col in merged.items())
        if page in SPECIAL:
            # retirer l'override couleur générique concurrent puis appliquer le patch dédié
            merged.pop('main a.button.button--secondary', None)
            css = ''.join(f'body {sel}{{color:{col}!important}}' for sel, col in merged.items()) + SPECIAL[page]
        html = re.sub(r'<style data-contrast-fix>.*?</style>\n?', '', html, flags=re.S)
        html = html.replace('</body>', f'<style data-contrast-fix>{css}</style>\n</body>')
        path.write_text(html, encoding='utf-8')
        pages += 1
        rules_total += len(rules)
    print(f'réparé: {pages} pages, {rules_total} overrides')

if __name__ == '__main__':
    main()

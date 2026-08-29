import { chromium } from 'playwright';
import { readdirSync, statSync, writeFileSync } from 'fs';
import { join } from 'path';

function listHtml(dir, base = '') {
  const out = [];
  for (const f of readdirSync(dir)) {
    const p = join(dir, f);
    if (statSync(p).isDirectory()) out.push(...listHtml(p, base + f + '/'));
    else if (f.endsWith('.html')) out.push(base + f);
  }
  return out;
}
const pages = listHtml('dist').filter(p => p !== 'index.html'); // home validée exclue
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });

const AUDIT_JS = () => {
  // luminance relative WCAG
  const lum = (r, g, b) => {
    const f = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const parse = c => { const m = c.match(/[\d.]+/g); return m ? m.map(Number) : null; };
  const ratio = (l1, l2) => (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  // fond effectif : remonte et compose l'alpha ; approx gradient via backgroundImage premier stop
  function effBg(el) {
    let r = 7, g = 10, b = 8; // bg-0
    const stack = [];
    let a = el;
    while (a && a.nodeType === 1) { stack.unshift(a); a = a.parentElement; }
    for (const n of stack) {
      const s = getComputedStyle(n);
      let c = s.backgroundColor, p = parse(c);
      if (s.backgroundImage && s.backgroundImage.includes('gradient')) {
        const gm = s.backgroundImage.match(/rgba?\([^)]+\)/);
        if (gm) { const gp = parse(gm[0]); if (gp) { p = gp; if (gp.length === 3) p = [...gp, 1]; } }
      }
      if (p) {
        const al = p.length === 4 ? p[3] : 1;
        if (al > 0) { r = p[0] * al + r * (1 - al); g = p[1] * al + g * (1 - al); b = p[2] * al + b * (1 - al); }
      }
    }
    return [r, g, b];
  }
  const fails = [];
  const seen = new Set();
  document.querySelectorAll('main *, main').forEach(el => {
    // uniquement les éléments avec du texte direct
    let txt = '';
    for (const n of el.childNodes) if (n.nodeType === 3) txt += n.textContent;
    txt = txt.trim();
    if (txt.length < 3) return;
    const rect = el.getBoundingClientRect();
    if (rect.width < 8 || rect.height < 8) return;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity === 0) return;
    const fg = parse(s.color); if (!fg) return;
    const fa = fg.length === 4 ? fg[3] : 1;
    if (fa === 0) return;
    const bg = effBg(el);
    const fr = fg[0] * fa + bg[0] * (1 - fa), fgg = fg[1] * fa + bg[1] * (1 - fa), fb = fg[2] * fa + bg[2] * (1 - fa);
    const cr = ratio(lum(fr, fgg, fb), lum(...bg));
    const size = parseFloat(s.fontSize);
    const bold = +s.fontWeight >= 600;
    const need = (size >= 24 || (size >= 18.5 && bold)) ? 3 : 4.5;
    if (cr < need) {
      const clean = c => (c || '').toString().split(' ').filter(x => /^[A-Za-z_][\w-]*$/.test(x)).slice(0, 2);
      const own = clean(el.className);
      let sel = el.tagName.toLowerCase() + own.map(c => '.' + c).join('');
      if (!own.length) {
        let anc = el.parentElement;
        while (anc && anc.tagName !== 'MAIN' && !clean(anc.className).length) anc = anc.parentElement;
        const ac = anc && anc.tagName !== 'MAIN' ? clean(anc.className) : [];
        if (ac.length) sel = '.' + ac[0] + ' ' + sel;
      }
      const sig = sel;
      if (seen.has(sig)) return;
      seen.add(sig);
      fails.push({ sig, sel, cr: +cr.toFixed(2), color: s.color, bg: bg.map(Math.round).join(','), txt: txt.slice(0, 40), size: Math.round(size) });
    }
  });
  return fails;
};

const results = {};
let done = 0;
const CONC = 6;
async function worker(chunk) {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  await ctx.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  const page = await ctx.newPage();
  for (const rel of chunk) {
    try {
      await page.goto('file://' + process.cwd() + '/dist/' + rel, { waitUntil: 'load', timeout: 30000 });
      await page.waitForTimeout(120);
      const fails = await page.evaluate(AUDIT_JS);
      if (fails.length) results[rel] = fails;
    } catch (e) { results[rel] = [{ sig: 'ERROR', txt: e.message.slice(0, 60) }]; }
    if (++done % 50 === 0) console.log('...', done);
  }
  await ctx.close();
}
const chunks = Array.from({ length: CONC }, () => []);
pages.forEach((p, i) => chunks[i % CONC].push(p));
await Promise.all(chunks.map(worker));
await browser.close();
writeFileSync('contrast_report.json', JSON.stringify(results, null, 1));
const totalFails = Object.values(results).reduce((s, v) => s + v.length, 0);
console.log(`pages auditées: ${pages.length} | pages avec échecs: ${Object.keys(results).length} | échecs uniques: ${totalFails}`);

const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + root + '/build/curso-nail-designer.html', { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // overflow check
  const over = await page.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => {
    const r = p.getBoundingClientRect(); let maxB = 0;
    p.querySelectorAll('*').forEach(e => { if (e.closest('.foot') || e.closest('.cover-hand')) return; const b = e.getBoundingClientRect().bottom; if (b > maxB) maxB = b; });
    return { page: i + 1, spare_mm: ((r.bottom - 15 * 3.78) - maxB) / 3.78 };
  }));
  console.log(JSON.stringify(over));
  await page.pdf({ path: root + '/Curso-Nail-Designer.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();

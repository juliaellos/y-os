// Renderiza os banners do YouTube (2560 x 1440) e as prévias de recorte.
// Uso: node identidade/banner-youtube/render.js
// Reaproveita o Playwright instalado no carrossel em stand-by.
const { chromium } = require('../../marketing/conteudo/STAND_BY_carrossel-tempo-economizado-2026-09-16/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const VERSIONS = [
  { v: 'a', name: 'banner-a-com-a-sua-cara' },
  { v: 'b', name: 'banner-b-junto-com-voce' },
];
const MAX_BYTES = 6 * 1024 * 1024;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2560, height: 1440 } });
  const url = (file, q) => 'file://' + path.resolve(__dirname, file) + '?' + q;

  for (const { v, name } of VERSIONS) {
    await page.goto(url('banner.html', 'v=' + v));
    await page.waitForSelector('body[data-ready="1"]');
    await page.waitForTimeout(300);

    // Confere se texto e logo ficaram dentro da área segura.
    const check = await page.evaluate(() => {
      const safe = document.querySelector('.safe').getBoundingClientRect();
      const items = [...document.querySelectorAll('.safe .promise, .safe .sign')].map(el => el.getBoundingClientRect());
      const box = {
        left: Math.min(...items.map(r => r.left)), right: Math.max(...items.map(r => r.right)),
        top: Math.min(...items.map(r => r.top)), bottom: Math.max(...items.map(r => r.bottom)),
      };
      return {
        width: Math.round(box.right - box.left), height: Math.round(box.bottom - box.top),
        inside: box.left >= safe.left && box.right <= safe.right && box.top >= safe.top && box.bottom <= safe.bottom,
      };
    });

    const out = path.join(__dirname, name + '.png');
    await page.screenshot({ path: out });
    const size = fs.statSync(out).size;
    console.log(`${name}.png  conteúdo ${check.width}x${check.height} (área segura 1235x338)  ` +
      `${check.inside ? 'dentro' : 'FORA DA ÁREA SEGURA'}  ${(size / 1024 / 1024).toFixed(2)} MB` +
      (size > MAX_BYTES ? '  ACIMA DE 6 MB' : ''));
  }

  const preview = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  for (const { name } of VERSIONS) {
    await preview.goto(url('previa.html', 'img=' + name));
    await preview.waitForSelector('body[data-ready="1"]');
    await preview.screenshot({ path: path.join(__dirname, name.replace('banner-', 'previa-') + '.png'), fullPage: true });
    console.log('salvo:', name.replace('banner-', 'previa-') + '.png');
  }

  await browser.close();
})();

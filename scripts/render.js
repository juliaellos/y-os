// Renderiza uma página HTML em PNG, no tamanho exato.
//
// Uso:
//   node scripts/render.js "<arquivo.html[?parametros]>" <saida.png> <largura> <altura>
//
// Exemplos:
//   node scripts/render.js "identidade/thumbnail-template.html?v=1" thumb.png 1280 720
//   node scripts/render.js "identidade/capa-reels-template.html?v=1" capa.png 1080 1920
//
// Se a página marcar <body data-ready="1"> (os templates marcam depois de
// ajustar o tamanho do texto), o render espera por isso antes do print.
//
// Playwright: usa o instalado na raiz, se existir. Se não, reaproveita o
// que está na pasta do carrossel em stand-by.

const path = require('path');

function loadPlaywright() {
  try {
    return require('playwright');
  } catch (e) {
    return require(path.resolve(__dirname, '../marketing/conteudo/STAND_BY_carrossel-tempo-economizado-2026-09-16/node_modules/playwright'));
  }
}

(async () => {
  const [input, output, w, h] = process.argv.slice(2);
  if (!input || !output || !w || !h) {
    console.log('Uso: node scripts/render.js "<arquivo.html[?parametros]>" <saida.png> <largura> <altura>');
    process.exit(1);
  }

  const [file, query] = input.split('?');
  const url = 'file://' + path.resolve(file) + (query ? '?' + query : '');
  const width = Number(w);
  const height = Number(h);

  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForSelector('body[data-ready="1"]', { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(200);

  const warnings = await page.evaluate(() => window.__avisos || []);
  warnings.forEach(a => console.log('AVISO:', a));

  await page.screenshot({ path: output, clip: { x: 0, y: 0, width, height } });
  const mb = require('fs').statSync(output).size / 1024 / 1024;
  console.log(`salvo: ${output} (${mb.toFixed(2)} MB)`);
  // O YouTube recusa thumbnail acima de 2 MB
  if (width === 1280 && height === 720 && mb > 2) console.log('AVISO: acima de 2 MB, o YouTube não aceita. Exportar em JPG.');
  await browser.close();
})();

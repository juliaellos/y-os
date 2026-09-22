const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + path.resolve(__dirname, 'estudo-visual.html'));
  await page.waitForTimeout(400);

  const outDir = path.resolve(__dirname, 'estudo');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const names = [
    'narrativa-A-barra.png',
    'narrativa-B-blocos.png',
    'narrativa-C-arco.png',
    'textura-1-grao.png',
    'textura-2-grao-glow.png',
    'textura-3-grao-glow-grid.png',
  ];

  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(outDir, names[i]) });
    console.log('salvo:', names[i]);
  }

  await browser.close();
})();

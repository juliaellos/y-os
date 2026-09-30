const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

// Duas passadas: o slide 7 mostra miniaturas dos próprios PNGs, então a
// segunda passada pega as imagens geradas na primeira.
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const filePath = 'file://' + path.resolve(__dirname, 'carrossel.html');
  const outDir = path.resolve(__dirname, 'instagram');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  for (let pass = 1; pass <= 2; pass++) {
    await page.goto(filePath);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(400);
    const slides = await page.$$('.slide');
    for (let i = 0; i < slides.length; i++) {
      const name = `slide-${String(i + 1).padStart(2, '0')}.png`;
      await slides[i].screenshot({ path: path.join(outDir, name) });
      if (pass === 2) console.log('salvo:', name);
    }
  }

  await browser.close();
})();

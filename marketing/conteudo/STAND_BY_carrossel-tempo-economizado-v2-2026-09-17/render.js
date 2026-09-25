const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const filePath = 'file://' + path.resolve(__dirname, 'carrossel.html');
  await page.goto(filePath);
  await page.waitForTimeout(300);

  const outDir = path.resolve(__dirname, 'instagram');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    const name = `slide-${String(i + 1).padStart(2, '0')}.png`;
    await slides[i].screenshot({ path: path.join(outDir, name) });
    console.log('salvo:', name);
  }

  await browser.close();
})();

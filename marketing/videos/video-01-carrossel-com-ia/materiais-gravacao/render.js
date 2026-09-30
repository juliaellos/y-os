const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 759, height: 665 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(__dirname, 'prompt-card.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.locator('.card').screenshot({ path: path.resolve(__dirname, 'prompt-card.png'), scale: 'css' });
  await browser.close();
  console.log('salvo: prompt-card.png');
})();

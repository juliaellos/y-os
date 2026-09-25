const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 540, height: 675 } });
  const filePath = 'file://' + path.resolve(__dirname, 'mockup-exemplo.html');
  await page.goto(filePath);
  await page.waitForTimeout(300);

  const mocks = await page.$$('.mock');
  const names = ['exemplo-mock-01.png', 'exemplo-mock-02.png'];
  for (let i = 0; i < mocks.length; i++) {
    await mocks[i].screenshot({ path: path.resolve(__dirname, names[i]) });
    console.log('salvo:', names[i]);
  }

  await browser.close();
})();

const path = require("path");

const runAction = require("pa11y/lib/action");

const scenarios = require("./scenarios");

const puppeteer = require("puppeteer");

(async () => {
  try {
    const browser = await puppeteer.launch({ args: ["--no-sandbox"] });
    const page = await browser.newPage();

    await page.goto("http://localhost:8000/admin/");

    await processScenarios(browser, page, scenarios);

    await page.screenshot({ path: path.join(__dirname, "test.png") });
    await browser.close();
  } catch (err) {
    console.log(err); // TypeError: failed to fetch
  }

  async function processScenarios(browser, page, scenarios) {
    for (const s of scenarios) {
      try {
        await processActions(browser, page, s);
      } catch (err) {
        console.log(err); // TypeError: failed to fetch
      }
    }
  }

  async function processActions(browser, page, scenario) {
    for (const action of scenario.states[0].actions) {
      try {
        await runAction(
          browser,
          page,
          {
            log: {
              debug: l => console.log(l)
            }
          },
          action
        );
      } catch (err) {
        console.log(err); // TypeError: failed to fetch
      }
    }
  }
})();

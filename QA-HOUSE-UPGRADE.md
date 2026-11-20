# Interactive House / Energy — QA Summary

Build date: 2026-11-11

## Automated checks
- Existing site tests: PASS.
- Shared home energy regression: PASS.
- JavaScript static syntax, HTML links and script imports: PASS.
- Isolated Chromium visual + interaction tests: PASS, including a real rendered canvas and click controls.

## Chromium checks (isolated component previews)
- Desktop: canvas renders without JS errors; orbit drag changes pixels; roof-open and roof-close work.
- 1 AC -> 2 AC: increased electricity estimate and reduced illustrative indoor temperature.
- Adding a fan: increased electricity use and changed comfort estimate but *not* air temperature.
- Reflective roof: changed illustrative temperature and heat model.
- Energy flow categories: click selection works, highlights data and shows matching consumption.
- Data passed to Energy & Savings: verified AC=2 and fans=4 after editing the house profile.
- Solar and rainwater calculator modules still run after Energy & Savings changes.
- Mobile 390px: no horizontal document overflow in isolated component screenshot; no JS page errors.

## Not yet validated
- Complete site deployment on GoDaddy (including third-party APIs, maps, CORS, authentication and email configuration).
- End-to-end navigation in live site; local URLs were blocked by Chromium's administrator policy in this environment. The isolated component tests used injected HTML and JS.
- Independent engineering accuracy, real HVAC COP, actual indoor-temperature outcomes, exact installation costs or actual utility generation provenance.
- Full accessibility audit with assistive technologies.

This release is a functioning interactive demonstration with transparent simulation limitations, not a certified building energy model.

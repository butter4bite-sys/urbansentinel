# Urban Sentinel — Judges' Readiness QA (19 November 2026)

## Implemented checks

- [x] Existing website regression tests: 12 suites pass (`npm test`).
- [x] Added `tests/judge-ready-regression.mjs`: 13th suite passes. Tests shared Cooling Planner storage, budgeted physical measures, duplicate/mismatched property inputs, two-floor placement, heat screening, roof absorbed-solar calculation, no fabricated appliance savings, provider count, and agreement-not-confirmed defaults.
- [x] JavaScript source syntax: `node --check` across local JS modules passes.
- [x] PHP backend syntax: `php -l` across backend PHP files passes.
- [x] Navigation and local file/link checks: covered by `tests/verify.mjs` and DOM smoke checks (pass).
- [x] Marketplace commission and consumer-versus-contractor disclosure is visible in frontend source.
- [x] Public directory contains nine uniquely named Pune businesses, initial agreement status false for all until explicitly approved.
- [x] Fresh setup maps the default business account to the intended Diligent Enterprises record (instead of the first seeded record).

## Not yet demonstrated in deployed production conditions

- [ ] Live visual WebGL test in ordinary Chrome/Edge with hardware graphics: browser navigation was blocked by this environment's administrator policy, so no completed interactive screenshot QA of this *specific release* can be claimed here.
- [ ] Android/iOS install behavior and mobile rendering on real devices.
- [ ] Live weather, AQI, external tiles and relevant source licensing on the destination HTTPS hostname.
- [ ] End-to-end live PHP account setup, privacy retention, referral email/notification (not implemented), contractor consent and commission contract acceptance for this deployment.
- [ ] Supplier confirmation of actual quotations/installed savings and calibrated engineering verification.

## Required last-mile actions

1. Copy website to a staging domain or fresh XAMPP folder. Back up and preserve private owner/contractor data stored outside web root.
2. Re-run `npm test`, use browser DevTools Console and Network tab on `assessment.html`, `3d-simulation.html`, `marketplace.html`, `energy-savings.html`.
3. On a desktop and mobile phone, walk through `JUDGE-DEMO-WALKTHROUGH.md`; confirm each floor, window, roof and zoom/Indoor control.
4. In the owner portal, import/refresh nine businesses; verify names and phone numbers, obtain real agreement consent, then enable callbacks for genuinely participating providers.
5. Ensure backup copy of the PPT and a prerecorded offline demo video in case of unreliable internet or API failures on viva day.

**Status:** Competition **staging candidate**, not certified thermal/CFD analysis, not a production-verified referral business, not confirmed signed partnerships.

# Urban Sentinel — Judges' Ready Cooling & 3D Edition
**Release:** 19 November 2026 · staging / competition candidate

Urban Sentinel is a free, India-focused environmental property assessment and cooling-planning website. The central competition workflow is **Cooling Planner → synchronized multi-floor 3D Simulation → Start Simulation → Original vs Improved comparison → contractor directory and optional tracked referrals**.

The dark teal/green website, existing weather/AQI maps, Indoor movement, energy/water tools, PWA install option and secure PHP owner/contractor access are retained.

## What's changed in this release

1. **Competition-ready 3D workflow:** guided house questions, manual controls, per-floor windows/appliances, and clearly explained demo buttons. The original and improved scenarios are displayed in the same interactive house and camera angle.
2. **Connected Cooling Planner:** on submission the selected budgeted measures are saved. In the 3D tab, **Apply saved Cooling Plan** translates supported selected interventions into roof treatments, shade structures or ventilation elements. Professional survey steps remain advisory. Mismatched property city or floor area triggers a warning.
3. **Meaningful Before vs After table:** side-by-side numeric original/improved heat/comfort risk *indices*, floor ventilation opportunity, absorbed roof solar power in kW, selected improvement cost allowance and monthly appliance kWh. No fabricated indoor temperature savings.
4. **Business model transparency:** the marketplace explains free customer use, consent-based referral IDs, contractor verification, completed-project evidence and a configurable illustrative success commission. A sample 5% on ₹50,000 = ₹2,500 is not real revenue or a contracted rate.
5. **Named Pune businesses:** eight public business listings plus Diligent Enterprises, with contact channels and public source details. The owner must explicitly verify a business's identity and agreement before it appears as a **Confirmed Urban Sentinel partner**, and separately enable referrals.
6. **Data correction:** a previously generic Shivajinagar solar listing with an unreliable contact was replaced with the named Unishark Solar entry.

## Pages to demonstrate

- `assessment.html` — Cooling Planner and budgeted measure suggestions.
- `3d-simulation.html` — primary interactive 3D Simulation page with guided setup, Indoor, floor selection, Start Simulation, applied Cooling Plan and Before/After comparisons.
- `energy-savings.html` — electricity, solar, rainwater analyses and explanatory flowcharts.
- `city-intelligence.html`, `aqi.html`, `temperature.html` — environmental info and maps, clearly distinguishing API data vs imagery.
- `marketplace.html` — public providers, indicative commission calculator and referral workflow for **approved** partners.
- `access.html` — owner and contractor portal (requires PHP one-time installation).

Old climate-lab and other duplicate simulator URLs redirect to the 3D Simulation entry; they are not separate tabs.

## Installation

Extract **the contents of the ZIP**, not an additional parent directory, into `C:\xampp\htdocs\urban-sentinel\` or GoDaddy `public_html/`. Confirm `index.html`, `3d-simulation.html`, `backend/setup.php` and `assets/` are alongside each other. Visit `http://localhost/urban-sentinel/` or your HTTPS domain.

**Existing installation:** back up the site and private referral storage first. The server's private data is expected *outside* the public web root; preserve those files. Existing owner/contractor accounts are not overwritten by copying HTML files. The owner can import/refresh named public providers from the portal.

**New installation:** read `REFERRAL-SETUP.md`. Initialize the PHP portal with its separate private key (not bundled in the public website ZIP). Do not put setup keys, private passwords or protected lead data inside public files. Use HTTPS before collecting customer contact details.

## Tests and integrity

Run `npm test` to execute the **13 automated regression suites** (12 inherited, plus the new judge-readiness test). `node --check` and PHP syntax checks are also performed before packaging. Full live browser/WebGL, mobile-device and provider-referral production checks remain mandatory and are **not** implied by passing unit/regression tests.

Read:
- `JUDGE-DEMO-WALKTHROUGH.md` — presentation-day sequence and anticipated technical/business questions.
- `JUDGE-MODEL-BOUNDARIES.md` — exact calculation claims and their limitations.
- `MARKETPLACE-CONTRACTOR-STATUS.md` — nine provider names and how to authorize a partnership honestly.
- `JUDGES-RELEASE-QA.md` — test and deployment status.
- `3D-SIMULATION-GUIDE.md`, `REFERRAL-SETUP.md` and `DEPLOY-GODADDY.md` — user and hosting instructions.

**Scientific boundary:** heat and wind visuals are screening-level scenarios, not CFD or a calibrated indoor-temperature forecast. Costs are allowances, not quotations. Public directory entries are not automatically official partnerships. Google cloud sync and live payment handling are not provided.

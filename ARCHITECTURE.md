**Architecture update — 18 November 2026:** `3d-simulation.html` is the single interactive house/simulation workspace, replacing the visible Climate Lab navigation. `assets/js/simulation-design.js` stores per-floor design objects and links them to `us4.property` (Cooling Plan) and `us4.calc.electricity` (Energy & Water). The simulation is an educational screening visualization, not CFD or a certified thermal model. `manifest.webmanifest`, `sw.js` and `assets/js/pwa-install.js` support home-screen installation; the SW never caches private owner/contractor APIs. Owner-managed Pune prospects can be imported unverified through the secured portal. See `3D-SIMULATION-GUIDE.md` and `QA-3D-SIMULATION.md`.

---

# Urban Sentinel architecture — SPARTA phase 1/2

The product is a responsive static HTML/CSS/JS application, with optional PHP OAuth/feedback endpoints on GoDaddy-compatible hosting.

- `assets/js/shell.js`: consistent navigation, **one Climate Lab** entry, SVG energy symbol, no plan gate.
- `assets/js/features.js`: current 7 relevant Climate Lab tools. Retired demos do not appear in the navigation or package.
- `assets/js/before-after.js`: shared photographic reference property and before/after studio; live controls, click hotspots, optical overlays and independent roof-energy/cost calculations; saved to localStorage.
- `assets/js/impact-model.js`: independently testable solar absorption, solar-electricity and rainwater formulas. Screening only.
- `assets/js/solar-science.js`: NOAA-style local solar position (India IST), azimuth and unobstructed shadow length.
- `assets/js/satellite-map.js`: real EOX Sentinel-2 2016 optical imagery, optional NASA VIIRS daily RGB optical imagery and OSM fallback; attribution, marker interaction, city lookup. Image pixels are **NOT** interpreted as heat measurements.
- `assets/js/climate-lab.js`: remaining relevant scientific tools — geographic solar-shadows, rainwater runoff, house heat-gain breakdown, roof comparison and cooling budget screen.
- `assets/js/pages/temperature.js`, `aqi.js`: temperature/AQI from external Open-Meteo/CAMS models, plotted separately over satellite or street basemaps, with their original provider/cache/error behavior.
- `assets/js/city-satellite.js`: context map under City Intelligence, following selected city.
- `assets/js/property-profile.js`: browser-saved structured shared property profile. No cloud sync.
- `assets/js/marketplace.js`: public third-party company contacts with official source links; not partners.
- `assets/css/sparta.css`: photographic visuals, satellite context, modern scientific layouts; keeps original design system.

See `RELEASE-NOTES-SPARTA.md`, `MODEL-METHODOLOGY.md`, `QA-SPARTA.md`, and `DEPLOY-GODADDY.md` for limitations, licensing and deployment prerequisites.


## November 2026 update — referral portal

The former Google account sign-in for customers was retired. Partner access uses `backend/setup.php`, `backend/api.php`, and `backend/portal.php`, and the new customer referral form is in `marketplace.html`. Passwords are entered at one-time setup, hashed server-side, and private referral data is stored outside the web document root. See `REFERRAL-SETUP.md` for authoritative current behavior; any older references to the Google demo are historical.

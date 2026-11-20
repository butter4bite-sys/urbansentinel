# QA — Urban Sentinel 3D Simulation edition

Tested in the build environment on 18 November 2026.

## Automated tests
- `npm test`: 12/12 suites passed. Includes legacy assessments, project reports, weather/AQI fallbacks, maps, referral backend contracts, energy/thermal invariants, mock-WebGL geometry, and the new multi-floor simulation regression.
- Dedicated multi-floor test covers three storeys, independent windows and equipment lists, opposing-window vs closed-window air-flow opportunity, zero-irradiance calculation, AC sensitivity, manual fridge placement, local persistence, Energy & Savings sync, legacy navigation.
- JavaScript syntax validated for new modules. Visual screenshots were captured via headless Chromium in a sandboxed inline-module fixture, because direct local-server navigation is blocked in this environment.

## Browser checks
- Desktop 1440 × 900: generated duplex with two floors, added a window to floor 2, toggled simulation, entered Indoor, moved back to ground floor. No uncaught JavaScript errors.
- Mobile 390 × 844: same controls reached; no horizontal overflow; no uncaught JavaScript errors.
- The browser fixture did not expose a visible working WebGL renderer. The existing renderer's mock-WebGL geometry regression passed, and its 2D compatibility walkthrough was exercised. **Real GPU/WebGL on an actual desktop and phone still needs staging verification.**
- The PWA manifest, service worker and installation prompt were added and syntax checked. Actual phone install / HTTPS deployment must be verified on hosting.

## Scientific limitations
- Animated wind and relative temperature indices are illustrative, **not CFD, measured airflow or surface/indoor temperature forecasts**.
- Roof absorption is calculated from user-supplied dimensions, reflectance assumptions, shade and shortwave input, not thermal satellite measurement. Nighttime zero sun stays zero.
- Interior visuals are procedural architectural sketches, not as-built scans. No guarantee of professional engineering accuracy or full photorealism.
- Data persists in browser storage; cross-device sync is not implemented.

## Deployment/regression checklist
- Open `index.html`, `assessment.html`, `3d-simulation.html`, `energy-savings.html`, `aqi.html`, `temperature.html`, `marketplace.html` and `access.html` in HTTPS/XAMPP.
- Confirm former `climate-lab.html` links redirect to 3D Simulation.
- Change dimensions and save a cooling plan; check the shared footprint and window orientation.
- Generate three floors; manually add one AC to floor 2; check energy totals, reopen 3D Simulation and save/reopen a scenario.
- Enter Indoor on each floor; verify windows, lighting, appliances and mobile walking buttons; ensure the 3D camera initializes on a WebGL-capable phone.
- Start simulation; close all openings, change wind direction, change roof insulation and ensure visual and screening outputs respond.
- Confirm public customer referral, owner login and contractor role isolation are unaffected; private data backups stay intact.
- Verify install prompt on Android Chrome and Add to Home Screen in iOS Safari, over HTTPS.

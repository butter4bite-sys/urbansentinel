# Urban Sentinel — Interactive House Climate Upgrade

## Scope and unchanged areas
Built on the supplied SPARTA Phase 1+2 site. Original theme, navigation, satellite/AQI/temperature maps, marketplace, Climate Lab grouping, other simulators, authentication, and hosting approach remain unchanged.

Only the Digital Twin, Before vs After and Energy & Savings workflow and their saved-scenario bridge were enhanced.

## Interactive 3D architectural view
- **3D coordinates with continuous orbit**: drag/touch to rotate; mouse wheel to zoom; arrow keys when the canvas is focused.
- Open/close the roof to inspect indoor furniture and appliances.
- Switch between **Architectural**, **Thermal view**, and **Energy flow**.
- Controls for outdoor temperature, solar intensity, shading, reflective coating and roof insulation. Both environmental inputs default to clearly labeled assumptions. The **Use local weather data** button optionally retrieves a modelled outdoor 2m temperature and shortwave radiation from the existing city/weather services, with timestamp/source and fallback warnings.
- Add/remove ACs, ceiling fans, LED lights, refrigerators. Add AC/fan position by choosing a placement tool and clicking on the exposed model floor.
- Color-mapped floor and roof show an **illustrative relative heat index**, not thermal-camera or satellite measurements.
- The scene is a conceptual building geometry model, not a photorealistic scan, CFD output or construction drawing. No claimed prediction of actual cooling savings.
- Reference house photos and the photographic Before vs After view were preserved below the new interactive model.

## Energy data integration
Both House Climate Studio and Electricity Bill Detective use `localStorage['us4.calc.electricity']`. They share:
- Air-conditioner count, average kW, hours/day and days/month.
- Fan count, kW per fan and hours/day.
- LED light count, wattage and hours/day.
- Refrigerator count and average running kW.
- Other appliance energy, billed units and effective tariff.

The Energy & Savings page adds a clickable household electricity-flow diagram: assumed utility-meter supply plus optional *modeled* rooftop solar potential, branching to appliance categories. It does NOT identify the actual power plant, transmission substation or household electrical wiring and cannot verify a solar share of grid consumption.

Existing user data is migrated conservatively: when older saved entries have only an `other` category, lights and refrigerators default to zero to prevent double-counting. The original bill history key is unchanged.

## Model assumptions and limitations
This is a rule-of-thumb **screening sensitivity model** (see `assets/js/home-energy-model.js`). Ambient temperature and solar intensity are user input assumptions. Roof absorbed solar power uses area × irradiance × (1 - reflectance) × (1 - shade). The illustrative indoor temperature estimator then applies assumed roof transfer, internal heat and assumed AC cooling effect (COP 2.8). These parameters have NOT been calibrated or validated against building measurements. Heat colors are a relative comfort/heat-risk proxy. Fans change perceived comfort, **not dry-bulb air temperature**. Refrain from using these outputs for HVAC sizing, health/safety decisions or vendor performance guarantees.

## Saved scenarios
The House Climate Studio saves the selected appliance counts, location/property profile, assumed conditions, heat score and placed AC/fan positions under the existing local `us4.scenarios` key. On My Projects, House Climate scenarios link back to `digital-twin.html?scenario=...` for restoring the scene. Data remains **browser-local**, not cloud-synced. Printable Before vs After and original scenario workflows remain available.

## Running and hosting
Static HTML/CSS/JS, no new external dependency or API keys. Compatible with the same GoDaddy static/PHP hosting as the prior SPARTA site.

To test locally, serve the folder over HTTP (`python -m http.server 8000`) rather than opening ES modules via `file://` in the browser.

## Testing performed
- Eight automated Node test suites passed (old suites plus shared climate/energy regression).
- Chromium isolated-component tests verified house canvas drawing, camera drag, reactive AC and fan values, reflective roof sensitivity, clickable energy-flow routes, shared saved data, solar/rain calculators and responsive 390px width, with zero JS page errors.
- Full website navigation was checked by existing automated tests; live deployed browser and third-party API checks were **not** performed. Staging verification on the actual GoDaddy site is still recommended.

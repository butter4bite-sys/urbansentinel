# Urban Sentinel — SPARTA (Phase 1 + Phase 2)

## Completed in this package

- Kept the original Urban Sentinel teal/green theme, main pages, free access, Climate Lab hub, and model-driven temperature/AQI maps.
- Removed the irrelevant particle-flow visualizer, fictional Future City 2050 scene, gamified Climate Challenge stub, duplicate Climate DNA screen, and an unsupported local Business Workspace from distribution and navigation.
- Replaced the old block-house 2.5D neighborhood display with a photographic property improvement studio for bungalow, duplex, sloped roof and apartment references. Interactive R/S/T markers change roof, shade and planting overlays; editable property dimensions affect the independent roof-absorption model, costs, and saved scenarios.
- Before and After views always share the same house reference, camera and zoom. Added the actual archival satellite context map beneath them; user can move location marker.
- Replaced geometric solar shadow drawings with (1) historical Sentinel-2 imagery for location and (2) calculated sun elevation, azimuth, and unobstructed shadow length driven by date/time/coordinates/height. Optional regional shortwave radiation request uses the Open-Meteo forecast API.
- Replaced synthetic blue flood polygon with a real location map and separately calculated rainfall-runoff volumes. Optional next-day modeled rain from Open-Meteo can populate the scenario. Clearly not a flood-depth prediction.
- Replaced simplistic X-ray house line art with a realistic house reference and numeric conduction/glazing calculations. The source image is illustrative and not thermography.
- Added actual satellite basemap options to AQI and Temperature maps and a satellite viewer under City Intelligence, with explicit city model readings kept distinct from pixels.
- Replaced the navigation's energy emoji with a simple inline SVG lightning symbol.
- Kept local project saving and documented example cost assumptions. Retained the marketplace's independently sourced public business contacts; they are not partnerships.
- Removed dead unshipped simulator JavaScript for outdated demos. Existing Node regression suite and new science checks pass.

## Satellite sources and commercial considerations

- **EOX Cloudless 2016:** historical Sentinel-2 RGB composite, ~10 m imagery, CC BY 4.0, openly licensed for commercial embedded apps with proper attribution. Tiles are provided as-is without uptime SLA. This is **not current 2026 imagery**, a surface-temperature layer, or precise building footprint survey. Source: https://cloudless.eox.at/documentation/faq and https://qms.nextgis.com/geoservices/2173 .
- **NASA GIBS VIIRS SNPP true color:** optional near-recent daily observations (~300 m resolution in Web Mercator), with clouds/patchy coverage. NASA requests acknowledgement of GIBS. Satellite RGB data must not be treated as LST or roof temperature. Source: https://nasa-gibs.github.io/gibs-api-docs/ and https://nasa-gibs.github.io/gibs-api-docs/access-advanced-topics/ .
- **OpenStreetMap:** alternative street map, with visible attribution; obey public tile-server usage limits. Commercial traffic may require approved tile hosting.
- **Leaflet JS:** currently fetched on demand from unpkg CDN, requires internet during public use. For commercial scale, self-host pinned assets and obey individual service usage policies.

## What is NOT done / is NOT claimed

1. Accurate 3D reconstruction of a real uploaded house, high-res photogrammetry or precise placement of improvements on an uploaded photograph. Uploaded images remain local session previews; effects are hidden for them.
2. Measured rooftop/indoor temperatures, certified building-energy predictions, live local thermography or accurate flooding risk.
3. Laboratory calibration or field validation of roof impact/heat-gain assumptions; example unit costs are not vendor quotes.
4. Cloud project sync, database accounts, active contractor partnerships, real payment/quotations/commissions.
5. Live external satellite/CDN/API smoke-testing inside this restricted execution environment, or complete cross-browser visual tests; deploy to a staging GoDaddy URL and check before any judging/demo.

## Next validation steps on hosting

1. Confirm EOX Sentinel-2 layer, NASA VIIRS and OSM tiles load and attribution displays; choose the right license for commercial scale.
2. Test desktop and mobile click/zoom/slider/keyboard/touch, selected house change, and roof/shade/tree interactions.
3. Check the date/time and latitude/longitude in Solar & Shadow against an independent solar calculator; spot-check shadow length.
4. Run rain forecast, AQI model and weather fallback on a real domain; verify timestamp labels and error states.
5. Validate reference-photo treatment against actual installation photos and adjust house-specific masks; never market this as an accurate edit of a user's photograph.
6. Replace sample pricing with verified supplier quotes and agree methodology checks with building professionals.
7. Test on a phone, keyboard/screen reader, Chrome/Firefox/Safari and slower data connection; continue Lighthouse/axe QA.

This is an upgrade to a **screening and planning product**, not a certified or fully operational commercial service.

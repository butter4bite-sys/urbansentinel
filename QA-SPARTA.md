# Urban Sentinel SPARTA QA — 11 November 2026

## Automated checks

- Original `npm test` suites pass: core application, modules, temperature map, AQI map, weather fallback and Urban Sentinel 4.0 scenarios.
- New scientific regression tests pass: sun elevation at Pune equinox, east/west solar azimuth progression, shadow length with sun angle, satellite source attribution.
- JavaScript syntax checked with Node `--check`.
- All site-owned local resource links checked with a static HTML scan; removed irrelevant features not in the Climate Lab menu.

## Important limitation

Full browser visual verification could NOT be completed from this environment. Headless Chromium navigation to local and synthetic test hosts returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Therefore we **do not certify** mobile visuals, CDN satellite tiles or external forecast APIs as live-tested. Do a real staging deployment QA pass before judging.

## Scientific integrity

- Optical satellites provide geographic context, not exact roof/indoor temperature or flooding depth.
- Photographic overlays are creative previews only and are not high-fidelity image editing.
- Shadow angle is calculated from location/date/time; building height is an input. Shadow length assumes unobstructed level ground.
- User-entered and modelled weather/radiation are clearly distinguished.
- Existing roof estimates are still screening models with unvalidated reflectance/shade factors.

## Final release audit

- HTML relative asset/link references: **198 checked; none broken**.
- Local JavaScript ES module imports: **66 checked; none broken**.
- All local JavaScript modules: passed `node --check`.
- PHP scripts: passed `php -l` for all 7 PHP files.
- `npm test`: **all 7 test suites passing**.
- Satellite tiles, photographic layouts, touch interactions and external API behavior still require live staging verification.

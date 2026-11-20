# Urban Sentinel 4.0 — Model Methodology and Limitations

All new calculators are explainable **screening approximations**. None is a building energy certification, indoor air temperature prediction, flood modeling service, or verified solar installation quotation.

## Roof Before vs After

Assumed incident irradiance: 800 W/m² under a deliberately simplified peak-sun scenario, not fetched live for a particular location/time. Roof length × width gives assumed rectangular roof area (m²). Default reflectance assumptions are concrete 0.24, metal 0.34 and tile 0.35. Selected reflective coating is assumed reflectance 0.67; shade is assumed 20% of applicable roof area, and trees another 8%. These fractions are generic scenarios, **not material certification or site measurements**.

`P_absorbed_kW = roof_area_m² × irradiance_W/m² × (1 − roof_reflectance) × (1 − shade_fraction) / 1000`.

Baseline is calculated without new changes; After uses selected changes. Combined changes reduce absorbed solar radiation multiplicatively (not adding percentage reductions). **This metric is peak modelled incident power absorbed at roof exterior, not indoor heat transfer, comfort, electricity saving or surface temperature.** The model omits roof heat capacity, thermal bridges, internal gains, solar angle, weather, wind, coating ageing and envelope performance. Ventilation and insulation do not change this exterior absorption figure; their potential benefits are described qualitatively.

Indicative cost *allowances* (not supplier prices): reflective coating ₹240/m²; external shade at 16% roof area × ₹900/m²; ventilation allowance ₹12,000; insulation ₹850/m²; landscaping four trees × ₹2,500. These are adjustable in source code but should be replaced with project-specific quotes before financial decisions. Currency values are illustrative and not real current market quotes.

## Electricity Bill Detective

`Appliance_kWh = average_appliance_power_kW × operating_hours × operating_days`.

Fan/AC estimates are added to a user-entered estimate for other appliances. The app compares that total with monthly billed units, showing the unexplained difference without assuming meter-level instrumentation. `energy_cost = units × user_entered_effective_rate`; excludes fixed charges, taxes, multiple slab tariffs, minimum charges and seasonal price changes. Actual appliance efficiency and inverter duty cycles differ.

## Solar feasibility

`annual_generation_kWh = installed_capacity_kW × peak_sun_hours_per_day × 365 × performance_ratio`.

Potential bill-offset kWh is capped by user-entered annual consumption. Annual budgetary saving uses user-entered effective tariff. Simple payback uses user-entered installation allowance minus a user-entered **confirmed** subsidy (default zero), divided by estimated savings. This ignores export tariffs, net metering, tariff structure, cash-flow timing, maintenance, financing, soiling, degradation, shading, structural safety and legal/regulatory requirements. The optional 10m²/kW footprint is a rough area screening assumption, not a structural or layout design.

## Rainwater collection

`annual_liters = roof_catchment_area_m² × annual_rainfall_mm × collection_efficiency`.

1 mm rainfall over 1 m² yields 1 L before losses. Equivalent days of intended usage = annual liters / user-entered daily demand, **not** a prediction of actual yearly water availability. It does not represent rainwater safety, seasonal rain distribution, storage yield, first-flush losses, tank overflow, filtration, groundwater recharge suitability or regulatory approvals.

## Weather & AQI

Existing Weather/AQI services request current modelled values via external providers. Time, source and cached/stale status must be shown; no made-up values during outages. US AQI is explicitly labeled, not relabeled as Indian NAQI. No rooftop or street-level surface temperature is inferred from standard air-temperature readings.

## Verification before field deployment

1. Collect measured roof material reflectance, building geometry, representative solar/weather conditions and temperatures.
2. Compare outputs with qualified engineering methods and real measured projects.
3. Publish validation error ranges and supported scope of scenarios before advertising performance predictions.
4. Replace generic unit costs with properly sourced quotations that include warranties, regional labor and taxes.

## SPARTA Phase 2 — added location-aware analysis (11 November 2026)

- **Solar site context:** `assets/js/solar-science.js` uses approximate NOAA-style solar declination/equation-of-time calculations. Entered local time is **IST**, longitude and latitude from manually selected map coordinates or a city geocoder. Solar azimuth is degrees clockwise from north; solar elevation is angle above horizon. For a simple vertical object of height `h`, flat-ground shadow length is `h / tan(elevation)` if the sun is above the horizon. No obstruction, terrain or 3D roof/adjacent-building geometry is modelled; the map cannot show a real cast-shadow footprint.
- **Optional irradiance:** The Before/After Studio and Solar & Shadow page can request regional, **modelled** Open-Meteo hourly shortwave solar radiation for location/date/time. The Studio otherwise explicitly uses the existing `800 W/m²` illustrated peak-day assumption. Irradiance is not measured rooftop flux or roof temperature. Nighttime radiation may be zero.
- **Rainfall runoff:** The Flood Scenario Lab no longer draws a fictional flood-depth polygon. It estimates gross runoff volume from user-set rain event depth, user-set area and an assumed weighted coefficient (`0.9 × impervious_fraction + 0.2 × permeable_fraction`). It subtracts entered retention and additional infiltration, capping remaining volume at zero. The optional next-day Open-Meteo precipitation value is a **24-hour model forecast**, not a peak storm intensity, inlet capacity or inundation forecast.
- **Cinematic house reference:** Generated reference images approximate 4 property styles. Clickable roof/shading/tree overlays provide an interactive visualization, but masking follows approximate reference image regions. Photograph pixels never enter the numeric model. User-uploaded house photos are preview only and receive no falsely aligned edits.
- **City satellite:** The archived Sentinel-2 2016 RGB layer and optional recent (~300 m) NASA VIIRS RGB observation are distinct from the Open-Meteo modeled air temperature and CAMS US AQI marker readings. No land-surface-temperature raster is generated or represented as a city thermal map.

The previous methodology statement that solar irradiance is *always* a fixed design input should therefore be read as its **fallback** behavior. It can now be replaced by a date/location-specific model request when available; calibration and scientific verification are still outstanding.

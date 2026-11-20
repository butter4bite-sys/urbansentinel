# Scientific Transparency for Competition Judges

## What can be calculated

**Roof solar absorption (illustrative instantaneous power):**

`absorbed kW = roof area (m²) × solar irradiance (W/m²) × (1 − reflectance) × (1 − shade fraction) / 1000`

The model assumes the roof surface receives the chosen irradiance, applies a material reflectance allowance, and gives a rough **relative power absorbed by the roof surface**. The figure is not the heat transmitted to a room, not a satellite thermal image and not an indoor temperature.

**Relative heat/comfort screening index:** A bounded 0–100 relative score adjusts with user-entered roof and ventilation options, AC count, fans, openings and shading. Its coefficients are deliberately simplified for scenario demonstration; it is **not calibrated against measured buildings**. A change of ten index points is not a change of ten °C.

**Ventilation index:** A qualitative 0–100 ranking derived from wind-direction, opening orientation, vent availability and selected wind speed. The animated arrows are explanatory vectors, not a computational fluid dynamics field. Openings that do not face appropriate wind directions limit cross-flow.

**Appliance electricity:** Estimates `kWh = quantity × average kW × hours used`; monthly fan/lighting and fridge use follow declared usage assumptions. Replacing roof treatment does not by itself generate a claimed kWh saving. Fans improve perceived comfort but cannot directly cool dry-bulb air.

**Costs:** Planning allowances, not supplier invoices. The marketplace displays public contact channels and allows requests only after business agreement approval.

## Key integrity rules

1. Observations, forecasts, assumed inputs and modeled outputs must have distinct labels.
2. “Before” and “After” must share a house geometry and camera angle; neither is a measured as-built reconstruction.
3. Do not advertise numerical cooling degrees or bills saved from these screening outputs.
4. Provider listings are not contracts; verified identity and confirmed referral agreement are separate owner checks.
5. In operational use, weather/API licenses, final supplier quotes, hardware performance and client consent need independent review.

The site includes a longer `MODEL-METHODOLOGY.md` describing legacy and current calculation assumptions. The current 3D Simulation deliberately prioritizes explainable **screening outputs** over invented engineering precision.

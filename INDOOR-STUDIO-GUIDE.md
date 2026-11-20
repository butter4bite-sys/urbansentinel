# Urban Sentinel — Indoor Property Studio (November 2026)

This release updates the existing climate-house module only. All AQI/Temperature Maps, energy calculators, Solutions Marketplace, referral-tracking backend, and owner/contractor access remain included.

## New controls

1. Open **Climate Lab → Digital Twin**, **Before vs After**, or **X-Ray Your House**. These now use the same property model and browser-saved appliance data.
2. Set **Room length**, **Room width**, **Ceiling height**, **house type**, and **floors**. The exterior shell is scaled in real metres. **One model world unit = one metre.** The roof/camera adjusts to the entered building footprint.
3. Press **Open roof** for overhead AC/fan/LED/fridge positioning. Individual LED ceiling fixtures and multiple refrigerator cabinets have visible 3D representations.
4. Use **Zoom + / −** on desktop or mobile. Drag to orbit; pinch also changes zoom on touchscreen devices.
5. Press **Indoor** beside Zoom to enter a first-person view. Move using W/A/S/D or arrow keys on desktop, or hold the overlay arrows on mobile. Drag to look around. Use **Exit Indoor** or press the same Indoor button to return outside. The walking-person HUD animates while moving.
6. Choose **Place AC / fan / LED / refrigerator** from the side panel, then tap **Place selected here** (or the mobile **+ Add** overlay) to add that appliance near the viewing direction. A tap on the canvas can also place it. Each action increases its count and updates the shared electricity model.
7. Choose **Thermal view** to inspect a **screening-level illustrative** relative heat layer. **Architectural** removes heat tint, and **Energy flow** displays conceptual household supply routes. Change sun/shade/AC/fan/insulation assumptions to see estimates update. This is not a certified CFD result or thermographic measurement.
8. Use **Show original house** / **Show improved house** in the side panel to compare on **the same interactive camera**. A separate photographic Before/After block and its satellite map were removed.
9. Use **Save scenario** to store configurations in the current browser and **Energy & Savings** to see appliance consumption using the same counts and assumptions.

## Physical extent and limits

- The configured length and width determine visible shell proportions, 1 m floor grid spacing, wall-hit distances, and first-person movement boundaries.
- Ceiling height controls the indoor wall height and the external storey height. Floors control the external storeys, but this first-person demonstrator opens the *ground-floor conceptual room*, not a fully detailed multistorey house with working stairs.
- Appliance sprites, furniture and internal decoration are illustrative. The website does not infer actual partitions, wall thicknesses, door openings or appliance locations from an external photo. If the owner has not measured those details, they must not be presented as precise.
- Air-conditioner response is from a disclosed simplified planning sensitivity. Fans influence perceived comfort but do not mechanically reduce indoor air temperature. Heat colors and scores are not measured indoor temperatures.
- Data and placed appliance coordinates are saved locally in browser storage. Cloud sync is not implemented in this package.
- Do not present the model as an engineering certification, actual thermography or a contractor quotation.

## Installation

Extract the **contents** of the ZIP directly into `C:\xampp\htdocs\urban-sentinel\` (or GoDaddy `public_html`), keeping the `backend` and `assets` directories. Visit `http://localhost/urban-sentinel/digital-twin.html` in XAMPP.

The owner/contractor portal is unchanged. Its one-time PHP setup still requires the separate private installation key; do not upload the private key to the public website. For a public launch, replace the demonstration passwords previously shared in chat.

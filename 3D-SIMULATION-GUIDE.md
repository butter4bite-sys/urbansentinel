# Urban Sentinel — 3D Simulation & Mobile Install Guide

## What changed
- Replaces the **Climate Lab navigation entry** with **3D Simulation**. Its former tool pages redirect to this one workspace; AQI/temperature maps, City Intelligence, savings calculators, marketplace, referrals and owner/contractor login remain.
- **Guided setup** (three steps) asks for a building type and measurements, per-floor window count/direction and openings, then appliance totals and envelope improvements. Select **Generate house** to create the model. This replaces a previous generated layout after confirmation.
- **Manual editor** has categories: Openings, Airflow, Cooling, Heating, Electrical, Envelope, Outside and Furniture. Select the floor and object, choose a wall for windows/vents, then **Add now** or **Place on model**. Undo or remove individual objects.
- **Floor controls**: use **Edit floor** over the model. In **Indoor**, use **↑ Floor** and **↓ Floor** to change storeys; object positions and window apertures are specific to the selected floor. You can adjust equipment counts per floor, while Energy & Savings uses building totals.
- **Scale**: 1 model unit = 1 metre. Room length, width and ceiling height change the geometry and Indoor walk boundaries. Exterior is a conceptual architectural visualization; 3D Indoor uses WebGL if supported, otherwise a simpler compatibility walkthrough.
- **Start simulation**: activates animated illustrative wind paths, relative heat colors and screening indices. Try changing windows, reflective roof, ACs, shading or wind direction, then compare the same house in Original vs Improved mode. **Stop simulation** returns to the design view.
- **Cooling Planner data**: Property Assessment shares the same saved city, floor footprint (square feet ↔ metres), roof material, window direction and ventilation. 3D Simulation shares appliance quantities with Electricity Bill Detective. This uses browser local storage, so changing device does not sync data.

## Desktop and phone controls
- Outside: drag to orbit, pinch or use **− / +** to zoom. Select a floor to arrange its features.
- Indoor: **W/A/S/D** to walk, drag to look, on-screen arrows for touch devices, **↑ Floor / ↓ Floor** to navigate levels. Choose the desired object from the manual editor and use **Place selected here** to add it while walking. **Exit Indoor** to return to the exterior.
- Generated doors, windows and vents are visual, editable objects. Any true natural ventilation analysis would require much more building geometry and weather information.

## Environmental model boundaries
This is a **comparative educational screening model**, not a measured roof temperature, CFD airflow solver, validated indoor-temperature predictor, BIM floor plan or licensed engineering design. Heat color and wind particles visualize assumptions. Fans improve perceived comfort but **do not lower dry-bulb room air temperature**. All costs, measurements and environmental data should be independently checked before investment.

## Mobile app-style installation (PWA)
- Deploy to a **public HTTPS website**; `http://localhost` works for local testing but cannot be opened from another person's phone.
- Android/Chrome: visitors may get **Install Urban Sentinel** prompt. If Chrome's native prompt is unavailable, use Chrome menu **Install app** or **Add to Home screen**.
- iPhone/Safari: tap Share → **Add to Home Screen**. iOS uses this manual method and does not offer the same automatic install prompt.
- This creates a home-screen app experience, **not an APK or App Store binary**. A static shell may be available offline after visiting; external weather/AQI, map tiles, business referrals, owner login and services still require internet. Private referral APIs and customer/contact pages are excluded from the service-worker cache.
- A dismissed install invitation is suppressed for 14 days in that browser. Display is suppressed inside standalone mode.

## Updating XAMPP or GoDaddy
1. **Back up the complete existing site** and especially any private referral storage, configuration and setup data. Preserve `backend/data` and any private configuration.
2. Extract the ZIP **contents (not the containing folder)** into `C:\xampp\htdocs\urban-sentinel\` or your hosting `public_html` site root.
3. Open `http://localhost/urban-sentinel/3d-simulation.html`, or your HTTPS website.
4. Existing private owner/business setup may remain valid if the private backend storage has not been overwritten. **Do not run one-time installation again just because you updated frontend files.**
5. On your deployed server test 3D Indoor rendering, all mobile controls, correct floor switching, Start simulation and data synchronization; verify PWA install eligibility and HTTPS before inviting users.

## Unchanged systems
The site includes its existing PHP owner and contractor referral interface. The 3D Simulation update does not create new providers, partnerships or real-world validation. Live data remains subject to the original API sources and their terms.

## Pune contractor shortlist continuity
The Owner Dashboard includes the previously requested **Import 8 Pune prospects** action from the latest available contractor edition. Those listings import as unverified, with referrals disabled until independently checked and approved by the website owner. This update does not assert their consent or change existing referrals.

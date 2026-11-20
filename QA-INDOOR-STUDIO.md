# Indoor Property Studio QA — November 14, 2026

## Code tests

- **10/10 automated Node test suites passing** via `npm test`, including original city maps, weather fallback, property/energy data, referral backend wiring, and new movement/metric scale tests.
- JavaScript syntax checked for changed renderer modules.
- Dimension unit tests cover 18 × 6 m room, ray/wall distances, collisions, appliance placement entry points and retained shared pages.

## Headless Chromium visual fixture

Due to this runtime's restrictions on direct browser navigation to local HTTP/file URLs, a self-contained `about:blank` HTML fixture with an import map was used to execute the **actual house studio JavaScript and CSS**, while simulating localStorage. This is not a full XAMPP/GoDaddy browser deployment test.

- **Desktop:** House renderer draws without page errors. Changing length from 12 m to 18 m and width from 9 m to 6 m updates stage title and dimension-based geometry; Indoor switches on and off; refrigerator and LED addition report valid positions; keyboard walking runs.
- **Mobile (390 px):** Stage renders, zoom/Indoor controls are accessible, the onscreen directional controller moves the location indicator, and document width stays at the device width (no horizontal overflow in the scoped fixture).
- The separate photographic comparison widget no longer loads on Digital Twin or Before/After routes.

## Verification still required after staging deployment

- Verify the entire site's navigation, banners and canvas controls together on a real Android and iOS browser. The visual fixture does not exercise external weather/AQI APIs or the real PHP portal.
- Verify pinch interactions on physical touch devices; simulated Chromium mouse/touch tests are not a substitute for hardware.
- Verify PHP owner/contractor portal installation, referral persistence and email behavior on the target XAMPP/GoDaddy host. The previously implemented referral flows were intentionally not modified.

## Scientific limitation

Geometry and navigation use metres, but architectural furnishings are symbolic and the heat model is screening-level. Measured room temperature, thermal imagery, engineering design, exact energy savings and precise 3D reconstruction are **not** claimed.

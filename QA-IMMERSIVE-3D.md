# Immersive 3D Quality Report

**Included tests:** `npm test` runs the existing ten website regression suites and the new `immersive-room-regression.mjs` contract test. The new test uses a simulated WebGL API to assert that the renderer creates a true triangle mesh, issues a draw call, changes geometry when metric dimensions change, adds geometry for additional appliances, and enters/exits correctly.

**Browser fixture:** `python tests/indoor-visual-harness.py` checks the full site module integration in headless Chromium, room edits, first-person entry/exit, appliance placement and mobile layout. In this environment, headless Chromium does **not** expose WebGL; the browser fixture therefore exercises the Canvas fallback and module wiring, **not** the hardware-rendered WebGL scene.

**Release status:** Code-level and fallback regression verified; WebGL render quality, full GPU browser behavior and phone performance require staging tests on a WebGL-enabled device before any competition presentation. Test desktop Chrome, Android Chrome and iPhone Safari. Ensure that an unavailable GPU takes users to the working fallback.

**Known conceptual limitations:** Generic furnishing, no multiroom level navigation, no measured construction drawings, no actual thermographic camera, no VR-headset support.

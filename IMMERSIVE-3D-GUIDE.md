# Urban Sentinel — Immersive Indoor 3D Studio

### Objective
Upgrade the existing Indoor button to a real browser-rendered 3D room with visible modern architectural furnishings, not a flat 2D/2.5D perspective diagram. Inspiration: the life-size architectural walk-through approach illustrated by Arc & Sphere (https://www.arcnsphere.com/ar-vr-architectural-experience). This is an original conceptual visualization, not their proprietary demo or assets.

### Enter the room
1. Go to Climate Lab → Digital Twin (or X-Ray / Before and After).
2. Enter **room length, width and ceiling height**. World geometry follows a **1 world-unit = 1 metre** convention.
3. Press **Indoor** (beside Zoom). The new self-contained WebGL renderer displays a furnished 3D room with floor, walls, framed windows, glass entry, sofa, rug, coffee table, entertainment wall, kitchen cabinets, plants, ceiling fans, LED fixtures, refrigerators and AC units.
4. **Desktop:** W/A/S/D or arrows to walk, drag to turn/look, Zoom + / − to narrow/widen field of view, Escape or Exit Indoor to leave.
5. **Mobile:** Swipe to look, hold the on-screen arrow buttons to walk and rotate, use Zoom + / −, use Exit Indoor to leave.
6. Select the appliance type from the left and tap **Place selected here** inside the room to add it; quantities immediately sync with Electricity Bill Detective.
7. Switch Architectural / Thermal / Energy Flow views. Thermal view tints the visualisation according to the *screening model*, not an actual thermographic image.
8. Original / Improved modes reuse the same house geometry and saved measurement profile.

### Technical architecture
`assets/js/immersive-room.js` is a small custom self-contained WebGL 1 renderer; it does **not** fetch third-party JavaScript or assets. Furniture and appliances are drawn as true triangle meshes in 3D coordinates, with material shaders, perspective camera, depth testing and directional lighting. The app still provides its previous Canvas 2D indoor view as a fallback on browsers without WebGL. A live 3D model is distinct from a certified architectural scan.

### Key limitations
- The property is a conceptual open-plan *ground-floor room envelope*, not a detailed multi-room measured property, staircase or collision-validated building information model.
- The house type determines the exterior concept; interiors are generic staged rooms, not real-world measured layouts. A VR headset mode is not implemented.
- Material, sunlight and thermal presentation is illustrative. There is no actual infrared thermal scan, CFD airflow model or engineering-grade indoor cooling prediction.
- Room length/width/height and counted appliances are shared, but partitions and furnishings are not automatically inferred from a building photograph.
- Projects remain in browser local storage; server referrals/owner dashboard are separate and unchanged.

### Install
Extract ZIP *contents* directly into `C:\xampp\htdocs\urban-sentinel\` or GoDaddy `public_html`, preserving both `assets` and `backend`. Your server must serve the `.js` module files correctly. Backup existing private referral data before overwriting any installation.

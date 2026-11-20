**2026-11-18 deployment note:** This build's main navigation has **3D Simulation**, not Climate Lab. The guided multistorey editor is `3d-simulation.html`. Preserve the existing private `backend/data` and server-managed setup files during upgrade. The new PWA install prompt requires HTTPS on public hosting; see `3D-SIMULATION-GUIDE.md`.

# Urban Sentinel 4.0 — GoDaddy Deployment

## Static platform features

1. Confirm your GoDaddy **hosting** plan (not merely a purchased domain) supports hosting site files. For optional OAuth/feedback, use PHP 8.1+, sessions, cURL, HTTPS and outbound HTTPS access.
2. Extract the ZIP and upload its **contents** (including `index.html`, `auth/`, `assets/`) into `public_html/` using File Manager or SFTP. Avoid uploading a folder inside `public_html` unless you intend a subdirectory deployment.
3. Enable HTTPS and open your domain. Verify home, the primary `3d-simulation.html` tab, guided floor plan creation, Apply saved Cooling Plan, Original / Improved comparison, energy/water, City Intelligence, Marketplace, owner/contractor access, My Projects, and mobile layouts.
4. Check JavaScript console, navigation, image loads, map tiles, weather/AQI sources, stale-data labels, report printing and local project saving. These depend on your live browser, network and hosting environment.

## Historical Google OAuth files (not active in the public user journey)

1. Create a Google Cloud OAuth client of type **Web application**. Configure consent screen and allowed testing users.
2. Set the exact authorized redirect URI `https://YOURDOMAIN/auth/google-callback.php` (adjust for your subdirectory).
3. Set `URBAN_GOOGLE_CLIENT_ID`, `URBAN_GOOGLE_CLIENT_SECRET`, `URBAN_GOOGLE_REDIRECT_URI` as hosting environment variables, or edit `auth/config.php` securely **on the server**. Never publish secrets or include them in frontend JavaScript or distributable ZIPs.
4. Check `auth/config.php`, `auth/.htaccess`, `auth/google-start.php`, `auth/google-callback.php`, `auth/me.php` and `auth/logout.php` on the deployed server. Confirm HTTPS, cURL and session cookies work.
5. The current website does not require customer sign-in. The following older Google-auth instructions are historical and should **not** be activated for the competition build unless a separate decision is made. This flow authenticates a Google identity and session **only**. It does not yet implement a MySQL project database or cross-device synchronization. Projects remain browser-local until server-side storage and user-level access control are added.

## Feedback email (optional)

Configure `URBAN_FEEDBACK_EMAIL` and verify `feedback-submit.php` works with your host's outgoing mail policy. If mail delivery is not configured, the website must report the error rather than claiming feedback was delivered.

## Marketplace and business rules

- All core tools are free. The former subscriptions and demo access switch have been removed.
- The marketplace contains independent public listings and a server-side referral system **only for owner-approved, explicitly contracted partners**. There is no payment collection, and listing a business alone never implies a signed partnership. The owner can import/refresh nine named Pune listings and approve their identity and agreement individually.
- The success-commission dashboard is **illustrative** until genuine agreements exist. Customer consent and a server-side lead ID are implemented for approved providers; fraud/dispute controls, verification evidence, invoicing and actual payment arrangements still need operational validation. Never assume a business has agreed to a commission merely because it appears in the directory.
- Reverify every provider's phone/email/coverage before a public launch and periodically thereafter.

## Reliability, privacy and compliance

- Solar, water and building comparison calculations are **screening estimates**, not energy audits, certified engineering calculations, health guarantees or street-level forecasts.
- Property photos are local session previews. Saved scenarios and bill history are browser-local; users should export a backup.
- Before commercial use, confirm third-party weather/AQI/map licensing, update the privacy notice with actual operator identity/contact and hosting details, add an appropriate consent and retention policy, and conduct a security review.

## QA before launch

Run `npm test`. Also use real desktop/mobile browsers on HTTPS hosting to test keyboard input, screenshots, comparison controls, state persistence, provider links, API failures and Google OAuth with live test credentials. Static regression tests alone do not prove live runtime functionality.


## SPARTA satellite map verification (added 11 November 2026)

- Make sure external Leaflet, historical EOX Cloudless 2016, optional NASA GIBS VIIRS and OSM are reachable on the public HTTPS domain. The site supplies an OSM fallback when satellite tiles repeatedly fail, but public services do not promise continuous availability.
- EOX Cloudless **2016** is CC BY 4.0 and accepts commercial embedded use with legible attribution; later EOX years are not freely licensed for a commercial marketplace. The historical layer **must not** be described as a current-2026 map.
- NASA VIIRS near-recent satellite imagery can be coarse (~300m), cloud covered and incomplete. It is an imagery overlay, never a street-level thermal or flood map.
- Existing temperature/AQI values come from weather/air-quality models independent of imagery, so labels must stay clearly separated.
- The Planning Assistant is now local rule-based only. It does not require a Netlify function, Gemini secret or AI quota. Any old Netlify chat endpoint must not be deployed.
- Test `digital-twin.html`, `before-after.html`, `solar-shadow.html`, `flood-lab.html`, `temperature.html`, `aqi.html` and `city-intelligence.html` on both desktop and mobile in staging before the judges' demo.


## Referral portal installation (new)

After deploying the website, visit `/backend/setup.php` and enter the *separate private installation key* and owner/business passwords. The PHP account must be able to create private data files above `public_html`. Once installed, `/access.html` opens the private owner/contractor portal. Never upload the private key file to `public_html`. See `REFERRAL-SETUP.md`.


## 19 November 2026 judges-ready update

See `JUDGE-DEMO-WALKTHROUGH.md`, `JUDGE-MODEL-BOUNDARIES.md`, and `MARKETPLACE-CONTRACTOR-STATUS.md`. Original and Improved share the same 3D scene; Cooling Planner recommendations are saved and applied only after the user presses **Apply saved Cooling Plan**. Costs and environmental indices are planning-only. Existing users must use the Owner Dashboard import/refresh action to synchronize named Pune directory entries without discarding private referrals.

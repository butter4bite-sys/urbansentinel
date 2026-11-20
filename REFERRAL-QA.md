# Referral Portal QA — 12 November 2026

## Backend integration test (PHP built-in server; local HTTP only)

**Passed:** one-time setup with separately supplied installation key; generated PHP password hashes; public provider directory; Diligent seeded but not owner-verified; customer consent form; random referral ID; owner/business login; contractor-specific lead access; status updates; contractor forbidden from owner commission confirmation; owner confirmation and 10% illustrative amount calculation; creation of a second contractor login for a second business; contractor isolation from another business's leads; invalid CSRF rejected; no password hashes in public directory API.

**Passed:** eight existing original website Node regression suites: navigation, temperature, AQI, weather fallback, climate model calculations, connected household energy and solar science. PHP syntax, JS syntax and local internal links were also checked.

**Not verified:** fully rendered desktop/mobile layouts in Chromium. This execution environment blocked Chromium from navigating to localhost even though Python HTTP requests reached the PHP server. Test visually after deployment to XAMPP/GoDaddy. No live SMS/email was tested or implemented, no real contractor agreement or service follow-up was verified, and no payment gateway/commission transfer exists.

## Important security/production cautions

- The user-provided demonstration account passwords were shared in chat; change them before public hosting.
- Passwords are not stored in the shipped ZIP or browser JavaScript. They are entered once at the installer and hashed using PHP `password_hash`.
- Keep the separate setup key out of all public website folders.
- HTTPS, contractor consent, an actual privacy contact and retention schedule are essential before accepting real customer information.
- The storage layer is file-backed, outside web document root. This is suitable for a small demo, not an audited high-volume CRM. Set up independent backups and migrate to a database before scale.
- A referral ID is evidence of an enquiry only, not proof of a completed installation. Final commissions require owner confirmation; enforce agreements independently.
- The 'Verified contractors' section lists businesses flagged by the owner after verification; it does not pretend that a public business directory is an active partnership.

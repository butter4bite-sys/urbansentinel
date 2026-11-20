# Urban Sentinel — referral tracking / owner portal

This package preserves the existing Urban Sentinel site, and adds a **PHP 8+ private referral management backend**. There is no customer sign-in, no subscription gating, and no Google OAuth dependency.

## What works

- Customer selects an enabled provider and submits a consent-based callback request.
- Unique random referral ID `US-YYYY-########`, timestamp, provider and service are stored in private server data files.
- Contractor account sees only enquiries assigned to that contractor.
- Contractor can mark New / Contacted / Quotation Sent / Work Started / Completed / Cancelled and report an agreed project value.
- Owner can add/edit/archive businesses, flag identity/partnership as owner-verified, enable/disable referrals, set agreed commission percentages and create separate contractor logins.
- Owner confirms completion and final project amount before the commission figure appears as confirmed.
- Owner can delete customer referral records and users can update passwords.

**No automatic emails, SMS, payment gateway, invoicing, contractor agreements or legally binding commission collection are included.** Referral IDs prove that the site received an enquiry; they do not prove work took place.

## Install on XAMPP / GoDaddy

1. Extract ZIP **contents** into `C:\xampp\htdocs\urban-sentinel\` (or GoDaddy `public_html/`), so `index.html` is at the root of the chosen site folder. Start Apache/PHP.
2. **Keep the separate `URBAN_SENTINEL_PRIVATE_SETUP_KEY.txt` offline. Never upload it into the public website.**
3. Open `http://localhost/urban-sentinel/backend/setup.php` on XAMPP, or `https://YOURDOMAIN/backend/setup.php` on HTTPS hosting. If you uploaded to a subdirectory, include it in the URL.
4. Enter the private installation key and configure `owner` and `business` passwords. For the requested demonstration use the passwords you supplied, but **change them before public launch** because they were shared in a chat. They are hashed on the server and are not embedded in JavaScript or the website ZIP.
5. The installer runs only once. Open `access.html` for owner/contractor access. The first `business` login is assigned to the Diligent Enterprises test listing.
6. The server must be permitted to create a private directory **outside the web document root**. For GoDaddy if this fails, ask hosting support to allow the PHP user to write inside your home directory (above `public_html`). Do not place private referral files in `public_html`.
7. Verify your site loads at the correct folder path. For local tests, you also need PHP; double-clicking `index.html` is not enough for referrals.
8. Before accepting real enquiries, set HTTPS, publish privacy contact + retention policy, confirm contractor consent to receiving leads, independently verify each approved contractor, and agree commission terms in writing.

## Diligent Enterprises and test number

The business seed listing uses **Diligent Enterprises, Chougule Mala, near Shivarkar Garden, Wanowrie, Pune, 411040**, phone **+91 98508 99159** from public business records (see source link in listing). It is **not marked verified or contracted** until the owner completes verification. There are similarly named businesses in other places; confirm identity before launch. For demonstration, callback enquiries can be recorded and viewed by the `business` login; they are not automatically sent to that phone number.

**7721005552** is displayed in a separate **Test contact number** box and is never described as Diligent's business contact.

## Business security model

The single sample `business` login sees Diligent enquiries only. Owner can create a different username/password for each additional partner, scoped by partner ID. Never reuse a shared business login for unrelated contractors. All data writes use lock-protected files, passwords use PHP `password_hash`, and APIs enforce role-based authorization and CSRF checks.

## Limitations

This is a low-traffic **file-backed MVP**, not a transactional database or a fully audited CRM. At scale, migrate to MySQL/PostgreSQL with database migrations, backup/restore, immutable audit logs, per-contract agreement evidence, automatic notifications and retention/deletion jobs. The environment did not independently validate real contractors' partnership status.

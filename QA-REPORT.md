# Urban Sentinel 4.0 — QA Summary

Prepared 10 November 2026.

## Checks completed

- `npm test`: **PASS** — original cooling recommendation and PDF generation, saved-project behavior, temperature and AQI parsers/regressions, weather provider fallback/cache, V4 link/navigation and pure-calculator math.
- PHP syntax: **PASS** for the included authentication endpoint scripts and feedback form (`php -l`).
- JavaScript syntax: **PASS** for all `assets/js/*.js` modules (`node --check`).
- Static HTML relative references: **PASS** — 193 local HTML href/src references checked; no missing targets.
- Subscription control: removed from runtime navigation and Climate Lab gating; legacy pricing URL redirects to marketplace.
- Climate Lab: original tools consolidated into a single directory with **Open Tool** links. Challenge/leaderboard removed from the directory and legacy route redirected.
- Before/After model: pure mathematical regression checks cover baseline, reflective roof, shade, combined reduction, and solar/rainfall arithmetic.
- Provider directory: public contact source pages included alongside each provider for rechecking; no fictitious ratings or claimed partnerships.
- No private Google client ID or secret included in `auth/config.php`.

## Not verified in this environment

- Browser-run visual comparisons, mobile device screenshots, keyboard interaction and full end-to-end page interactions: Chromium navigation to file/localhost was blocked by an administrator policy in this execution environment.
- Live third-party API availability from the eventual public domain; free API licensing/rate limits should be confirmed.
- Google OAuth round trip (requires real Cloud credentials and the target HTTPS domain).
- PHP feedback email delivery (requires host mail configuration).
- Real vendor response, contracted referrals, project status, commissions, user payments, database/cloud project sync (not implemented).

## Recommended launch checklist

1. Unzip into GoDaddy `public_html`; load each navigation page on desktop and Android/iOS.
2. Open Climate Lab and launch each tool using its **Open Tool** link; verify no separate simulator sidebar links.
3. In Before/After, change dimensions, toggle reflective roof/shade, switch comparison slider, save and reopen a scenario in My Projects, test Print/Save as PDF.
4. In Energy & Water, change each calculator input and check the formula and units. Save an electricity-bill history entry.
5. In Marketplace, filter categories and click each official business contact source. Confirm that direct email/phone links work on your devices.
6. Test environmental API failure/stale labels and all maps with your intended domain.
7. Configure and test OAuth if sign-in is required; communicate clearly that cloud project sync is not live.
8. Reverify business contact details and service coverage before publishing; arrange agreements before any commission claims.
9. Obtain independent review of estimates before advertising quantified indoor cooling effects.

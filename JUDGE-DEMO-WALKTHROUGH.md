# Urban Sentinel — Competition Demonstration Guide

**Competition:** Senior Group, “Create your own ICT based Innovations & Start-up idea”  
**Selected topic:** **Cool City – Beat the Urban Heat**  
**PPT submission:** 25 November 2026, by 8:00 p.m.  
**Final viva and working model:** 19 December 2026, 9:00 a.m. at KHS.

## Prepare before the judge enters

1. Serve the website using XAMPP/Apache, or use an HTTPS staging deployment on GoDaddy. Verify that `index.html`, `assessment.html`, `3d-simulation.html`, `energy-savings.html`, `marketplace.html` and `access.html` load.
2. Use a recent Chrome/Edge desktop with hardware-accelerated WebGL; have the mobile alternative available. Keep a backup screenshot or recording in case browser graphics or external weather APIs fail.
3. Save any real project data before you use **Load example house**. A demo house and its values are explicitly illustrative.
4. The marketplace needs a PHP-enabled host and one-time owner setup for tracked callback submissions. Before any real customer enquiry, the owner must review provider identity and record actual consent to partnership terms.
5. Do not claim scientifically verified room-temperature reductions, verified energy-bill savings, or signed partnerships unless supported by evidence.

## 4-minute live sequence

| Time | Page and action | What to explain |
|---|---|---|
| 0:00–0:45 | **Cooling Planner / Assess My Property:** enter Pune, home/duplex, realistic floor area and budget. Submit the plan. | The application screens practical solutions against the user's budget and keeps a reusable property profile. |
| 0:45–1:25 | **3D Simulation:** open the tab; use the same profile or choose **Load example house** if no plan exists. Show floor selector and Indoor button. | A single metric-scaled model, separate object placement per floor, and editable windows/vents/appliances. |
| 1:25–2:15 | **Connected cooling plan:** click **Apply saved Cooling Plan** to add eligible roof/shade/ventilation items; choose **Start Simulation**. | The selection drives the same model. Wind and heat overlays are a comparative screening visualization, not full CFD. |
| 2:15–2:55 | **Before vs After:** toggle **Show original house** / **Show improved house**, pointing to the live comparison table. | Consistent camera and geometry. Compare relative heat risk, airflow opportunity, rooftop absorbed solar power, costs and monthly appliance use. Do not call roof kW a temperature measurement. |
| 2:55–3:30 | **Energy & Savings:** show electricity analysis and appliance links; return to 3D floor choice if asked. | The house model and Bill Detective use shared appliance totals, with modeled—not measured—consumption. |
| 3:30–4:00 | **Solutions Marketplace:** explain the commission example calculator and referral ID flow. | Free consumer planning. Only an owner-approved partner with actual agreement can receive tracked callbacks. Commission becomes payable only under agreed completion terms. |

## Questions to anticipate

**Why not just ask ChatGPT?** ChatGPT can advise, but Urban Sentinel provides repeatable structured property inputs, an editable floor-by-floor scenario, one connected numerical comparison, saved planning scenarios and a referral workflow. These product advantages depend on reliable operation, not just descriptive claims.

**Is the heat simulation scientifically accurate?** It is a screening model, not a verified indoor temperature simulation. The roof absorbed-solar estimate uses roof area, irradiation, assumed reflectance and shading. Wind uses an illustrative index based on opening direction and wind. Actual temperatures, HVAC savings and airflow require field data and independent validation.

**How does Urban Sentinel make money?** The customer tools are free. If a provider separately agrees to a commission and a referred installation is verified complete, a contract-defined fee may be due. The site illustrates **5% of ₹50,000 = ₹2,500**; that is not current collected income or a rate accepted by every contractor.

**Are the listed companies your partners?** They are named public-directory entries unless the Owner Dashboard reflects actual verified identity, express agreement and activated referrals. Do not present unapproved listings as official partners.

**Where is the data stored?** House scenarios and energy inputs are browser-local. The private referral backend uses server-side files outside public web root on supported PHP hosting. It is not full multi-device cloud synchronization.

**What if weather or 3D graphics fail?** Weather has source and freshness labels with fallbacks. The illustrative 3D environment has reduced graphics/compatibility behavior, but live real-device testing is still necessary.

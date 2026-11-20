from pathlib import Path
import subprocess,json
root=Path('/mnt/data/urban_sentinel_judges_v1')
p=root/'assets/js/partner-portal.js';s=p.read_text()
s=s.replace("${p.verified?'Verified by owner':'Pending'}${p.archived?' · Archived':''}", "${p.verified&&p.agreement_confirmed?'Confirmed partner':p.verified?'Identity checked · agreement pending':'Public listing · pending'}${p.archived?' · Archived':''}")
s=s.replace("Owner-verified contractor</label><label><input name=\"referral_enabled\"", "Owner has checked business identity</label><label><input name=\"agreement_confirmed\" type=\"checkbox\" ${p?.agreement_confirmed?'checked':''}> I confirm that this business expressly agreed to be listed as an Urban Sentinel partner and accepted the referral terms</label><label><input name=\"referral_enabled\"")
s=s.replace("['verified','referral_enabled','archived']", "['verified','agreement_confirmed','referral_enabled','archived']")
s=s.replace("p?.[name]??'');const text", "p?.[name]??'');const text")
s=s.replace("value=\"${v('commission_percent')||10}\"", "value=\"${p?.commission_percent??0}\"")
s=s.replace("<p class=\"ref-muted\">Add, edit, verify, archive or enable referral requests for businesses.</p>", "<p class=\"ref-muted\">A public listing is not a partnership. Confirm the business identity and written/commercial agreement before enabling tracked callback requests or applying any commission percentage.</p>")
p.write_text(s)
p=root/'backend/setup.php';s=p.read_text();s=s.replace("$businessPartner=$seed[0]['id'];", "$businessPartner=$seed[0]['id'];foreach($seed as $entry)if(($entry['name']??'')==='Diligent Enterprises'){$businessPartner=$entry['id'];break;}")
p.write_text(s)
# Static fallback directory can be shown even without the PHP backend; only public data.
output=subprocess.check_output(['php','-r',"require 'backend/lib.php';echo json_encode(array_slice(us_seed_partners(),0,9),JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);"],cwd=root)
items=json.loads(output)
for i,x in enumerate(items):
 x['id']=f'public-pune-{i+1:02d}'
 x['verified']=False
 x['agreement_confirmed']=False
 x['referral_enabled']=False
 x.pop('commission_percent',None)
data=root/'assets/data';data.mkdir(parents=True,exist_ok=True)
(data/'pune-contractors.json').write_text(json.dumps({'updated':'2026-11-19','notice':'Public directory entries, not confirmed Urban Sentinel partnerships. Contact details should be reconfirmed before use.','providers':items},ensure_ascii=False,indent=2))

p=root/'assets/js/marketplace.js';s=p.read_text()
s=s.replace('let providers=[],filtered=[]', 'const partnerConfirmed=p=>Boolean(p.verified&&p.agreement_confirmed);\nlet providers=[],filtered=[]')
s=s.replace('Search independent public listings and, where referral tracking is enabled, request a callback. <b>Public listings are not automatically verified partners.</b>', 'Find publicly identified Pune contractors and environmental services. A directory listing does not establish an Urban Sentinel partnership. Tracked referrals open only for owner-approved businesses with confirmed agreements.')
s=s.replace('<h2>Verified contractors</h2><p class="us4-mini">Only businesses explicitly approved by the Urban Sentinel owner appear here. A public directory listing alone does not prove a partnership or professional qualifications.</p>', '<h2>Confirmed Urban Sentinel partners</h2><p class="us4-mini">Only businesses whose identity and referral agreement have both been confirmed by the owner appear here. A public directory listing or phone conversation is not by itself a verified partnership.</p>')
s=s.replace("${p.verified?'Owner-verified contractor':'Public listing · verification pending'}", "${partnerConfirmed(p)?'Confirmed Urban Sentinel partner':p.verified?'Identity checked · partner agreement pending':'Public listing · affiliation not confirmed'}")
s=s.replace("${p.referral_enabled&&installed?", "${p.referral_enabled&&partnerConfirmed(p)&&installed?")
s=s.replace("${p.referral_enabled?'<p class=\"us4-mini\">Tracked enquiries are stored in the private dashboard; a callback is not guaranteed.</p>':'<p class=\"us4-mini\">No tracked enquiries for this provider yet; contact the business independently.</p>'}", "${p.referral_enabled&&partnerConfirmed(p)?'<p class=\"us4-mini\">Tracked enquiries are stored in the private dashboard; a callback is not guaranteed.</p>':'<p class=\"us4-mini\">Public contact only. A formal Urban Sentinel partnership has not been established in this listing.</p>'}")
s=s.replace("const yes=filtered.filter(p=>p.verified),rest=filtered.filter(p=>!p.verified);", "const yes=filtered.filter(partnerConfirmed),rest=filtered.filter(p=>!partnerConfirmed(p));")
s=s.replace('No businesses have been approved as verified partners yet. The owner can verify them after confirming business identity and partnership status.', 'No formal partnerships have been approved in this installation. The owner can confirm agreements in the private dashboard.')
s=s.replace("<section class=\"us4-card\"><h2>How referral tracking works</h2>", """<section class="us4-card usjudge-business"><div class="us4-intro"><div><h2>How Urban Sentinel can earn revenue</h2><p>The environmental planning tools are free for customers. An agreed provider commission is proposed only when an actual project referred through the platform is completed and verified.</p></div><span class="us4-tag">Illustrative model · not revenue earned</span></div><div class="usjudge-steps"><div><b>1 · Free assessment</b><span>Customer explores cooling and energy options, no subscription.</span></div><div><b>2 · Consent-based referral</b><span>A participating provider receives a unique referral ID and enquiry.</span></div><div><b>3 · Verified completion</b><span>Contractor reports progress; owner checks completion evidence.</span></div><div><b>4 · Agreed commission</b><span>Commission is recorded according to signed terms; no payment collected by this site.</span></div></div><div class="usjudge-calculator"><label>Illustrative project value (₹)<input type="number" id="usjudge-project-value" min="0" max="100000000" step="1000" value="50000"></label><label>Example commission (%)<input type="number" id="usjudge-rate" min="0" max="100" step=".5" value="5"></label><div><small>Illustrative commission</small><strong id="usjudge-commission">₹2,500</strong></div></div><p class="us4-mini">Example only. No contractor is assumed to have accepted 5%, and this calculation is not a booked or collected payment. Owner confirmation and written terms determine the actual commission.</p></section><section class="us4-card"><h2>How referral tracking works</h2>""")
s=s.replace("document.getElementById('leadForm').addEventListener('submit'", """const calcCommission=()=>{const value=Math.max(0,Math.min(100000000,Number(document.getElementById('usjudge-project-value').value)||0));const rate=Math.max(0,Math.min(100,Number(document.getElementById('usjudge-rate').value)||0));document.getElementById('usjudge-commission').textContent='₹'+Math.round(value*rate/100).toLocaleString('en-IN');};
for(const id of ['usjudge-project-value','usjudge-rate'])document.getElementById(id).addEventListener('input',calcCommission);
document.getElementById('leadForm').addEventListener('submit'""")
s=s.replace("}catch{providers=placeholder;installed=false;document.getElementById('refStatus').textContent='PHP backend unavailable. Referral requests will be enabled after installation.'}", "}catch{try{const r=await fetch('assets/data/pune-contractors.json',{cache:'no-store'});if(!r.ok)throw Error();providers=(await r.json()).providers||placeholder}catch{providers=placeholder}installed=false;document.getElementById('refStatus').textContent='Public listings only. PHP referrals unavailable until server-side setup is completed.'}")
p.write_text(s)

# The About page reinforces an honest investor/judge story without claiming revenue.
p=root/'about.html';s=p.read_text()
insert='''<section class="card"><h2>Startup model · free to plan, verified referrals to execute</h2><p>Urban Sentinel helps homeowners assess heat-related problems, compare illustrative building improvements and contact suitable independent contractors. Customers do not pay a subscription to use the planning tools.</p><p>The proposed income is a <strong>negotiated commission on successfully completed, owner-confirmed referred projects</strong>. For example, a ₹50,000 project at an illustrative 5% agreed rate would mean ₹2,500 commission. This is an example, not a claim of actual revenue or a rate accepted by the businesses in our public directory.</p><p>A partner is presented as confirmed only when the operator has validated business identity and its referral agreement. The website does not process payments.</p><p><a class="btn secondary" href="marketplace.html">View contractor directory and revenue model →</a></p></section>'''
s=s.replace('</main><footer',insert+'</main><footer')
p.write_text(s)

from pathlib import Path
p=Path('/mnt/data/urban_sentinel_judges_v1/assets/js/3d-simulation.js')
s=p.read_text()
s=s.replace("import {KINDS,getDesign,saveDesign,makeObject,autoLayout,placementArrays,floorEnergy,syncEnergyFromDesign,importAppliancesFromEnergy,floorObjects,floorSimulation} from './simulation-design.js';", "import {KINDS,getDesign,saveDesign,makeObject,autoLayout,placementArrays,floorEnergy,syncEnergyFromDesign,importAppliancesFromEnergy,floorObjects,floorSimulation} from './simulation-design.js';\nimport {getCoolingPlan,coolingPlanIssues,compareScenarios,baselineDesign,baselineHome,applyCoolingPlan} from './cooling-bridge.js';")
s=s.replace('<div class="cg-layout"><aside', '''<div class="usjudge-intro" role="region" aria-label="Judge demonstration guide"><div><strong>Competition demonstration · a connected workflow</strong><p>1. Build your property or open the Cooling Planner · 2. Apply suggested measures · 3. Start Simulation · 4. Switch Original / Improved · 5. Review assumptions and connect to providers.</p></div><button type="button" id="cg-demo" class="btn secondary">Load example house</button></div><div class="cg-layout"><aside''')
s=s.replace('<div class="cg-section-title"><span>04</span> Compare &amp; actions</div>', '''<div class="cg-section-title"><span>04</span> Connected cooling plan</div><div class="usjudge-plan"><p id="cg-plan-brief">Checking the latest Cooling Planner result…</p><div class="cg-choices"><button id="cg-apply-plan" class="btn" type="button">Apply saved Cooling Plan</button><a class="btn secondary" href="assessment.html?type=home">Edit Cooling Plan ↗</a></div><p id="cg-plan-message" class="cg-fine" role="status" aria-live="polite"></p></div><div class="cg-section-title"><span>05</span> Compare &amp; actions</div>''')
s=s.replace('<p class="cg-fine" id="cg-compare-status">Both views use the same rotatable building and camera angle.</p>', '''<p class="cg-fine" id="cg-compare-status">Both views use the same rotatable building and camera angle.</p><div id="cg-comparison" class="usjudge-compare" aria-live="polite"><p>Choose Original or Improved to compare.</p></div>''')
s=s.replace('<div class="cg-simulation-panel" id="cg-simulation-panel" hidden>', '''<div class="usjudge-method"><strong>What these results mean</strong><p>Wind arrows represent opportunities from selected window and vent positions, not a CFD simulation. Heat colours and the risk index are illustrative rankings, not thermal-camera readings, indoor thermometer predictions or engineering certification. Roof absorbed solar power is estimated from area × solar irradiance × (1 − roof reflectance) × (1 − shade fraction).</p><details><summary>Read the modelling assumptions</summary><p>Airflow uses an opening-direction screening index. The thermal index is a transparent sensitivity model affected by user-selected appliances and shading. Fans influence comfort but do not cool dry-bulb air. Installation costs from the Cooling Planner are planning allowances, not supplier quotations. These outputs must be checked by an engineer before real building work.</p></details></div><div class="cg-simulation-panel" id="cg-simulation-panel" hidden>''')
s=s.replace("function activeHome(){return beforeMode?{...home,roofCoating:false,roofInsulation:false,shade:15,trees:0}:home}", "function activeHome(){return beforeMode?baselineHome(home):home}\nfunction visualDesign(){return beforeMode?baselineDesign(design):design}")
a=s.index('function buildHouse(){')
b=s.index('function render(){',a)
build=s[a:b]
build=build.replace('floorObjects(design,', 'floorObjects(visualDesign(),').replace('floorSimulation(design,', 'floorSimulation(visualDesign(),')
s=s[:a]+build+s[b:]
s=s.replace("heatIndex:floorSimulation(design,profile,activeHome(),activeFloor).heatScore", "heatIndex:floorSimulation(visualDesign(),profile,activeHome(),activeFloor).heatScore")
s=s.replace("objects:floorObjects(design,activeFloor),floor:activeFloor", "objects:floorObjects(visualDesign(),activeFloor),floor:activeFloor")
s=s.replace("openings:floorObjects(design,activeFloor).filter", "openings:floorObjects(visualDesign(),activeFloor).filter")
s=s.replace("const model=getModel(),breakdown=energyBreakdown(energy),perFloor=floorEnergy(design,activeFloor,energy),sim=floorSimulation(design,profile,activeHome(),activeFloor);", "const model=getModel(),breakdown=energyBreakdown(energy),perFloor=floorEnergy(design,activeFloor,energy),sim=floorSimulation(visualDesign(),profile,activeHome(),activeFloor);")
s=s.replace("host.querySelectorAll('[data-mode]').forEach", "updateJudgeSummary();host.querySelectorAll('[data-mode]').forEach")
anchor="// Per-floor menu is shared by overhead placement and first-person movement."
add='''function updateJudgeSummary(){
 const plan=getCoolingPlan();const issues=coolingPlanIssues(plan,profile);
 const brief=button('#cg-plan-brief');const apply=button('#cg-apply-plan');
 if(plan){brief.textContent=`Saved Cooling Plan: ${plan.steps.length} recommended action(s), ₹${Math.round(plan.spent).toLocaleString('en-IN')} estimated allowance against ₹${Math.round(plan.budget).toLocaleString('en-IN')} budget. ${issues.length?issues.join(' '):'Property dimensions and city match.'}`;apply.disabled=false;}
 else{brief.textContent='No submitted Cooling Plan on this browser. Complete the Cooling Planner first, or use the guided setup.';apply.disabled=true;}
 const result=compareScenarios(design,profile,home,energy,plan);const selected=result.floorRows[Math.min(activeFloor,result.floorRows.length-1)];
 const money=n=>'₹'+Math.round(n).toLocaleString('en-IN');
 const signed=n=>n>0?`−${n} points`:n<0?`+${Math.abs(n)} points`:'No modelled change';
 button('#cg-comparison').innerHTML=`<h3>Before vs After · same model, same camera</h3><p class="cg-fine">Toggle Original / Improved above. Baseline removes proposed upgrades but keeps existing appliances and opening positions. These indices are illustrative, not measured °C.</p><div class="usjudge-tablewrap"><table class="usjudge-table"><thead><tr><th>Measure</th><th>Original</th><th>Improved</th></tr></thead><tbody><tr><th>Building-wide heat/comfort risk</th><td>${result.originalRisk}/100</td><td>${result.improvedRisk}/100 (${signed(result.riskChange)})</td></tr><tr><th>Floor ${activeFloor+1} heat/comfort risk</th><td>${selected.baseline.heatScore}/100</td><td>${selected.improved.heatScore}/100</td></tr><tr><th>Floor ${activeFloor+1} airflow opportunity</th><td>${selected.baseline.airflowIndex}/100</td><td>${selected.improved.airflowIndex}/100</td></tr><tr><th>Roof solar energy absorbed *</th><td>${fmt(result.originalRoof)} kW</td><td>${fmt(result.improvedRoof)} kW</td></tr><tr><th>Monthly appliance use (all floors) *</th><td colspan="2">${fmt(result.electricity)} kWh with current appliance inventory; no modeled savings attributed to roof treatments</td></tr><tr><th>Cooling plan budget / allowance *</th><td>${money(result.budget||0)} budget</td><td>${result.planCost!=null?money(result.planCost)+' estimated allocation':'No submitted plan'}</td></tr></tbody></table></div><p class="cg-fine">Selected upgrades: ${safe(result.activeMeasures.join(', ')||'No additional upgrades')}. * Screening assumptions, not an invoice, meter reading or indoor temperature prediction.</p>`;
}
button('#cg-apply-plan').onclick=()=>{
 const plan=getCoolingPlan();if(!plan)return;const issues=coolingPlanIssues(plan,profile);
 if(issues.length&&!confirm(issues.join(' ')+' Apply only the recommendations you have selected in that plan?'))return;
 const result=applyCoolingPlan(plan,design,profile,home);
 if(!result.applied.length){button('#cg-plan-message').textContent='This plan contains advisory actions only. There are no directly modelable upgrades to apply; use manual editing as appropriate.';return;}
 home=saveHome(result.home);beforeMode=false;persistDesign(result.design);
 button('#cg-plan-message').textContent='Applied: '+result.applied.join(', ')+'. '+(result.advisory.join(' ')||'Compare Original and Improved, then Start Simulation.');
};
button('#cg-demo').onclick=()=>{
 if(design.objects.length&&!confirm('Replace the current 3D layout with a labeled example? Save a scenario first if you want to keep these objects.'))return;
 const example={floors:Math.max(2,floorCount()),windows:3,windowWall:'opposite',openWindows:'open',vents:true,exhaust:false,ac:2,fans:4,lights:6,fridge:1,roofShade:false,insulation:false,solar:false};
 profile=saveProfile({name:'Example duplex (demonstration)',type:'duplex',floors:2,length:12,width:9,ceilingHeight:2.9,city:'Pune',roof:'concrete'});
 home=saveHome({ambient:34,irradiance:800,roofCoating:false,roofInsulation:false,shade:15,cutaway:true});
 persistDesign(autoLayout({...example,floors:2},profile,energy));dist=fitDistance();beforeMode=false;simulationActive=false;
 button('#cg-guide-status').textContent='Example loaded. This is demonstration data, not a measured property. Choose upgrades, then press Start Simulation.';
};
'''
s=s.replace(anchor,add+anchor)
s=s.replace("button('#cg-before').onclick=()=>{beforeMode=true;", "button('#cg-before').onclick=()=>{beforeMode=true;")
p.write_text(s)

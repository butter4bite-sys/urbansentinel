from pathlib import Path
from playwright.sync_api import sync_playwright
import json, traceback
root=Path('/mnt/data')
base='http://127.0.0.1:8766/'
logs=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--enable-webgl','--use-gl=angle','--use-angle=swiftshader'])
 try:
  page=browser.new_page(viewport={'width':1440,'height':950},device_scale_factor=1)
  page.on('pageerror',lambda e:logs.append('PAGEERROR: '+str(e)))
  page.on('console',lambda m:logs.append('CONSOLE: '+m.text) if m.type=='error' else None)
  page.on('dialog',lambda d:d.accept())
  page.goto(base+'3d-simulation.html',wait_until='domcontentloaded',timeout=30000)
  page.wait_for_selector('#cg-demo',timeout=20000)
  page.click('#cg-demo')
  page.wait_for_timeout(550)
  assert page.locator('#cg-floors').input_value()=='2'
  page.locator('#cg-coat').check()
  page.click('#cg-start-simulation')
  page.wait_for_timeout(450)
  msg=page.locator('#cg-comparison').inner_text()
  assert 'Original' in msg and 'Improved' in msg and 'kW' in msg, msg
  assert page.locator('#cg-sim-heat').inner_text().endswith('/100')
  page.screenshot(path=str(root/'urban_judges_3d_desktop.png'),full_page=True,animations='disabled')
  print('DESKTOP_CHECK',page.locator('#cg-comparison').inner_text()[:280].replace('\n',' | '))
  page.click('#cg-before')
  before=page.locator('#cg-stage-house').inner_text()
  page.click('#cg-after')
  after=page.locator('#cg-stage-house').inner_text()
  assert 'ORIGINAL' in before and 'DESIGN' in after,(before,after)
  print('COMPARE_TOGGLE',before[:30],after[:30])
  # Test planner bridge across pages and persistent storage
  plan={'version':1,'savedAt':'2026-11-19T00:00:00.000Z','details':{'city':'Pune','areaSqFt':round(12*9*10.7639),'budget':50000},'budget':50000,'spent':36000,'steps':[{'id':'roof-paint','title':'Reflective cool-roof treatment','cost':36000},{'id':'thermal-insulation','title':'Roof insulation','cost':44000}]}
  page.evaluate('(v)=>localStorage.setItem("us4.cooling.latest.v1",JSON.stringify(v))',plan)
  page.reload(wait_until='domcontentloaded')
  page.wait_for_selector('#cg-apply-plan',timeout=10000)
  assert page.locator('#cg-apply-plan').is_enabled()
  page.click('#cg-apply-plan')
  assert 'Reflective roof' in page.locator('#cg-plan-message').inner_text()
  assert page.locator('#cg-insulate').is_checked()
  print('PLAN_LINK',page.locator('#cg-plan-message').inner_text()[:120])
  # Mobile smoke
  phone=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
  phone.on('pageerror',lambda e:logs.append('MOBILE_PAGEERROR: '+str(e)))
  phone.goto(base+'3d-simulation.html',wait_until='domcontentloaded',timeout=30000)
  phone.wait_for_selector('#cg-indoor',timeout=16000)
  phone.click('#cg-indoor')
  phone.wait_for_timeout(500)
  print('MOBILE_INDOOR',phone.locator('#cg-indoor').get_attribute('aria-pressed'))
  assert phone.locator('#cg-indoor').get_attribute('aria-pressed')=='true'
  overflow=phone.evaluate('document.documentElement.scrollWidth-innerWidth')
  print('MOBILE_OVERFLOW',overflow)
  phone.screenshot(path=str(root/'urban_judges_3d_mobile.png'),animations='disabled')
  assert overflow <= 5,overflow
  # Marketplace fallback before server setup
  mp=browser.new_page(viewport={'width':1280,'height':900})
  mp.on('pageerror',lambda e:logs.append('MARKET_PAGEERROR: '+str(e)))
  mp.goto(base+'marketplace.html',wait_until='domcontentloaded')
  mp.wait_for_selector('#providerList .us4-provider',timeout=15000)
  print('MARKETPLACE_COUNT',mp.locator('#providerList .us4-provider').count())
  assert mp.locator('#providerList .us4-provider').count()>=9
  assert 'Diligent Enterprises' in mp.locator('#providerList').inner_text()
  assert 'Crystal Interiors' in mp.locator('#providerList').inner_text()
  assert mp.locator('#verifiedList .us4-provider').count()==0
  mp.screenshot(path=str(root/'urban_judges_marketplace.png'),animations='disabled')
 finally:
  browser.close()
print('BROWSER_ERRORS',logs)
if logs: raise RuntimeError(logs)

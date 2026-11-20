from pathlib import Path
import re
root=Path('/mnt/data/urban_sentinel_judges_v1')
p=root/'backend/lib.php';s=p.read_text()
start=s.index('return [',s.index('function us_seed_partners()'))
end=s.index(" ['name'=>'Diligent Enterprises'",start)
reps=[
 dict(name='Satyam Enterprises',category='Waterproofing',region='Kothrud, Pune, Maharashtra',address='Sr. No. 44, Hanuman Nagar, Kothrud, Pune, Maharashtra 411038, India',phone='+91 98902 58212',website='',source='https://www.freelistingindia.in/listings/satyam-enterprises',service='Terrace waterproofing, dampness and roof repairs'),
 dict(name='Conproof Waterproofing',category='Waterproofing',region='Sadashiv Peth, Pune, Maharashtra',address='1696, Khajina Vihar Chowk, Sadashiv Peth, Pune, Maharashtra 411030, India',phone='+91 96234 58303',website='https://waterproofinginpune.com/',source='https://waterproofinginpune.com/',service='Terrace, balcony, bathroom and tank waterproofing'),
 dict(name='Samarth Enterprises',category='Solar energy & lighting',region='Rasta Peth, Pune, Maharashtra',address='Shop No. 6, Sharda Plaza, 342 Rasta Peth, Pune, Maharashtra 411011, India',phone='+91 98221 04343',website='https://samarthsolar.com/',source='https://samarthsolar.com/',service='Solar lighting, solar water heaters, LED systems'),
 dict(name='Unishark Solar',category='Rooftop solar',region='Shivajinagar, Pune, Maharashtra',address='216, Jangali Maharaj Road, opposite JM Temple, Shivajinagar, Pune, Maharashtra 411005, India',phone='+91 91308 31152',website='https://unisharksolar.com/',source='https://unisharksolar.com/',service='Residential rooftop solar planning and installation'),
 dict(name='GReN Eco Services',category='Rainwater harvesting',region='Sinhgad Road, Pune, Maharashtra',address='E101, Sun Orbit, Anand Nagar, Sinhgad Road, Pune, Maharashtra 411051, India',phone='+91 93256 21051',website='',source='',service='Rainwater harvesting, groundwater recharge and water-management services'),
 dict(name='Sunguard Awning',category='Shade structures',region='Kothrud, Pune, Maharashtra',address='Flat 10, Motiram Villa, Paud Road, Bhusari Colony, Kothrud, Pune, Maharashtra 411038, India',phone='+91 98819 87158',website='',source='https://www.justdial.com/Pune/Sunguard-Awning-Kothrud/020PXX20-XX20-130315123029-C9C8_BZDET',service='Retractable awnings, window and terrace shading'),
 dict(name='Crystal Interiors & Awnings',category='Shade structures',region='Prabhat Road, Pune, Maharashtra',address='Lane No. 6, Prabhat Road, Deccan Gymkhana, Pune, Maharashtra 411004, India',phone='+91 95616 18323',website='https://www.crystalinteriors.in',source='https://wa.me/crystalawnings',service='Awnings, tensile canopies and exterior shading'),
 dict(name='Envision Rainwater Harvesting Consultancy',category='Rainwater harvesting',region='Warje, Pune, Maharashtra',address='Ankur Plaza, Malawadi, Warje, Pune, Maharashtra 411058, India',phone='+91 95450 44242',website='https://www.envisionconsultants.in/',source='https://www.envisionconsultants.in/',service='Rainwater harvesting planning, recharge and water management'),
]
lines=[]
for r in reps:
 r.update(description='Publicly identified Pune business. Urban Sentinel partnership/commission agreement is not verified. Owner approval required.',verified=False,agreement_confirmed=False,referral_enabled=False,commission_percent=0)
 parts=[]
 for k,v in r.items():
  if isinstance(v,bool):val='true' if v else 'false'
  elif isinstance(v,(int,float)):val=str(v)
  else:val="'"+str(v).replace('\\','\\\\').replace("'","\\'")+"'"
  parts.append("'"+k+"'=>"+val)
 lines.append(' ['+', '.join(parts)+'],\n')
s=s[:start]+'return [\n'+''.join(lines)+s[end:]
s=s.replace("['id','name','category','service','region','address','phone','email','website','source','verified','referral_enabled','description']", "['id','name','category','service','region','address','phone','email','website','source','verified','agreement_confirmed','referral_enabled','description']")
s=s.replace("'verified'=>false,'referral_enabled'=>true,'commission_percent'=>10],", "'verified'=>false,'agreement_confirmed'=>false,'referral_enabled'=>false,'commission_percent'=>0],",1)
p.write_text(s)

p=root/'backend/api.php';s=p.read_text()
start=s.index(" if($action==='import_pune_candidates'){")
end=s.index(" if($action==='login')",start)
s=s[:start]+''' if($action==='import_pune_candidates'){
  us_auth('owner');
  $candidates=array_slice(us_seed_partners(),0,8);
  // Earlier builds stored five generic location labels and two ambiguous solar contacts.
  // Match old candidates by their original position's name so saved lead IDs are retained.
  $oldAliases=['Satyam Enterprises','Conproof Waterproofing','Samarth Solar','Solar Systems Provider — Shivajinagar','Rainwater Harvesting Provider — Sinhgad Road','Shading Provider — Kothrud','Shading & Interiors Provider — Prabhat Road','Rainwater Harvesting Provider — Warje'];
  $result=us_change('partners',function(&$all)use($candidates,$oldAliases){
   $added=0;$updated=0;
   foreach($candidates as $i=>$candidate){
    $existingIndex=-1;
    foreach($all as $j=>$p)if(strcasecmp($p['name'],$candidate['name'])===0||strcasecmp($p['name'],$oldAliases[$i])===0){$existingIndex=$j;break;}
    if($existingIndex>=0){
     $old=$all[$existingIndex];
     // Never overwrite an owner's approved or explicitly confirmed partner details.
     if(empty($old['verified']) && empty($old['agreement_confirmed'])){
      $all[$existingIndex]=array_replace($old,$candidate,['id'=>$old['id'],'verified'=>false,'agreement_confirmed'=>false,'referral_enabled'=>false,'commission_percent'=>0]);$updated++;
     }
     continue;
    }
    $all[]=['id'=>us_id(),...$candidate,'created_at'=>gmdate('c')];$added++;
   }
   return ['added'=>$added,'updated'=>$updated];
  });
  us_json(['ok'=>true,...$result]);
 }
''' + s[end:]
s=s.replace("if(!$partner || empty($partner['referral_enabled']))us_error(400,'This business is not currently accepting tracked referrals.');", "if(!$partner || empty($partner['referral_enabled']) || empty($partner['agreement_confirmed']) || empty($partner['verified']))us_error(400,'This business is not currently accepting tracked referrals.');")
s=s.replace("$verified=($data['verified']??false)===true;$enabled=($data['referral_enabled']??false)===true;", "$verified=($data['verified']??false)===true;$agreed=($data['agreement_confirmed']??false)===true;$enabled=($data['referral_enabled']??false)===true;")
s=s.replace("if(strlen($name)<2 || !$category || !$region || $percent<0 || $percent>100)us_error(422,'Business name, category, region and valid commission percentage are required.');", "if(strlen($name)<2 || !$category || !$region || $percent<0 || $percent>100)us_error(422,'Business name, category, region and valid commission percentage are required.');if($agreed && !$verified)us_error(422,'Verify the business identity before confirming partnership.');if($enabled && (!$verified || !$agreed))us_error(422,'A tracked referral requires identity verification and a confirmed partner agreement.');")
s=s.replace("$obj=compact('name','category','region','phone','address','service','email','website','source','description','verified','archived');", "$obj=compact('name','category','region','phone','address','service','email','website','source','description','verified','archived');$obj['agreement_confirmed']=$agreed;")
p.write_text(s)

p=root/'assets/js/partner-portal.js';s=p.read_text()
s=s.replace('Import 8 Pune prospects','Import / refresh 8 Pune listings')
s=s.replace('Add the eight Pune shortlist entries? They will be unverified and referrals will stay disabled until you approve them.', 'Import or refresh the eight named Pune directory listings? They stay unverified and cannot receive tracked referrals until you confirm both identity and a partnership agreement.')
s=s.replace("alert(r.added+' new prospects added.');", "alert(`${r.added} new listings added; ${r.updated||0} unapproved directory records refreshed.`);")
# inspect checkbox syntax next rather than blind replace
p.write_text(s)

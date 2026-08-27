from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

old_css = '.geo-map-link.show{display:inline-flex}.geo-map-link:focus-visible{outline-color:var(--green)}'
new_css = '.geo-map-link.show{display:inline-flex}.geo-map-link:focus-visible{outline-color:var(--green)}.geo-ios-help{display:none;margin-top:10px;padding:12px;border:1px solid rgba(188,27,87,.32);border-radius:8px;background:#fff8fb;color:var(--ink-soft);font-size:.76rem;line-height:1.42}.geo-ios-help.show{display:block}.geo-ios-help strong{display:block;color:var(--raspberry-deep);font-size:.8rem}.geo-ios-help p{margin:5px 0 7px}.geo-ios-help ol{margin:0;padding-left:19px}.geo-ios-help li+li{margin-top:4px}'
if old_css not in html:
    raise SystemExit("Ancre CSS de l’aide iPhone introuvable.")
html = html.replace(old_css, new_css, 1)

old_markup = '<div id="geoStatus" class="geo-status" role="status"></div><a id="geoMapLink" class="geo-map-link" href="#" target="_blank" rel="noopener noreferrer" hidden>Ouvrir dans Plans pour vérifier</a>'
new_markup = '''<div id="geoStatus" class="geo-status" role="status"></div><div id="geoIosHelp" class="geo-ios-help" hidden><strong>Autoriser la localisation sur iPhone</strong><p>Ouvrez le site dans Safari, puis vérifiez :</p><ol><li>Réglages iPhone → Confidentialité et sécurité → Service de localisation.</li><li>Choisissez <em>Sites web Safari</em>, puis autorisez la localisation.</li><li>Si Safari l’affiche, modifiez aussi l’autorisation du site depuis les réglages du navigateur.</li></ol></div><a id="geoMapLink" class="geo-map-link" href="#" target="_blank" rel="noopener noreferrer" hidden>Ouvrir dans Plans pour vérifier</a>'''
if old_markup not in html:
    raise SystemExit("Ancre HTML de l’aide iPhone introuvable.")
html = html.replace(old_markup, new_markup, 1)

old_script = 'const geoButton=document.getElementById("geoButton"),geoStatus=document.getElementById("geoStatus"),geoMapLink=document.getElementById("geoMapLink"),geoHelp=document.getElementById("geoHelp");const isIOS='
new_script = 'const geoButton=document.getElementById("geoButton"),geoStatus=document.getElementById("geoStatus"),geoMapLink=document.getElementById("geoMapLink"),geoHelp=document.getElementById("geoHelp"),geoIosHelp=document.getElementById("geoIosHelp");const isIOS='
if old_script not in html:
    raise SystemExit("Déclaration JavaScript de géolocalisation introuvable.")
html = html.replace(old_script, new_script, 1)

old_helper = 'function displayGeo(type,message){geoStatus.className=`geo-status show ${type}`;geoStatus.textContent=message;geoStatus.setAttribute("role",type==="error"?"alert":"status")}function hideGeoMapLink()'
new_helper = 'function displayGeo(type,message){geoStatus.className=`geo-status show ${type}`;geoStatus.textContent=message;geoStatus.setAttribute("role",type==="error"?"alert":"status")}function setIOSPermissionHelp(show){const visible=Boolean(show&&isIOS);geoIosHelp.hidden=!visible;geoIosHelp.classList.toggle("show",visible)}function hideGeoMapLink()'
if old_helper not in html:
    raise SystemExit("Ancre d’aide JavaScript introuvable.")
html = html.replace(old_helper, new_helper, 1)

replacements = [
    ('const {latitude,longitude,accuracy}=position.coords;const coordinates=', 'const {latitude,longitude,accuracy}=position.coords;setIOSPermissionHelp(false);const coordinates='),
    ('displayGeo("error",geoErrorMessage(error,true));geoButton.disabled=false;', 'setIOSPermissionHelp(error.code===1);displayGeo("error",geoErrorMessage(error,true));geoButton.disabled=false;'),
    ('geo=null;hideGeoMapLink();geoButton.disabled=true;', 'geo=null;hideGeoMapLink();setIOSPermissionHelp(false);geoButton.disabled=true;'),
]
for old, new in replacements:
    if old not in html:
        raise SystemExit(f"Ancre de comportement introuvable : {old[:72]}")
    html = html.replace(old, new, 1)

path.write_text(html, encoding="utf-8")
print("Aide de réautorisation iPhone ajoutée au panier.")

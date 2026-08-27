from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

old = 'function initRootScrollPosition(){const returnToTop=()=>{if(!window.location.hash)window.scrollTo({top:0,left:0,behavior:"auto"})};window.addEventListener("pageshow",returnToTop);if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",()=>requestAnimationFrame(returnToTop),{once:true});else requestAnimationFrame(returnToTop)}'
new = 'function initRootScrollPosition(){const returnToTop=()=>{if(window.location.hash)return;window.scrollTo({top:0,left:0,behavior:"auto"});document.documentElement.scrollTop=0;document.body.scrollTop=0};const settleAtTop=()=>{if(window.location.hash)return;returnToTop();requestAnimationFrame(returnToTop);window.setTimeout(returnToTop,80);window.setTimeout(returnToTop,320);window.setTimeout(returnToTop,900)};window.addEventListener("pageshow",settleAtTop);window.addEventListener("load",settleAtTop,{once:true});if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",settleAtTop,{once:true});else settleAtTop()}'

if old not in html:
    raise SystemExit("La fonction de correction attendue est introuvable.")

path.write_text(html.replace(old, new, 1), encoding="utf-8")
print("Remise à zéro du scroll renforcée.")

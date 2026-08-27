from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

old = '''function initRootScrollPosition(){if("scrollRestoration" in history)history.scrollRestoration="manual";let userHasNavigated=false;const shouldReturnToHero=()=>!window.location.hash&&!userHasNavigated;const returnToTop=()=>{if(!shouldReturnToHero())return;window.scrollTo(0,0);document.documentElement.scrollTop=0;document.body.scrollTop=0};const settleAtTop=()=>{if(!shouldReturnToHero())return;returnToTop();requestAnimationFrame(returnToTop);[45,120,280,560,1000,1600].forEach(delay=>window.setTimeout(returnToTop,delay))};const noteUserNavigation=()=>{userHasNavigated=true};["touchstart","pointerdown","wheel"].forEach(type=>window.addEventListener(type,noteUserNavigation,{once:true,passive:true}));window.addEventListener("keydown",noteUserNavigation,{once:true});window.addEventListener("pageshow",event=>{if(!event.persisted)settleAtTop()});window.addEventListener("load",settleAtTop,{once:true});document.addEventListener("visibilitychange",()=>{if(!document.hidden)settleAtTop()});if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",settleAtTop,{once:true});else settleAtTop()}'''

new = '''function initRootScrollPosition(){if("scrollRestoration" in history)history.scrollRestoration="manual";let userHasNavigated=false,topLockUntil=0,topLockFrame=0;const shouldReturnToHero=()=>!window.location.hash&&!userHasNavigated;const returnToTop=()=>{if(!shouldReturnToHero())return;window.scrollTo(0,0);document.documentElement.scrollTop=0;document.body.scrollTop=0};const keepAtTopDuringBoot=()=>{if(!shouldReturnToHero()||performance.now()>topLockUntil){topLockFrame=0;return}returnToTop();topLockFrame=requestAnimationFrame(keepAtTopDuringBoot)};const settleAtTop=()=>{if(!shouldReturnToHero())return;returnToTop();topLockUntil=performance.now()+2600;if(topLockFrame)cancelAnimationFrame(topLockFrame);topLockFrame=requestAnimationFrame(keepAtTopDuringBoot);[45,120,280,560,1000,1600].forEach(delay=>window.setTimeout(returnToTop,delay))};const noteUserNavigation=()=>{userHasNavigated=true;if(topLockFrame)cancelAnimationFrame(topLockFrame)};["touchstart","pointerdown","wheel"].forEach(type=>window.addEventListener(type,noteUserNavigation,{once:true,passive:true}));window.addEventListener("keydown",noteUserNavigation,{once:true});window.addEventListener("pageshow",settleAtTop);window.addEventListener("load",settleAtTop,{once:true});document.addEventListener("visibilitychange",()=>{if(!document.hidden)settleAtTop()});if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",settleAtTop,{once:true});else settleAtTop()}'''

if old not in html:
    raise SystemExit("Routine de retour au hero attendue introuvable.")

path.write_text(html.replace(old, new, 1), encoding="utf-8")
print("Verrou initial de scroll ajouté.")

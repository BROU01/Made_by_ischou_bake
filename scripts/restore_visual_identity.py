from pathlib import Path
import re

path = Path("/home/ubuntu/Made_by_ischou_bake/index.html")
html = path.read_text(encoding="utf-8")

def replace_once(old: str, new: str, label: str) -> None:
    global html
    if html.count(old) != 1:
        raise RuntimeError(f"Remplacement ambigu ou introuvable pour : {label}")
    html = html.replace(old, new, 1)

replace_once(
    '<a class="brand" href="#accueil" aria-label="Made by Ischou, accueil"><span class="brand-mark">M</span><span class="brand-text"><b>Made by</b><span>Ischou</span></span></a>',
    '<a class="brand logo-lockup" href="#accueil" aria-label="Made by Ischou, accueil"><img src="logo.svg" width="78" height="60" alt="Made by Ischou"><span class="sr-only">Made by Ischou</span></a>',
    "logo de navigation",
)
replace_once(
    '<h1 class="hero-title" id="heroTitle">Le goût qui rassemble, <em>préparé avec soin.</em></h1>',
    '<h1 class="hero-title" id="heroTitle">Le goût qui rassemble, <em>préparé avec soin.</em></h1><div class="hero-typewriter" id="heroTypewriterWrap"><span class="hero-typewriter-label">Aujourd’hui, découvrez</span><span class="hero-typewriter-value" id="heroTypewriter" aria-hidden="true"></span><span class="hero-typewriter-cursor" aria-hidden="true"></span><span class="sr-only" id="heroTypewriterStatus">Pastels dorés et généreux</span><div class="hero-progress" aria-hidden="true"><span id="heroProgressFill"></span></div><div class="hero-states" aria-label="Choisir un message du hero"><button type="button" data-hero-state="0" aria-pressed="true">Pastels</button><button type="button" data-hero-state="1" aria-pressed="false">Crêpes</button><button type="button" data-hero-state="2" aria-pressed="false">Box</button></div></div>',
    "typewriter hero",
)
replace_once(
    '<div class="footer-brand">Made by Ischou</div>',
    '<div class="footer-brand"><img src="logo.svg" width="110" height="85" alt="Made by Ischou"></div>',
    "logo de footer",
)
replace_once(
    '<div class="thanks-art" aria-hidden="true">M</div>',
    '<div class="thanks-art thanks-art--gif" aria-hidden="true"><img src="assets/shoppingbag.gif" alt=""></div>',
    "GIF de remerciement",
)

image_map = {
    'id:"box-petite-vanille",family:"box",name:"Petite Box Vanille",description:"7 crêpes roulées à la vanille.",price:1500,count:7}': 'id:"box-petite-vanille",family:"box",name:"Petite Box Vanille",description:"7 crêpes roulées à la vanille.",price:1500,count:7,image:"assets/offres/petite-box-vanille-7.jpg"}',
    'id:"box-petite-chocolat",family:"box",name:"Petite Box Chocolat",description:"6 crêpes roulées au chocolat.",price:2500,count:6}': 'id:"box-petite-chocolat",family:"box",name:"Petite Box Chocolat",description:"6 crêpes roulées au chocolat.",price:2500,count:6,image:"assets/offres/petite-box-chocolat-6.jpg"}',
    'id:"box-petite-chocolat-banane",family:"box",name:"Petite Box Chocolat-Banane",description:"6 crêpes roulées au chocolat et à la banane.",price:3500,count:6}': 'id:"box-petite-chocolat-banane",family:"box",name:"Petite Box Chocolat-Banane",description:"6 crêpes roulées au chocolat et à la banane.",price:3500,count:6,image:"assets/offres/petite-box-chocolat-banane-6.jpg"}',
    'id:"box-classique-vanille",family:"box",name:"Box Classique Vanille",description:"10 crêpes roulées à la vanille.",price:2400,count:10}': 'id:"box-classique-vanille",family:"box",name:"Box Classique Vanille",description:"10 crêpes roulées à la vanille.",price:2400,count:10,image:"assets/offres/box-classique-vanille-10.jpg"}',
    'id:"box-classique-chocolat",family:"box",name:"Box Classique Chocolat",description:"9 crêpes roulées au chocolat.",price:4000,count:9}': 'id:"box-classique-chocolat",family:"box",name:"Box Classique Chocolat",description:"9 crêpes roulées au chocolat.",price:4000,count:9,image:"assets/offres/box-classique-chocolat-9.jpg"}',
    'id:"box-classique-chocolat-banane",family:"box",name:"Box Classique Chocolat-Banane",description:"9 crêpes roulées au chocolat et à la banane.",price:5600,count:9}': 'id:"box-classique-chocolat-banane",family:"box",name:"Box Classique Chocolat-Banane",description:"9 crêpes roulées au chocolat et à la banane.",price:5600,count:9,image:"assets/offres/box-classique-chocolat-banane-9.jpg"}',
    'id:"offer-5-poisson-fume",family:"pastel-offer",name:"5 Pastels Poisson fumé",description:"5 pastels au poisson fumé.",price:1000,count:5}': 'id:"offer-5-poisson-fume",family:"pastel-offer",name:"5 Pastels Poisson fumé",description:"5 pastels au poisson fumé.",price:1000,count:5,image:"assets/offres/formule-5-poisson-fume.jpg"}',
    'id:"offer-5-classique",family:"pastel-offer",name:"5 Pastels Classique",description:"5 pastels classiques à la sardine.",price:1200,count:5}': 'id:"offer-5-classique",family:"pastel-offer",name:"5 Pastels Classique",description:"5 pastels classiques à la sardine.",price:1200,count:5,image:"assets/offres/formule-5-classique.jpg"}',
    'id:"offer-5-gourmand",family:"pastel-offer",name:"5 Pastels Gourmand",description:"5 pastels gourmands.",price:1500,count:5}': 'id:"offer-5-gourmand",family:"pastel-offer",name:"5 Pastels Gourmand",description:"5 pastels gourmands.",price:1500,count:5,image:"assets/offres/formule-5-gourmand.jpg"}',
    'id:"offer-11-poisson-fume",family:"pastel-offer",name:"11 Pastels Poisson fumé",description:"11 pastels au poisson fumé.",price:2000,count:11}': 'id:"offer-11-poisson-fume",family:"pastel-offer",name:"11 Pastels Poisson fumé",description:"11 pastels au poisson fumé.",price:2000,count:11,image:"assets/offres/formule-11-poisson-fume.jpg"}',
    'id:"offer-11-classique",family:"pastel-offer",name:"11 Pastels Classique",description:"11 pastels classiques à la sardine.",price:2400,count:11}': 'id:"offer-11-classique",family:"pastel-offer",name:"11 Pastels Classique",description:"11 pastels classiques à la sardine.",price:2400,count:11,image:"assets/offres/formule-11-classique.jpg"}',
    'id:"offer-11-gourmand",family:"pastel-offer",name:"11 Pastels Gourmand",description:"11 pastels gourmands.",price:3000,count:11}': 'id:"offer-11-gourmand",family:"pastel-offer",name:"11 Pastels Gourmand",description:"11 pastels gourmands.",price:3000,count:11,image:"assets/offres/formule-11-gourmand.jpg"}',
}
for old, new in image_map.items():
    replace_once(old, new, old.split(',')[0])

offer_function = '''    function offerCard(product){const isBox=product.family === "box";const countText=isBox?`${product.count} crêpes`:`${product.count} pastels`;return `<article class="offer-card reveal"><div class="offer-visual"><img src="${product.image}" loading="lazy" width="1280" height="698" alt="${product.name} : ${countText}"><span class="offer-count" aria-label="${countText}">${product.count}</span></div><div class="offer-content"><div class="offer-top"><span class="offer-type">${isBox?"Box à emporter":"Formule à partager"}</span><span class="offer-quantity">${countText}</span></div><h4>${product.name}</h4><p>${product.description}</p><div class="offer-meta">${isBox?"Supplément Banane possible (+200 F par box)":"Formule fixe, sans supplément"}</div><div class="offer-bottom"><span class="price">${money(product.price)}<small>le ${isBox?"box":"pack"}</small></span>${stepperMarkup(product.id)}</div></div></article>`}'''
html, replacements = re.subn(
    r'    function offerCard\(product\)\{.*?\n    function renderCatalogue',
    offer_function + '\n    function renderCatalogue',
    html,
    count=1,
    flags=re.S,
)
if replacements != 1:
    raise RuntimeError("Fonction de carte offre introuvable")

thanks_functions = '''    function openThanks(){if(!totalCount())return;pendingWhatsAppUrl=`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(buildWhatsAppMessage())}`;const overlay=document.getElementById("thanksOverlay"),fill=document.getElementById("progressFill"),value=document.getElementById("progressValue"),status=document.getElementById("thanksStatus"),progress=overlay.querySelector("[role=progressbar]");overlay.classList.add("open");overlay.setAttribute("aria-hidden","false");document.body.classList.add("locked");document.getElementById("thanksClose").focus();const start=performance.now(),duration=7000;function tick(now){const ratio=Math.min(1,(now-start)/duration),percent=Math.round(ratio*100);fill.style.width=`${percent}%`;value.textContent=`${percent} %`;progress.setAttribute("aria-valuenow",String(percent));status.textContent=ratio<.42?"On prépare votre message…":ratio<.82?"Encore un instant, votre commande prend forme…":"WhatsApp va s’ouvrir…";if(ratio<1){thankYouFrame=requestAnimationFrame(tick)}else{window.location.assign(pendingWhatsAppUrl)}}thankYouFrame=requestAnimationFrame(tick)}
    function closeThanks(){if(thankYouFrame){cancelAnimationFrame(thankYouFrame);thankYouFrame=null}const overlay=document.getElementById("thanksOverlay");overlay.classList.remove("open");overlay.setAttribute("aria-hidden","true");document.getElementById("progressFill").style.width="0";document.getElementById("progressValue").textContent="0 %";document.getElementById("thanksStatus").textContent="Préparation du message…";document.body.classList.remove("locked");document.getElementById("orderButton").focus()}
    function openWhatsAppNow(){if(pendingWhatsAppUrl)window.location.assign(pendingWhatsAppUrl)}
    document.getElementById("orderButton").addEventListener("click",openThanks);document.getElementById("thanksClose").addEventListener("click",closeThanks);document.getElementById("thanksNow").addEventListener("click",openWhatsAppNow);

    function initHeroTypewriter(){const wrap=document.getElementById("heroTypewriterWrap"),target=document.getElementById("heroTypewriter"),status=document.getElementById("heroTypewriterStatus"),fill=document.getElementById("heroProgressFill");if(!wrap||!target||!status||!fill)return;const phrases=["Pastels dorés et généreux.","Crêpes longues et gourmandes.","Box prêtes à partager."];const reduced=window.matchMedia("(prefers-reduced-motion: reduce)").matches;let index=0,character=0,deleting=false,paused=false,timer=null,holdStarted=0;const stateButtons=[...wrap.querySelectorAll("[data-hero-state]")];function paint(){target.textContent=phrases[index].slice(0,character);stateButtons.forEach(button=>button.setAttribute("aria-pressed",String(Number(button.dataset.heroState)===index)));fill.style.transform=`scaleX(${Math.min(1,character/phrases[index].length)})`}function schedule(delay){clearTimeout(timer);timer=setTimeout(tick,delay)}function settle(){status.textContent=phrases[index];holdStarted=performance.now();fill.style.transform="scaleX(1)";schedule(1850)}function tick(){if(paused)return;if(!deleting&&character<phrases[index].length){character+=1;paint();schedule(46);return}if(!deleting){settle();deleting=true;return}if(deleting&&character>0){character-=1;paint();schedule(26);return}deleting=false;index=(index+1)%phrases.length;paint();schedule(180)}function selectState(next){index=next;character=reduced?phrases[index].length:0;deleting=false;status.textContent=phrases[index];paint();if(!reduced){paused=false;schedule(90)}}if(reduced){character=phrases[0].length;paint();status.textContent=phrases[0];stateButtons.forEach(button=>button.addEventListener("click",()=>selectState(Number(button.dataset.heroState))));return}schedule(120);wrap.addEventListener("pointerenter",()=>{paused=true;clearTimeout(timer)});wrap.addEventListener("pointerleave",()=>{if(paused){paused=false;schedule(300)}});wrap.addEventListener("focusin",()=>{paused=true;clearTimeout(timer)});wrap.addEventListener("focusout",()=>{paused=false;schedule(300)});stateButtons.forEach(button=>button.addEventListener("click",()=>selectState(Number(button.dataset.heroState))));document.addEventListener("visibilitychange",()=>{if(document.hidden){paused=true;clearTimeout(timer)}else if(!paused){schedule(280)}})}
    function initHeroParallax(){if(window.matchMedia("(prefers-reduced-motion: reduce), (max-width: 720px)").matches)return;const image=document.querySelector(".hero-image");if(!image)return;let frame=0;function update(){frame=0;const shift=Math.min(15,window.scrollY*.045);image.style.transform=`scale(1.04) translate3d(0, ${shift}px, 0)`}function requestUpdate(){if(!frame)frame=requestAnimationFrame(update)}window.addEventListener("scroll",requestUpdate,{passive:true});update()}

    const navLinks='''
html, replacements = re.subn(
    r'    function openThanks\(\)\{.*?\n    const navLinks=',
    thanks_functions,
    html,
    count=1,
    flags=re.S,
)
if replacements != 1:
    raise RuntimeError("Fonctions de remerciement introuvables")

style_layer = '''
    /* Identité restaurée : logo, typewriter, photos d’offres et rythme de scroll */
    .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
    .logo-lockup{width:84px;height:60px;display:flex;align-items:center}.logo-lockup img{width:78px;height:60px;object-fit:contain}.footer-brand{height:72px;display:flex;align-items:center}.footer-brand img{width:110px;height:85px;object-fit:contain;filter:brightness(0) invert(1)}
    .hero-image{will-change:transform}.hero-typewriter{margin-top:22px;max-width:390px}.hero-typewriter-label{display:block;color:rgba(251,243,233,.68);font-size:.7rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase;margin-bottom:5px}.hero-typewriter-value{display:inline;font-family:Georgia,serif;font-size:clamp(1.25rem,2.25vw,1.75rem);font-style:italic;color:#f4cf85}.hero-typewriter-cursor{display:inline-block;width:2px;height:1.05em;margin-left:4px;vertical-align:-.13em;background:#f4cf85;animation:caret .78s steps(2,end) infinite}.hero-progress{height:2px;margin-top:13px;background:rgba(251,243,233,.22);overflow:hidden}.hero-progress span{display:block;height:100%;width:100%;background:#f4cf85;transform:scaleX(0);transform-origin:left;transition:transform .22s linear}.hero-states{display:flex;gap:14px;margin-top:11px}.hero-states button{border:0;padding:0;background:transparent;color:rgba(251,243,233,.55);font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}.hero-states button[aria-pressed="true"]{color:#fff}.hero-states button[aria-pressed="true"]::before{content:"● ";color:#f4cf85}
    .offer-card{padding:0;min-height:0;overflow:hidden}.offer-card:hover{transform:translateY(-4px)}.offer-visual{position:relative;aspect-ratio:1.62/1;overflow:hidden;background:#4b2f26}.offer-visual::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(42,24,16,.05),rgba(42,24,16,.46))}.offer-visual img{width:100%;height:100%;object-fit:cover;transition:transform .7s var(--ease-out)}.offer-card:hover .offer-visual img{transform:scale(1.035)}.offer-card .offer-count{position:absolute;z-index:1;right:12px;bottom:9px;color:#fff;font-size:clamp(3.2rem,5vw,4.4rem);text-shadow:0 2px 18px rgba(42,24,16,.48)}.offer-content{padding:18px 19px 19px;display:flex;flex:1;flex-direction:column}.offer-card .offer-top{align-items:center}.offer-quantity{font-size:.66rem;color:rgba(251,243,233,.65);font-weight:700}.offer-card .offer-bottom{margin-top:auto}.thanks-art--gif{background:#fff7ef;padding:5px;border:2px solid var(--raspberry);overflow:hidden}.thanks-art--gif img{width:100%;height:100%;object-fit:contain}.thanks-card{background:linear-gradient(145deg,#fffaf3,#f8e9df);border:1px solid rgba(188,27,87,.18)}.progress-track{height:7px;background:#ead6c2}.progress-fill{background:linear-gradient(90deg,var(--raspberry),#e7698f)}
    .reveal.in{transition-timing-function:cubic-bezier(.16,1,.3,1)}.catalogue-grid .reveal:nth-child(2),.offer-grid .reveal:nth-child(2){transition-delay:55ms}.catalogue-grid .reveal:nth-child(3),.offer-grid .reveal:nth-child(3){transition-delay:110ms}.offer-grid .reveal:nth-child(4){transition-delay:40ms}.offer-grid .reveal:nth-child(5){transition-delay:85ms}.offer-grid .reveal:nth-child(6){transition-delay:130ms}@keyframes caret{50%{opacity:0}}
'''
marker = '    @media(max-width:960px){'
if html.count(marker) != 1:
    raise RuntimeError("Point d’insertion CSS introuvable")
html = html.replace(marker, style_layer + '\n' + marker, 1)

mobile_overrides = '''
    @media(max-width:720px){.logo-lockup{width:68px;height:52px}.logo-lockup img{width:68px;height:52px}.hero-typewriter{max-width:300px}.hero-states{gap:11px}.hero-states button{font-size:.65rem}.offer-visual{aspect-ratio:1.8/1}.offer-content{padding:17px}.offer-card .offer-count{font-size:3.55rem}.footer-brand img{width:98px;height:76px}}
'''
marker = '    @media(prefers-reduced-motion:reduce){'
if html.count(marker) != 1:
    raise RuntimeError("Point d’insertion responsive introuvable")
html = html.replace(marker, mobile_overrides + '\n' + marker, 1)

replace_once(
    'document.getElementById("year").textContent=new Date().getFullYear();loadCart();renderCatalogue();sync();',
    'document.getElementById("year").textContent=new Date().getFullYear();loadCart();renderCatalogue();sync();initHeroTypewriter();initHeroParallax();',
    "initialisation des effets",
)

path.write_text(html, encoding="utf-8")
print("Identité et visuels restaurés.")

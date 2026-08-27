from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

head_anchor = '  <link rel="icon" href="favicon.svg" type="image/svg+xml">'
head_replacement = '''  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="app.webmanifest">
  <link rel="apple-touch-icon" href="icons/made-by-ischou-180.png">
  <meta name="apple-mobile-web-app-title" content="Made by Ischou">'''
if head_anchor not in html:
    raise SystemExit("Ancre head introuvable.")
html = html.replace(head_anchor, head_replacement, 1)

nav_anchor = '<button class="cart-trigger" id="cartOpen" aria-label="Ouvrir le panier">'
nav_replacement = '<button class="site-share" id="siteShare" type="button" aria-label="Partager le site Made by Ischou"><span aria-hidden="true">↗</span><span>Partager</span></button><button class="cart-trigger" id="cartOpen" aria-label="Ouvrir le panier">'
if nav_anchor not in html:
    raise SystemExit("Ancre navigation introuvable.")
html = html.replace(nav_anchor, nav_replacement, 1)

info_anchor = '        <div class="supplement-panel reveal"><div><strong>Supplément Banane</strong><p>Disponible uniquement avec une crêpe individuelle ou une box. Il n’est pas proposé avec les pastels ni leurs formules.</p></div><b>+200 F</b></div>'
info_replacement = '''        <div class="supplement-panel reveal"><div><strong>Supplément Banane</strong><p>Disponible uniquement avec une crêpe individuelle ou une box. Il n’est pas proposé avec les pastels ni leurs formules.</p></div><b>+200 F</b></div>
        <section class="install-card reveal" id="installCard" aria-labelledby="installTitle"><div><div class="eyebrow">Commande rapide</div><h3 id="installTitle">Gardez Made by Ischou à portée de main.</h3><p id="installCopy">Ajoutez le site à votre écran d’accueil pour y revenir comme dans une application.</p></div><div class="install-actions"><button class="install-button" type="button" id="installButton">Installer l’application</button><p id="installStatus" class="install-status" role="status"></p></div><div id="installHelp" class="install-help" hidden></div></section>'''
if info_anchor not in html:
    raise SystemExit("Ancre section infos introuvable.")
html = html.replace(info_anchor, info_replacement, 1)

footer_anchor = '<p class="cart-footnote">Aucun paiement n’est effectué sur le site.</p>'
footer_replacement = '<button type="button" class="cart-share-button" id="cartShare" disabled>Partager ce panier</button><p id="cartShareStatus" class="share-status" role="status"></p><p class="cart-footnote">Aucun paiement n’est effectué sur le site.</p>'
if footer_anchor not in html:
    raise SystemExit("Ancre pied de panier introuvable.")
html = html.replace(footer_anchor, footer_replacement, 1)

css_anchor = '.cart-footnote{text-align:center;color:var(--ink-soft);font-size:.72rem;margin:8px 0 0}'
css_replacement = '''.cart-footnote{text-align:center;color:var(--ink-soft);font-size:.72rem;margin:8px 0 0}.site-share{border:1px solid var(--line);border-radius:999px;background:transparent;color:var(--raspberry-deep);min-height:39px;padding:8px 12px;font-size:.78rem;font-weight:800;white-space:nowrap}.site-share:hover{background:#fff}.site-share:active,.cart-share-button:active,.install-button:active{transform:scale(.97)}.cart-share-button{width:100%;border:1px solid var(--raspberry);border-radius:9px;background:#fff;color:var(--raspberry-deep);min-height:43px;font-size:.84rem;font-weight:800}.cart-share-button:disabled{opacity:.52;cursor:not-allowed}.share-status{min-height:1.15em;margin:7px 0 0;color:var(--green);text-align:center;font-size:.73rem;font-weight:700}.cart-validation{margin:10px 0 0;padding:10px;border:2px solid var(--raspberry);border-radius:7px;background:#fff0f5;color:#7a153b;font-size:.8rem;line-height:1.35}.install-card{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:22px;align-items:center;margin-top:22px;padding:24px;border:1px solid var(--line);background:#fff8f0;border-radius:2px 2px 18px 2px}.install-card h3{font-family:"Bricolage Grotesque",sans-serif;font-size:clamp(1.35rem,2vw,1.8rem);line-height:1;margin:7px 0}.install-card p{margin:0;color:var(--ink-soft);font-size:.88rem;max-width:55ch}.install-actions{display:grid;justify-items:stretch;gap:4px;min-width:190px}.install-button{border:0;border-radius:999px;min-height:44px;padding:10px 15px;background:var(--ink);color:#fff;font-size:.83rem;font-weight:800}.install-button:hover{background:var(--raspberry-deep)}.install-status{min-height:1.15em;text-align:center;font-size:.71rem!important;font-weight:700;color:var(--green)!important}.install-help{grid-column:1/-1;padding-top:15px;border-top:1px dashed var(--line);font-size:.82rem;line-height:1.45;color:var(--ink-soft)}.install-help strong{color:var(--raspberry-deep)}.install-help ol{margin:8px 0 0;padding-left:20px}.install-help li+li{margin-top:4px}'''
if css_anchor not in html:
    raise SystemExit("Ancre CSS panier introuvable.")
html = html.replace(css_anchor, css_replacement, 1)

media_anchor = '.cart{width:100%}}'
media_replacement = '.cart{width:100%}.site-share{width:39px;padding:8px}.site-share span:last-child{display:none}.install-card{grid-template-columns:1fr;gap:15px}.install-actions{min-width:0}.install-button{width:100%}}'
if media_anchor not in html:
    raise SystemExit("Ancre CSS mobile introuvable.")
html = html.replace(media_anchor, media_replacement, 1)

sync_anchor = 'document.getElementById("deliveryTotalNote").textContent=delivery?"Livraison à confirmer":"Retrait take-away"}'
sync_replacement = 'document.getElementById("deliveryTotalNote").textContent=delivery?"Livraison à confirmer":"Retrait take-away";document.getElementById("cartShare").disabled=count===0}'
if sync_anchor not in html:
    raise SystemExit("Ancre synchronisation panier introuvable.")
html = html.replace(sync_anchor, sync_replacement, 1)

whatsapp_anchor = '    function openThanks(){if(!totalCount())return;pendingWhatsAppUrl='
whatsapp_replacement = '''    function validateDelivery(){const currentAddress=document.getElementById("deliveryAddress");const prior=document.getElementById("cartDeliveryValidation");prior?.remove();currentAddress.removeAttribute("aria-invalid");if(!delivery||geo||currentAddress.value.trim())return true;currentAddress.setAttribute("aria-invalid","true");const notice=document.createElement("p");notice.id="cartDeliveryValidation";notice.className="cart-validation";notice.setAttribute("role","alert");notice.textContent="Ajoutez une adresse, un point de repère ou votre position avant de préparer la livraison.";currentAddress.insertAdjacentElement("beforebegin",notice);currentAddress.focus();return false}document.getElementById("deliveryAddress").addEventListener("input",()=>{document.getElementById("cartDeliveryValidation")?.remove();document.getElementById("deliveryAddress").removeAttribute("aria-invalid")});
    function openThanks(){if(!totalCount()||!validateDelivery())return;pendingWhatsAppUrl='''
if whatsapp_anchor not in html:
    raise SystemExit("Ancre WhatsApp introuvable.")
html = html.replace(whatsapp_anchor, whatsapp_replacement, 1)

before_init_anchor = '    function initRootScrollPosition(){'
sharing_code = '''    const siteShareButton=document.getElementById("siteShare"),cartShareButton=document.getElementById("cartShare"),cartShareStatus=document.getElementById("cartShareStatus");let sharedCartNotice=false;function canonicalUrl(){return `${window.location.origin}${window.location.pathname}`}function encodeCartForShare(){return btoa(JSON.stringify({v:1,items:productItems().map(([id,amount])=>[id,amount,bananas[id]||0])})).replaceAll("+","-").replaceAll("/","_").replaceAll("=","")}function decodeSharedCart(){const token=new URLSearchParams(window.location.search).get("panier");if(!token)return;try{const normalized=token.replaceAll("-","+").replaceAll("_","/");const padded=normalized+"=".repeat((4-normalized.length%4)%4);const shared=JSON.parse(atob(padded));if(shared?.v!==1||!Array.isArray(shared.items))return;const nextCart={},nextBananas={};shared.items.forEach(item=>{const[id,amount,banana]=item||[];if(byId[id]&&Number.isInteger(amount)&&amount>0&&amount<100){nextCart[id]=amount;if(eligible(byId[id])&&Number.isInteger(banana)&&banana>0&&banana<=amount)nextBananas[id]=banana}});if(Object.keys(nextCart).length){cart=nextCart;bananas=nextBananas;sharedCartNotice=true;history.replaceState({},document.title,`${window.location.pathname}${window.location.hash}`)}}catch(error){console.warn("Lien de panier invalide",error)}}async function copyShareLink(url){if(navigator.clipboard?.writeText&&window.isSecureContext){await navigator.clipboard.writeText(url);return}const area=document.createElement("textarea");area.value=url;area.setAttribute("readonly","");area.style.position="fixed";area.style.opacity="0";document.body.append(area);area.select();document.execCommand("copy");area.remove()}async function shareOrCopy(data,status){try{if(navigator.share&&window.isSecureContext){await navigator.share(data);status.textContent="Partage ouvert.";return}await copyShareLink(data.url);status.textContent="Lien copié. Vous pouvez maintenant l’envoyer."}catch(error){if(error?.name==="AbortError"){status.textContent="Partage annulé.";return}try{await copyShareLink(data.url);status.textContent="Partage non disponible : lien copié."}catch(copyError){status.textContent="Copiez ce lien depuis la barre d’adresse."}}}siteShareButton.addEventListener("click",()=>shareOrCopy({title:"Made by Ischou",text:"Pastels, crêpes et box à commander sur WhatsApp.",url:canonicalUrl()},{set text(value){siteShareButton.setAttribute("aria-label",value)}}));cartShareButton.addEventListener("click",()=>{if(!totalCount())return;const url=`${canonicalUrl()}?panier=${encodeURIComponent(encodeCartForShare())}`;shareOrCopy({title:"Mon panier Made by Ischou",text:"Voici le panier que je souhaite partager.",url},cartShareStatus)});
    const installCard=document.getElementById("installCard"),installButton=document.getElementById("installButton"),installCopy=document.getElementById("installCopy"),installStatus=document.getElementById("installStatus"),installHelp=document.getElementById("installHelp");let deferredInstallPrompt=null;const isStandalone=window.matchMedia("(display-mode: standalone)").matches||window.navigator.standalone===true;function showInstallHelp(markup){installHelp.innerHTML=markup;installHelp.hidden=false}function initInstall(){if(isStandalone){installCopy.textContent="Made by Ischou est déjà installé sur cet appareil.";installButton.hidden=true;return}if(isIOS){installButton.textContent="Ajouter à l’écran d’accueil";installButton.addEventListener("click",()=>showInstallHelp("<strong>Sur iPhone ou iPad :</strong><ol><li>Ouvrez ce site dans Safari.</li><li>Appuyez sur le bouton Partager de Safari.</li><li>Choisissez « Sur l’écran d’accueil », puis « Ajouter ».</li></ol>"));return}window.addEventListener("beforeinstallprompt",event=>{event.preventDefault();deferredInstallPrompt=event;installButton.textContent="Installer l’application"});installButton.addEventListener("click",async()=>{if(!deferredInstallPrompt){showInstallHelp("<strong>Sur Android :</strong><ol><li>Ouvrez ce site dans Chrome.</li><li>Ouvrez le menu du navigateur.</li><li>Choisissez « Installer l’application » ou « Ajouter à l’écran d’accueil ».</li></ol>");return}deferredInstallPrompt.prompt();const choice=await deferredInstallPrompt.userChoice;installStatus.textContent=choice.outcome==="accepted"?"Installation lancée.":"Installation annulée.";deferredInstallPrompt=null});window.addEventListener("appinstalled",()=>{installCopy.textContent="Made by Ischou est maintenant installé sur cet appareil.";installButton.hidden=true;installHelp.hidden=true;installStatus.textContent="Installation terminée."})}function registerPwa(){if("serviceWorker" in navigator&&window.isSecureContext)navigator.serviceWorker.register("/sw.js").catch(error=>console.warn("Service worker indisponible",error))}
'''
if before_init_anchor not in html:
    raise SystemExit("Ancre initialisation introuvable.")
html = html.replace(before_init_anchor, sharing_code + before_init_anchor, 1)

load_anchor = 'document.getElementById("year").textContent=new Date().getFullYear();loadCart();renderCatalogue();sync();initRootScrollPosition();initHeroTypewriter();initHeroParallax();initEditorialScroll();'
load_replacement = 'document.getElementById("year").textContent=new Date().getFullYear();loadCart();decodeSharedCart();renderCatalogue();sync();if(sharedCartNotice){cartShareStatus.textContent="Panier partagé chargé. Vérifiez votre commande avant WhatsApp."}initRootScrollPosition();initHeroTypewriter();initHeroParallax();initEditorialScroll();initInstall();registerPwa();'
if load_anchor not in html:
    raise SystemExit("Ancre de chargement introuvable.")
html = html.replace(load_anchor, load_replacement, 1)

path.write_text(html, encoding="utf-8")
print("Contrôle livraison, partage et PWA ajoutés.")

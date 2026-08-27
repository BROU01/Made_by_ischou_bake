from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

old_markup = '<button class="site-share" id="siteShare" type="button" aria-label="Partager le site Made by Ischou"><span aria-hidden="true">↗</span><span>Partager</span></button><button class="cart-trigger"'
new_markup = '<button class="site-share" id="siteShare" type="button" aria-label="Partager le site Made by Ischou"><span aria-hidden="true">↗</span><span>Partager</span></button><span id="siteShareStatus" class="sr-only" role="status" aria-live="polite"></span><button class="cart-trigger"'
if old_markup not in html:
    raise SystemExit("Ancre de partage du site introuvable.")
html = html.replace(old_markup, new_markup, 1)

old_script = 'const siteShareButton=document.getElementById("siteShare"),cartShareButton=document.getElementById("cartShare"),cartShareStatus=document.getElementById("cartShareStatus");let sharedCartNotice=false;'
new_script = 'const siteShareButton=document.getElementById("siteShare"),siteShareStatus=document.getElementById("siteShareStatus"),cartShareButton=document.getElementById("cartShare"),cartShareStatus=document.getElementById("cartShareStatus");let sharedCartNotice=false;'
if old_script not in html:
    raise SystemExit("Ancre JavaScript de partage introuvable.")
html = html.replace(old_script, new_script, 1)

old_share = 'async function shareOrCopy(data,status){try{if(navigator.share&&window.isSecureContext){await navigator.share(data);status.textContent="Partage ouvert.";return}await copyShareLink(data.url);status.textContent="Lien copié. Vous pouvez maintenant l’envoyer."}catch(error){if(error?.name==="AbortError"){status.textContent="Partage annulé.";return}try{await copyShareLink(data.url);status.textContent="Partage non disponible : lien copié."}catch(copyError){status.textContent="Copiez ce lien depuis la barre d’adresse."}}}siteShareButton.addEventListener("click",()=>shareOrCopy({title:"Made by Ischou",text:"Pastels, crêpes et box à commander sur WhatsApp.",url:canonicalUrl()},{set text(value){siteShareButton.setAttribute("aria-label",value)}}));'
new_share = 'function shareFeedback(status,message){status.textContent=message;if(status===siteShareStatus){const label=siteShareButton.querySelector("span:last-child"),original="Partager";label.textContent=message.includes("copié")?"Lien copié":"Partager";window.setTimeout(()=>{label.textContent=original;status.textContent=""},2400)}}async function shareOrCopy(data,status){try{if(navigator.share&&window.isSecureContext){await navigator.share(data);shareFeedback(status,"Partage ouvert.");return}await copyShareLink(data.url);shareFeedback(status,"Lien copié. Vous pouvez maintenant l’envoyer.")}catch(error){if(error?.name==="AbortError"){shareFeedback(status,"Partage annulé.");return}try{await copyShareLink(data.url);shareFeedback(status,"Partage non disponible : lien copié.")}catch(copyError){shareFeedback(status,"Copiez ce lien depuis la barre d’adresse.")}}}siteShareButton.addEventListener("click",()=>shareOrCopy({title:"Made by Ischou",text:"Pastels, crêpes et box à commander sur WhatsApp.",url:canonicalUrl()},siteShareStatus));'
if old_share not in html:
    raise SystemExit("Routine de partage à remplacer introuvable.")
html = html.replace(old_share, new_share, 1)

path.write_text(html, encoding="utf-8")
print("Retour de copie du lien public ajouté.")

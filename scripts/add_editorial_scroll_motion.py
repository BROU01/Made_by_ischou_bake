from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

if "initEditorialScroll" in html:
    raise SystemExit("La motion éditoriale est déjà présente : aucune modification appliquée.")

css_anchor = ".reveal.in{opacity:1;transform:none;transition:opacity .72s var(--ease-out),transform .72s var(--ease-out)}"
css_addition = r'''
    /* Motion éditoriale au scroll : profondeur lente et chapitres, sans canvas */
    .scene-heading{position:relative;isolation:isolate}.scene-heading::before{content:attr(data-chapter);position:absolute;z-index:-1;right:0;bottom:-25px;font-family:Georgia,serif;font-style:italic;font-size:clamp(4.8rem,10vw,8.8rem);line-height:.7;color:rgba(188,27,87,.08);pointer-events:none}.scene-heading::after{content:"";position:absolute;bottom:-18px;left:0;width:min(156px,38%);height:2px;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .92s var(--ease-out) .18s}.scene-heading .eyebrow,.scene-heading h2,.scene-heading p{opacity:0;transform:translate3d(0,22px,0);transition:opacity .74s var(--ease-out),transform .74s var(--ease-out)}.scene-heading.in .eyebrow,.scene-heading.in h2,.scene-heading.in p{opacity:1;transform:none}.scene-heading.in h2{transition-delay:85ms}.scene-heading.in p{transition-delay:180ms}.scene-heading.in::after{transform:scaleX(1)}.scene-atelier .atelier-intro,.scene-atelier .process{opacity:0;transition:opacity .8s var(--ease-out),transform .8s var(--ease-out)}.scene-atelier .atelier-intro{transform:translate3d(-22px,18px,0)}.scene-atelier .process{transform:translate3d(22px,18px,0)}.scene-atelier.in .atelier-intro,.scene-atelier.in .process{opacity:1;transform:none}.scene-atelier.in .process{transition-delay:115ms}.scene-line{position:relative}.scene-line::after{content:"";position:absolute;right:0;bottom:-8px;width:72px;height:1px;background:var(--raspberry);transform:scaleX(0);transform-origin:right;transition:transform .8s var(--ease-out) .2s}.scene-line.in::after{transform:scaleX(1)}.scene-board .info-card{opacity:0;transform:translate3d(0,22px,0);transition:opacity .65s var(--ease-out),transform .65s var(--ease-out)}.scene-board.in .info-card{opacity:1;transform:none}.scene-board.in .info-card:nth-child(2){transition-delay:70ms}.scene-board.in .info-card:nth-child(3){transition-delay:140ms}.scene-board.in .info-card:nth-child(4){transition-delay:210ms}.depth-viewport{overflow:hidden}.crepe-portrait img[data-depth]{will-change:transform}.offers .wrap{position:relative;z-index:1}.offers .scene-heading::before{color:rgba(251,243,233,.075)}.offer-orbit{position:absolute;z-index:0;right:-32vw;top:230px;width:min(72vw,840px);aspect-ratio:1;border:1px solid rgba(244,207,133,.24);border-radius:50%;box-shadow:0 0 0 58px rgba(251,243,233,.028),0 0 0 116px rgba(251,243,233,.018);pointer-events:none;will-change:transform}
'''.strip()

if css_anchor not in html:
    raise SystemExit("Ancre CSS introuvable.")
html = html.replace(css_anchor, css_anchor + "\n    " + css_addition, 1)

replacements = [
    ('<div class="hero-copy reveal">', '<div class="hero-copy reveal scene-hero-copy">'),
    ('<aside class="hero-side-note reveal"', '<aside class="hero-side-note reveal scene-hero-note"'),
    ('<div class="wrap atelier-grid reveal">', '<div class="wrap atelier-grid reveal scene-atelier">'),
    ('<div class="section-heading reveal"><div><div class="eyebrow">Les incontournables</div>', '<div class="section-heading reveal scene-heading" data-chapter="01"><div><div class="eyebrow">Les incontournables</div>'),
    ('<div class="product-intro reveal">', '<div class="product-intro reveal scene-line">'),
    ('<div class="section-heading reveal"><div><div class="eyebrow">La pause douceur</div>', '<div class="section-heading reveal scene-heading" data-chapter="02"><div><div class="eyebrow">La pause douceur</div>'),
    ('<figure class="crepe-portrait reveal"><img src="assets/refonte/crepes-generous.jpg"', '<figure class="crepe-portrait reveal depth-viewport"><img data-depth="14" data-depth-scale="1.06" src="assets/refonte/crepes-generous.jpg"'),
    ('<section class="offers" id="offres" aria-labelledby="offresTitle">\n      <div class="wrap">', '<section class="offers" id="offres" aria-labelledby="offresTitle">\n      <div class="offer-orbit" data-depth="11" aria-hidden="true"></div>\n      <div class="wrap">'),
    ('<div class="section-heading reveal"><div><div class="eyebrow">À partager ou à offrir</div>', '<div class="section-heading reveal scene-heading" data-chapter="03"><div><div class="eyebrow">À partager ou à offrir</div>'),
    ('<div class="offer-intro reveal">', '<div class="offer-intro reveal scene-line">'),
    ('<div class="section-heading reveal"><div><div class="eyebrow">Tout savoir</div>', '<div class="section-heading reveal scene-heading" data-chapter="04"><div><div class="eyebrow">Tout savoir</div>'),
    ('<div class="info-grid reveal">', '<div class="info-grid reveal scene-board">'),
]

for old, new in replacements:
    if old not in html:
        raise SystemExit(f"Ancre HTML introuvable : {old[:76]}")
    html = html.replace(old, new, 1)

mobile_anchor = '@media(max-width:720px){.wrap{width:min(100% - 30px,var(--max))}'
mobile_replacement = '@media(max-width:720px){.scene-heading::before{right:0;bottom:-19px;font-size:4.8rem}.scene-heading::after{bottom:-14px}.offer-orbit{display:none}.wrap{width:min(100% - 30px,var(--max))}'
if mobile_anchor not in html:
    raise SystemExit("Ancre mobile introuvable.")
html = html.replace(mobile_anchor, mobile_replacement, 1)

script_anchor = '    const navLinks=[...document.querySelectorAll(".nav-links a")];'
script_addition = r'''
    function initEditorialScroll(){if(window.matchMedia("(prefers-reduced-motion: reduce), (max-width: 960px)").matches)return;const depthItems=[...document.querySelectorAll("[data-depth]")];if(!depthItems.length)return;const active=new Set();let frame=0;function update(){frame=0;const viewport=window.innerHeight||1;active.forEach(item=>{const rect=item.getBoundingClientRect(),factor=Number(item.dataset.depth)||0,progress=Math.max(-1,Math.min(1,(rect.top+rect.height/2-viewport/2)/viewport)),scale=Number(item.dataset.depthScale)||1;item.style.transform=`translate3d(0, ${Math.round(progress*factor)}px, 0) scale(${scale})`})}function schedule(){if(!frame)frame=requestAnimationFrame(update)}const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting)active.add(entry.target);else active.delete(entry.target)});schedule()},{rootMargin:"18% 0px 18% 0px"});depthItems.forEach(item=>{item.style.willChange="transform";observer.observe(item)});window.addEventListener("scroll",schedule,{passive:true});window.addEventListener("resize",schedule,{passive:true});schedule()}

'''.strip()
if script_anchor not in html:
    raise SystemExit("Ancre JavaScript introuvable.")
html = html.replace(script_anchor, script_addition + "\n\n    " + script_anchor, 1)

startup_anchor = 'initHeroTypewriter();initHeroParallax();'
if startup_anchor not in html:
    raise SystemExit("Ancre d’initialisation introuvable.")
html = html.replace(startup_anchor, 'initHeroTypewriter();initHeroParallax();initEditorialScroll();', 1)

path.write_text(html, encoding="utf-8")
print("Motion éditoriale ajoutée à index.html")

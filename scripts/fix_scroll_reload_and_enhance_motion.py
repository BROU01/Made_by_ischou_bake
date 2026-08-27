from pathlib import Path


path = Path(__file__).resolve().parents[1] / "index.html"
html = path.read_text(encoding="utf-8")

if "initRootScrollPosition" in html:
    raise SystemExit("La correction du rechargement est déjà présente : aucune modification appliquée.")

head_anchor = '  <link rel="icon" href="favicon.svg" type="image/svg+xml">'
head_addition = '''  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <script>
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  </script>'''
if head_anchor not in html:
    raise SystemExit("Ancre du head introuvable.")
html = html.replace(head_anchor, head_addition, 1)

css_replacements = [
    (
        '.scene-heading{position:relative;isolation:isolate}.scene-heading::before{content:attr(data-chapter);position:absolute;z-index:-1;right:0;bottom:-25px;font-family:Georgia,serif;font-style:italic;font-size:clamp(4.8rem,10vw,8.8rem);line-height:.7;color:rgba(188,27,87,.08);pointer-events:none}.scene-heading::after{content:"";position:absolute;bottom:-18px;left:0;width:min(156px,38%);height:2px;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .92s var(--ease-out) .18s}.scene-heading .eyebrow,.scene-heading h2,.scene-heading p{opacity:0;transform:translate3d(0,22px,0);transition:opacity .74s var(--ease-out),transform .74s var(--ease-out)}.scene-heading.in .eyebrow,.scene-heading.in h2,.scene-heading.in p{opacity:1;transform:none}.scene-heading.in h2{transition-delay:85ms}.scene-heading.in p{transition-delay:180ms}.scene-heading.in::after{transform:scaleX(1)}.scene-atelier .atelier-intro,.scene-atelier .process{opacity:0;transition:opacity .8s var(--ease-out),transform .8s var(--ease-out)}.scene-atelier .atelier-intro{transform:translate3d(-22px,18px,0)}.scene-atelier .process{transform:translate3d(22px,18px,0)}.scene-atelier.in .atelier-intro,.scene-atelier.in .process{opacity:1;transform:none}.scene-atelier.in .process{transition-delay:115ms}.scene-line{position:relative}.scene-line::after{content:"";position:absolute;right:0;bottom:-8px;width:72px;height:1px;background:var(--raspberry);transform:scaleX(0);transform-origin:right;transition:transform .8s var(--ease-out) .2s}.scene-line.in::after{transform:scaleX(1)}.scene-board .info-card{opacity:0;transform:translate3d(0,22px,0);transition:opacity .65s var(--ease-out),transform .65s var(--ease-out)}.scene-board.in .info-card{opacity:1;transform:none}.scene-board.in .info-card:nth-child(2){transition-delay:70ms}.scene-board.in .info-card:nth-child(3){transition-delay:140ms}.scene-board.in .info-card:nth-child(4){transition-delay:210ms}.depth-viewport{overflow:hidden}.crepe-portrait img[data-depth]{will-change:transform}.offers .wrap{position:relative;z-index:1}.offers .scene-heading::before{color:rgba(251,243,233,.075)}.offer-orbit{position:absolute;z-index:0;right:-32vw;top:230px;width:min(72vw,840px);aspect-ratio:1;border:1px solid rgba(244,207,133,.24);border-radius:50%;box-shadow:0 0 0 58px rgba(251,243,233,.028),0 0 0 116px rgba(251,243,233,.018);pointer-events:none;will-change:transform}',
        '.scene-heading{position:relative;isolation:isolate}.scene-heading::before{content:attr(data-chapter);position:absolute;z-index:-1;right:0;bottom:-27px;font-family:Georgia,serif;font-style:italic;font-size:clamp(5.2rem,11vw,9.6rem);line-height:.7;color:rgba(188,27,87,.12);pointer-events:none;transform:translate3d(18px,14px,0);transition:transform 1s var(--ease-out),opacity .8s var(--ease-out);opacity:0}.scene-heading::after{content:"";position:absolute;bottom:-18px;left:0;width:min(188px,44%);height:2px;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform 1s var(--ease-out) .18s}.scene-heading .eyebrow,.scene-heading h2,.scene-heading p{opacity:0;transition:opacity .88s var(--ease-out),transform .88s var(--ease-out)}.scene-heading .eyebrow{transform:translate3d(-24px,12px,0)}.scene-heading h2{transform:translate3d(-38px,20px,0)}.scene-heading p{transform:translate3d(34px,20px,0)}.scene-heading.in .eyebrow,.scene-heading.in h2,.scene-heading.in p{opacity:1;transform:none}.scene-heading.in h2{transition-delay:100ms}.scene-heading.in p{transition-delay:220ms}.scene-heading.in::before{opacity:1;transform:none}.scene-heading.in::after{transform:scaleX(1)}.scene-atelier .atelier-intro,.scene-atelier .process{opacity:0;transition:opacity .92s var(--ease-out),transform .92s var(--ease-out)}.scene-atelier .atelier-intro{transform:translate3d(-34px,24px,0)}.scene-atelier .process{transform:translate3d(34px,24px,0)}.scene-atelier.in .atelier-intro,.scene-atelier.in .process{opacity:1;transform:none}.scene-atelier.in .process{transition-delay:150ms}.scene-line{position:relative}.scene-line::after{content:"";position:absolute;right:0;bottom:-8px;width:112px;height:2px;background:var(--raspberry);transform:scaleX(0);transform-origin:right;transition:transform .9s var(--ease-out) .22s}.scene-line.in::after{transform:scaleX(1)}.scene-board .info-card{opacity:0;transform:translate3d(0,34px,0);transition:opacity .76s var(--ease-out),transform .76s var(--ease-out)}.scene-board.in .info-card{opacity:1;transform:none}.scene-board.in .info-card:nth-child(2){transition-delay:80ms}.scene-board.in .info-card:nth-child(3){transition-delay:160ms}.scene-board.in .info-card:nth-child(4){transition-delay:240ms}.offers .offer-card.reveal{transform:translate3d(0,42px,0)}.offers .offer-card.reveal.in{transform:none;transition:opacity .82s var(--ease-out),transform .82s var(--ease-out),background .2s var(--ease-out)}.offers .offer-card.reveal.in:hover{transform:translateY(-4px)}.depth-viewport{overflow:hidden}.crepe-portrait img[data-depth]{will-change:transform}.offers .wrap{position:relative;z-index:1}.offers .scene-heading::before{color:rgba(251,243,233,.12)}.offer-orbit{position:absolute;z-index:0;right:-32vw;top:230px;width:min(72vw,840px);aspect-ratio:1;border:1px solid rgba(244,207,133,.32);border-radius:50%;box-shadow:0 0 0 58px rgba(251,243,233,.042),0 0 0 116px rgba(251,243,233,.028);pointer-events:none;will-change:transform}'
    ),
    (
        '<img data-depth="14" data-depth-scale="1.06" src="assets/refonte/crepes-generous.jpg"',
        '<img data-depth="26" data-depth-scale="1.08" src="assets/refonte/crepes-generous.jpg"'
    ),
    (
        '<div class="offer-orbit" data-depth="11" aria-hidden="true"></div>',
        '<div class="offer-orbit" data-depth="18" aria-hidden="true"></div>'
    ),
]

for old, new in css_replacements:
    if old not in html:
        raise SystemExit(f"Ancre de motion introuvable : {old[:80]}")
    html = html.replace(old, new, 1)

script_anchor = '    function initHeroTypewriter()'
scroll_script = '''    function initRootScrollPosition(){const returnToTop=()=>{if(!window.location.hash)window.scrollTo({top:0,left:0,behavior:"auto"})};window.addEventListener("pageshow",returnToTop);if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",()=>requestAnimationFrame(returnToTop),{once:true});else requestAnimationFrame(returnToTop)}

'''
if script_anchor not in html:
    raise SystemExit("Ancre JavaScript d’initialisation introuvable.")
html = html.replace(script_anchor, scroll_script + script_anchor, 1)

startup_anchor = 'initHeroTypewriter();initHeroParallax();initEditorialScroll();'
if startup_anchor not in html:
    raise SystemExit("Ancre de démarrage introuvable.")
html = html.replace(startup_anchor, 'initRootScrollPosition();initHeroTypewriter();initHeroParallax();initEditorialScroll();', 1)

path.write_text(html, encoding="utf-8")
print("Correction de rechargement et motion renforcée appliquées à index.html")

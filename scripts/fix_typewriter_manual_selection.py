from pathlib import Path

path = Path("/home/ubuntu/Made_by_ischou_bake/index.html")
html = path.read_text(encoding="utf-8")

replacements = {
    'let index=0,character=0,deleting=false,paused=false,timer=null,holdStarted=0;': 'let index=0,character=0,deleting=false,paused=false,manuallySelected=false,timer=null,holdStarted=0;',
    'function selectState(next){index=next;character=reduced?phrases[index].length:0;deleting=false;status.textContent=phrases[index];paint();if(!reduced){paused=false;schedule(90)}}': 'function selectState(next){index=next;character=phrases[index].length;deleting=false;manuallySelected=true;paused=true;clearTimeout(timer);status.textContent=phrases[index];paint();fill.style.transform="scaleX(1)"}',
    'wrap.addEventListener("pointerleave",()=>{if(paused){paused=false;schedule(300)}});': 'wrap.addEventListener("pointerleave",()=>{if(paused&&!manuallySelected){paused=false;schedule(300)}});',
    'wrap.addEventListener("focusout",()=>{paused=false;schedule(300)});': 'wrap.addEventListener("focusout",()=>{if(!manuallySelected){paused=false;schedule(300)}});',
}

for old, new in replacements.items():
    if html.count(old) != 1:
        raise RuntimeError(f"Remplacement introuvable ou ambigu : {old[:55]}")
    html = html.replace(old, new, 1)

path.write_text(html, encoding="utf-8")
print("Le typewriter respecte désormais la sélection manuelle.")

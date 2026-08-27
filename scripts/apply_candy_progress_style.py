from pathlib import Path

path = Path("/home/ubuntu/Made_by_ischou_bake/index.html")
html = path.read_text(encoding="utf-8")

old = '.thanks-art--gif{background:#fff7ef;padding:5px;border:2px solid var(--raspberry);overflow:hidden}.thanks-art--gif img{width:100%;height:100%;object-fit:contain}.thanks-card{background:linear-gradient(145deg,#fffaf3,#f8e9df);border:1px solid rgba(188,27,87,.18)}.progress-track{height:7px;background:#ead6c2}.progress-fill{background:linear-gradient(90deg,var(--raspberry),#e7698f)}'
new = '.thanks-art--gif{background:#fff7ef;padding:5px;border:2px solid var(--raspberry);overflow:hidden}.thanks-art--gif img{width:100%;height:100%;object-fit:contain}.thanks-card{background:linear-gradient(145deg,#fffaf3,#f8e9df);border:1px solid rgba(188,27,87,.18)}.progress-track{box-sizing:border-box;position:relative;height:31px;padding:3px;overflow:hidden;background:#ffe4e9;border:3px solid var(--raspberry);border-radius:999px;box-shadow:0 4px 0 var(--raspberry-deep),inset 0 2px 4px rgba(42,24,16,.2)}.progress-fill{position:relative;height:100%;overflow:hidden;border-radius:999px;background:linear-gradient(180deg,rgba(255,255,255,.42),rgba(255,79,143,.1)),repeating-linear-gradient(-45deg,#ff529a 0 14px,#ff529a 14px,#fff6f8 14px,#fff6f8 28px);box-shadow:inset 0 -2px 0 rgba(87,23,43,.22);animation:candyStripeShift 1.7s linear infinite}.progress-fill::before,.progress-fill::after{content:"";position:absolute;pointer-events:none}.progress-fill::before{top:1px;right:3px;left:3px;height:48%;border-radius:999px 999px 5px 5px;background:linear-gradient(180deg,rgba(255,255,255,.86),rgba(255,255,255,.08))}.progress-fill::after{top:0;bottom:0;left:-42px;width:34px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.65),transparent);transform:skewX(-20deg);animation:candyShineSweep 2.8s ease-in-out infinite}@keyframes candyStripeShift{to{background-position:0 0,28px 0}}@keyframes candyShineSweep{0%,58%{left:-42px}100%{left:calc(100% + 42px)}}@media (prefers-reduced-motion:reduce){.progress-fill,.progress-fill::after{animation:none}}'

if html.count(old) != 1:
    raise RuntimeError("Le bloc de progress bar actuel est introuvable ou ambigu.")

path.write_text(html.replace(old, new, 1), encoding="utf-8")
print("Style Candy Crush/Pirouline appliqué à la progress bar du popup.")

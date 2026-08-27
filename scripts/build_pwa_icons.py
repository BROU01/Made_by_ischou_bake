from pathlib import Path

import cairosvg


root = Path(__file__).resolve().parents[1]
source = root / "icons" / "made-by-ischou-app-icon.svg"
for size in (192, 512, 180):
    destination = root / "icons" / f"made-by-ischou-{size}.png"
    cairosvg.svg2png(url=str(source), write_to=str(destination), output_width=size, output_height=size)
    print(destination.relative_to(root))

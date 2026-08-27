from pathlib import Path
from PIL import Image

ROOT = Path("/home/ubuntu/Made_by_ischou_bake")
SOURCE = Path("/home/ubuntu/webdev-static-assets/made_by_ischou")
DESTINATION = ROOT / "assets" / "refonte"
DESTINATION.mkdir(parents=True, exist_ok=True)

ASSETS = {
    "calibration-pastels-generous.jpg": "pastels-generous.jpg",
    "calibration-crepes-generous.jpg": "crepes-generous.jpg",
}

for source_name, output_name in ASSETS.items():
    source = SOURCE / source_name
    if not source.exists():
        raise FileNotFoundError(f"Asset de calibration manquant : {source}")

    with Image.open(source) as image:
        image = image.convert("RGB")
        width = 1280
        height = round(image.height * width / image.width)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        image.save(
            DESTINATION / output_name,
            "JPEG",
            quality=82,
            optimize=True,
            progressive=True,
        )

for output_name in ASSETS.values():
    output = DESTINATION / output_name
    print(f"{output.name}: {output.stat().st_size} octets")

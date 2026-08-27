from pathlib import Path
from PIL import Image, ImageOps

UPLOADS = Path("/home/ubuntu/upload")
DESTINATION = Path("/home/ubuntu/Made_by_ischou_bake/assets/offres")
DESTINATION.mkdir(parents=True, exist_ok=True)

IMAGES = {
    "pasted_file_SQxECg_PetiteBoxVanille—7pièces.png": "petite-box-vanille-7.jpg",
    "pasted_file_U7B5Qm_PetiteBoxChocolat—6pièces.jpg": "petite-box-chocolat-6.jpg",
    "pasted_file_jb2Eof_PetiteBoxChocolat-Banane—6pièces.jpg": "petite-box-chocolat-banane-6.jpg",
    "pasted_file_e9CY3j_BoxClassiqueVanille—10pièces.jpg": "box-classique-vanille-10.jpg",
    "pasted_file_Dbxtqt_BoxClassiqueChocolat—9pièces.jpg": "box-classique-chocolat-9.jpg",
    "pasted_file_zYdAfn_BoxClassiqueChocolat-Banane—9pièces.jpg": "box-classique-chocolat-banane-9.jpg",
    "pasted_file_EbafCq_5PastelsPoissonfumé.jpg": "formule-5-poisson-fume.jpg",
    "pasted_file_Bn2N4v_5PastelsClassique.jpg": "formule-5-classique.jpg",
    "pasted_file_sLmRVW_5PastelsGourmand.jpg": "formule-5-gourmand.jpg",
    "pasted_file_qtgzma_11PastelsPoissonfumé.jpg": "formule-11-poisson-fume.jpg",
    "pasted_file_lnAJFh_11PastelsClassique.jpg": "formule-11-classique.jpg",
    "pasted_file_XRH3in_11PastelsGourmand.jpg": "formule-11-gourmand.jpg",
}

for input_name, output_name in IMAGES.items():
    source = UPLOADS / input_name
    if not source.exists():
        raise FileNotFoundError(f"Photo introuvable : {source}")

    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
        target = DESTINATION / output_name
        image.save(target, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"{output_name}: {image.width}×{image.height}, {target.stat().st_size} octets")

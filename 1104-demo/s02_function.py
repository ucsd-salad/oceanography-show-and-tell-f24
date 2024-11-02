import pytesseract
from PIL import Image
from pathlib import Path


def recognize_image(img: Image) -> str:
    return pytesseract.image_to_string(img)


def recognize_and_write(img_path: Path, out_dir: Path):
    img = Image.open(img_path)
    text = recognize_image(img)
    out_path = out_dir / img_path.with_suffix(".txt").name
    out_path.write_text(text)

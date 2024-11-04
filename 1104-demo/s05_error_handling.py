from PIL import Image
from pathlib import Path
from joblib import Parallel, delayed
from tqdm import tqdm

from s02_function import recognize_image
from enum import Enum


class RecognitionResult(Enum):
    SUCCESS = "success"
    SKIP = "skip"
    ERROR = "error"


def recognize_and_write_if_needed(
    img_path: Path, out_dir: Path
) -> tuple[Path, RecognitionResult, str | None]:
    out_path = out_dir / img_path.with_suffix(".txt").name
    if out_path.exists():
        return img_path, RecognitionResult.SKIP, None
    try:
        img = Image.open(img_path)
        text = recognize_image(img)
        out_path.write_text(text)
    except Exception as e:
        return img_path, RecognitionResult.ERROR, str(e)
    return img_path, RecognitionResult.SUCCESS, None


def main(argv) -> int:
    if len(argv) != 3:
        print(f"Usage: {argv[0]} <input_dir> <output_dir>")
        return 1

    input_dir = Path(argv[1])
    out_dir = Path(argv[2])

    files = list(input_dir.iterdir())

    results = Parallel(n_jobs=-1, backend="multiprocessing")(
        delayed(recognize_and_write_if_needed)(img_path, out_dir)
        for img_path in tqdm(files)
    )

    for img_path, result, message in results:
        if result == RecognitionResult.SUCCESS:
            # print(f"Recognized {img_path}")
            pass
        elif result == RecognitionResult.SKIP:
            print(f"Skipped {img_path}")
        elif result == RecognitionResult.ERROR:
            print(f"Error processing {img_path}: {message}")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

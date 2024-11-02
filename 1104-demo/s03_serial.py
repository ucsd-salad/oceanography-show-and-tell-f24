from pathlib import Path
from tqdm import tqdm

from s02_function import recognize_and_write


def main(argv) -> int:
    if len(argv) != 3:
        print(f"Usage: {argv[0]} <input_dir> <output_dir>")
        return 1

    input_dir = Path(argv[1])
    out_dir = Path(argv[2])

    files = list(input_dir.iterdir())

    for img_path in tqdm(files):
        recognize_and_write(img_path, out_dir)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

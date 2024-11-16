## Overview

This repository demonstrates how to deal with modularity, parallelism, and error recovery in Python.

We consider a scenario where we have a directory with a large number of images and we want to extract text from them and save the results. We use the `pytesseract` library to extract text from images.

The accompanying slides can be found [here](https://docs.google.com/presentation/d/1q2hlC86bsF8pDmSiJxyZxu5aYUqdwQzR5tuboGGRt_c/edit?usp=sharing).

## Setup

1. You need to have [uv](https://github.com/astral-sh/uv) installed.
1. Run `uv venv` to create a virtual environment.
1. Run `uv sync` to install the dependencies.
1. Use `uv run jupyter lab` to start the Jupyter Lab server.
1. Use `uv run python [file.py]` to run a Python script.
   - `s03_serial.py` and `s04_parallel.py` take two arguments: the input directory and the output directory.

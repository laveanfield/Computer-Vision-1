# CV Project 1: Color Image Representation, Signal Filtering, and Geometric Transformations

Computer Vision project consisting of 3 parts, each with its own notebook:

| Notebook | Content |
| --- | --- |
| `notebooks/module1_color_gray.ipynb` | Part 1: Color images, grayscale images, splitting / merging / swapping / replacing color channels |
| `notebooks/module2_filtering.ipynb` | Part 2: Low-pass filters (mean, median, Gaussian) and high-pass filters (Sobel, Prewitt, Laplacian) |
| `notebooks/module3_transformations.ipynb` | Part 3: Translation, rotation, scaling, shearing, affine, and projective transformations |

## Directory Structure

```
.
├── Images/                  # input images: cv_img1.jpg, cv_img2.jpg
├── notebooks/               # notebooks
├── src/
│   └── config/
│       └── config.py        # all project paths
├── pyproject.toml
└── README.md

```

## Installation and Usage

1. Copy the input images into the `Images/` directory (`cv_img1.jpg`, `cv_img2.jpg`), or update the corresponding filenames in `src/config/config.py`.
2. Create a dedicated virtual environment for this project (the top-level package named `src` might conflict with other projects if sharing an environment), then install the dependencies:

```bash
python -m venv .venv
# Windows:          .venv\Scripts\activate
# Linux / macOS:    source .venv/bin/activate

pip install -e ".[notebook]"
jupyter lab

```

`pip install -e .` registers the `src` package into the environment, allowing notebooks to import it from any directory:

```python
from src.config.config import COLOR_IMAGE_PATH

```

To change the names or locations of the input images, simply modify `src/config/config.py`.
"""
Shared path configuration for the entire project.

"""

from pathlib import Path

# //////////////////////////////////////
# Directories
# //////////////////////////////////////

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SRC_DIR = PROJECT_ROOT / "src"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
IMAGES_DIR = PROJECT_ROOT / "Images"

# //////////////////////////////////////
# Input images for each section
# //////////////////////////////////////

COLOR_IMAGE_PATH = IMAGES_DIR / "cv_img1.jpg"       # Part 1
FILTER_IMAGE_PATH = IMAGES_DIR / "cv_img5.jpg"      # Part 2
TRANSFORM_IMAGE_PATH = IMAGES_DIR / "cv_img6.jpg"   # Part 3
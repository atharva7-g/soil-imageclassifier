import cv2
import numpy as np
import os

from pathlib import Path

root_folder = Path("./data") # change this path

image_files = [f for f in root_folder.glob("**/*") if f.suffix.lower() in [".jpg", ".png", ".jpeg"]]

max_width, max_height = 0, 0
for img_path in image_files:
    img = cv2.imread(str(img_path))
    if img is None:
        continue  # skip unreadable images
    h, w = img.shape[:2]
    max_width = min(max_width, w)
    max_height = min(max_height, h)

print(f"Largest Image Size: {max_width}x{max_height}")






# src/image_loader.py
"""
Simple image loader for JPEG/PNG and DICOM.
Provides an ImageDataset-like interface for PyTorch later.
"""

from pathlib import Path
import cv2
import numpy as np
from typing import List, Tuple, Optional
import pydicom


def read_image(path: Path) -> np.ndarray:
    path = Path(path)
    if path.suffix.lower() in [".dcm"]:
        ds = pydicom.dcmread(str(path))
        arr = ds.pixel_array.astype(np.float32)
    else:
        arr = cv2.imread(str(path), cv2.IMREAD_UNCHANGED).astype(np.float32)
    return arr


def preprocess_image(img: np.ndarray, target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
    # Basic resize and normalization (0-1)
    h, w = img.shape[:2]
    img_resized = cv2.resize(img, (target_size[1], target_size[0]), interpolation=cv2.INTER_AREA)
    # If grayscale produce a 3-channel image
    if img_resized.ndim == 2:
        img_resized = np.stack([img_resized] * 3, axis=-1)
    img_resized = img_resized.astype(np.float32)
    img_resized = img_resized - img_resized.min()
    if img_resized.max() != 0:
        img_resized = img_resized / img_resized.max()
    return img_resized


def list_images(folder: Path, exts: Optional[List[str]] = None) -> List[Path]:
    exts = exts or [".png", ".jpg", ".jpeg", ".dcm"]
    files = []
    for ext in exts:
        files.extend(folder.rglob(f"*{ext}"))
    return sorted(files)

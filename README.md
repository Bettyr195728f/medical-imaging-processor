# Image Loader

A simple Python library for loading and preprocessing medical images.

## Features

- Load JPEG images from directories
- Convert images to normalized float32 arrays
- Resize and pad images to target dimensions
- Basic image information extraction

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --input images --limit 5
```

This will load images from the specified directory and display basic information about each image.

## Project Structure

```
├── src/
│   └── image_loader.py    # Core image loading functionality
├── tests/
│   └── test_image_loader.py # Unit tests
├── main.py                  # Demo script
└── requirements.txt       # Dependencies
```

## API

### `list_images(input_dir: Path) -> list[Path]`
Returns a sorted list of JPEG image files in the specified directory.

### `read_image(path: Path) -> np.ndarray`
Reads an image and converts it to a normalized float32 NumPy array.

### `preprocess_image(img: np.ndarray, target_size: tuple[int, int]) -> np.ndarray`
Resizes and pads an image to the target size while maintaining aspect ratio.

## Running Tests

```bash
python -m unittest discover tests -k image_loader
```

# Image Filter

A simple Python library for applying common filters to medical images.

## Features

- Apply Gaussian blur for noise reduction
- Apply Contrast Limited Adaptive Histogram Equalization (CLAHE) for contrast enhancement

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --input images/person1946_bacteria_4874.jpeg --output output
```

This will load the input image, apply filters, and save the result to the output directory.

## Project Structure

```
├── src/
│   ├── image_loader.py    # Image loading utilities
│   └── image_processor.py # Core image filtering functions
├── tests/
│   └── test_image_filter.py # Unit tests
├── main.py                  # Demo script
└── requirements.txt       # Dependencies
```

## API

### `apply_gaussian_blur(img: np.ndarray, ksize: int = 5) -> np.ndarray`
Applies a Gaussian blur filter to the input image.

### `apply_clahe(img: np.ndarray) -> np.ndarray`
Applies CLAHE to enhance the contrast of the input image.

## Running Tests

```bash
python -m unittest discover tests -k image_filter
```

#!/usr/bin/env python3
"""
Image Filter Main Script

This script demonstrates image filtering functionality.
It loads an image, applies filters, and saves the result.
"""

from pathlib import Path
from src.image_loader import read_image
from src.image_processor import apply_gaussian_blur, apply_clahe, save_image

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Image Filter Demo")
    parser.add_argument("--input", required=True, help="Input image file")
    parser.add_argument("--output", required=True, help="Output directory for filtered image")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_path = output_dir / input_path.name
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Filtering image: {input_path}")
    print(f"Output will be saved to: {output_path}")
    print("-" * 50)
    
    try:
        # Load the image
        img = read_image(input_path)
        print(f"Loaded image with shape: {img.shape}")
        
        # Apply filters
        clahe_img = apply_clahe(img)
        blurred_img = apply_gaussian_blur(clahe_img)
        print("Applied CLAHE and Gaussian blur filters.")
        
        # Save the filtered image
        save_image(output_path, blurred_img)
        print(f"\n✅ Successfully filtered and saved image to: {output_path}")
        
    except Exception as e:
        print(f"\n❌ Error filtering image: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
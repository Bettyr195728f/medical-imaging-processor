#!/usr/bin/env python3
"""
Image Loader Main Script

This script demonstrates image loading functionality.
It loads images from a directory and displays basic information.
"""

from pathlib import Path
from src.image_loader import list_images, read_image

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Image Loader Demo")
    parser.add_argument("--input", required=True, help="Input directory containing images")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of images to load (default: 5)")
    
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    
    print(f"Loading images from: {input_dir}")
    print(f"Limit: {args.limit}")
    print("-" * 50)
    
    try:
        image_files = list_images(input_dir)
        print(f"Found {len(image_files)} image files")
        
        for i, img_path in enumerate(image_files[:args.limit]):
            print(f"\nLoading image {i+1}: {img_path.name}")
            
            # Load the image
            img = read_image(img_path)
            
            # Display basic information
            print(f"  Shape: {img.shape}")
            print(f"  Data type: {img.dtype}")
            print(f"  Min value: {img.min():.3f}")
            print(f"  Max value: {img.max():.3f}")
        
        print(f"\n✅ Successfully loaded {min(len(image_files), args.limit)} images!")
        
    except Exception as e:
        print(f"\n❌ Error loading images: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
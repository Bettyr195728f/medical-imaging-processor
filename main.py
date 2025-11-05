#!/usr/bin/env python3
"""
Pneumonia Detection Main Script

This script runs the pneumonia detection pipeline on chest x-ray images.
It classifies images as either Normal or Pneumonia and saves them to 
separate directories.
"""

from pathlib import Path
from src.pipelines.pipeline import run_pipeline

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Pneumonia Detection Pipeline")
    parser.add_argument("--input", required=True, help="Input directory containing chest x-ray images")
    parser.add_argument("--output", required=True, help="Output directory for processed images")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of images to process (default: 10)")
    
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    output_dir = Path(args.output)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Running pneumonia detection pipeline...")
    print(f"Input: {input_dir}")
    print(f"Output: {output_dir}")
    print(f"Limit: {args.limit}")
    print("-" * 50)
    
    try:
        run_pipeline(input_dir, output_dir, n=args.limit)
        print("\n✅ Pneumonia detection pipeline completed successfully!")
        print(f"Processed images saved to: {output_dir}")
        print("Images are organized into 'Normal' and 'Pneumonia' subdirectories.")
        
    except Exception as e:
        print(f"\n❌ Error running pipeline: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
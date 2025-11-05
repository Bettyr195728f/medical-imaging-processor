import unittest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_processor import apply_gaussian_blur, apply_clahe

class TestImageProcessing(unittest.TestCase):

    def test_apply_gaussian_blur(self):
        # Create a dummy image
        img = np.zeros((100, 100), dtype=np.float32)
        img[50, 50] = 1.0

        # Apply Gaussian blur
        blurred_img = apply_gaussian_blur(img, ksize=5)

        # Check that the output is a valid image
        self.assertEqual(blurred_img.shape, (100, 100))
        self.assertIsInstance(blurred_img, np.ndarray)

    def test_apply_clahe(self):
        # Create a dummy image
        img = np.random.rand(100, 100).astype(np.float32)

        # Apply CLAHE
        enhanced_img = apply_clahe(img)

        # Check that the output is a valid image
        self.assertEqual(enhanced_img.shape, (100, 100))
        self.assertIsInstance(enhanced_img, np.ndarray)

if __name__ == '__main__':
    unittest.main()

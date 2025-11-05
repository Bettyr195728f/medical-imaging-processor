import unittest
from pathlib import Path
import numpy as np
import cv2
from src.image_loader import read_image
from src.image_processor import apply_gaussian_blur, apply_clahe

class TestImageFilter(unittest.TestCase):
    
    def setUp(self):
        self.test_image_dir = Path("images")
        self.test_image_path = self.test_image_dir / "person1946_bacteria_4874.jpeg"
        # Create a dummy image for testing
        self.dummy_image = np.random.rand(100, 100).astype(np.float32)

    def test_apply_gaussian_blur(self):
        """Test that Gaussian blur runs without error and changes the image."""
        blurred = apply_gaussian_blur(self.dummy_image, ksize=5)
        self.assertEqual(self.dummy_image.shape, blurred.shape)
        self.assertFalse(np.array_equal(self.dummy_image, blurred))

    def test_apply_clahe(self):
        """Test that CLAHE runs and enhances contrast."""
        clahe_img = apply_clahe(self.dummy_image)
        self.assertEqual(self.dummy_image.shape, clahe_img.shape)
        # CLAHE should change the image
        self.assertFalse(np.array_equal(self.dummy_image, clahe_img))

if __name__ == '__main__':
    unittest.main()
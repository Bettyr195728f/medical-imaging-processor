import unittest
from pathlib import Path
import numpy as np
from src.image_loader import list_images, read_image, preprocess_image

class TestImageLoader(unittest.TestCase):
    
    def setUp(self):
        self.test_image_dir = Path("images")
        self.test_image_path = self.test_image_dir / "person1946_bacteria_4874.jpeg"
    
    def test_list_images(self):
        """Test that list_images returns a list of image files."""
        images = list_images(self.test_image_dir)
        self.assertIsInstance(images, list)
        self.assertGreater(len(images), 0)
        for img_path in images:
            self.assertTrue(img_path.exists())
            self.assertTrue(img_path.suffix.lower() in ['.jpeg', '.jpg'])
    
    def test_read_image(self):
        """Test that read_image loads an image correctly."""
        if self.test_image_path.exists():
            img = read_image(self.test_image_path)
            self.assertIsInstance(img, np.ndarray)
            self.assertEqual(img.dtype, np.float32)
            self.assertGreaterEqual(img.min(), 0)
            self.assertLessEqual(img.max(), 1.0)
    
    def test_preprocess_image(self):
        """Test that preprocess_image resizes correctly."""
        if self.test_image_path.exists():
            img = read_image(self.test_image_path)
            target_size = (224, 224)
            processed = preprocess_image(img, target_size)
            self.assertEqual(processed.shape, target_size)
            self.assertEqual(processed.dtype, np.float32)

if __name__ == '__main__':
    unittest.main()
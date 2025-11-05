import unittest
import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.classifier import classify_image, preprocess_for_classification

class TestClassifier(unittest.TestCase):

    def test_classify_image_returns_valid_result(self):
        """Test that the classify_image function returns a valid classification."""
        # Use a sample image from the images directory
        image_path = Path("images/person1946_bacteria_4874.jpeg")
        if image_path.exists():
            classification = classify_image(image_path)
            self.assertIn(classification, ["Normal", "Pneumonia"])
        else:
            self.skipTest("Test image not found")

    def test_preprocess_for_classification(self):
        """Test that image preprocessing works correctly."""
        image_path = Path("images/person1946_bacteria_4874.jpeg")
        if image_path.exists():
            try:
                processed_image = preprocess_for_classification(image_path)
                self.assertEqual(processed_image.shape[0], 1)  # Batch size
                self.assertEqual(processed_image.shape[1], 1)  # Grayscale channels
                self.assertEqual(processed_image.shape[2], 224)  # Height
                self.assertEqual(processed_image.shape[3], 224)  # Width
            except Exception as e:
                self.fail(f"Preprocessing failed: {e}")
        else:
            self.skipTest("Test image not found")

if __name__ == '__main__':
    unittest.main()
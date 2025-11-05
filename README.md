# Medical Image Processor

This project is a Python-based medical imaging processor that provides a set of tools for loading, processing, and saving medical images.

## Project Structure

```
├── .gitignore
├── README.md
├── contributers.md
├── dir
├── docs
│   └── problem statement.md
├── images
│   ├── person1946_bacteria_4874.jpeg
│   ├── person1946_bacteria_4875.jpeg
│   ├── person1947_bacteria_4876.jpeg
│   ├── person1949_bacteria_4880.jpeg
│   ├── person1950_bacteria_4881.jpeg
│   ├── person1951_bacteria_4882.jpeg
│   ├── person1952_bacteria_4883.jpeg
│   └── person1954_bacteria_4886.jpeg
├── main.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── image_filter.py
│   ├── image_loader.py
│   ├── image_processor.py
│   └── medical-imaging-oop
│       └── filterpipeline.py
├── test_sample.py
└── tests
```
## How to Run

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   python main.py --input images --output output
   ```

   This will process chest x-ray images and save them into `Normal` and `Pneumonia` subdirectories based on the classification.

## How to Run Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

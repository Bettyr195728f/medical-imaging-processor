import os
import cv2
import glob
import matplotlib.pyplot as plt

# === Step 1: Load and Filter One Image ===
img_path = os.path.join("data", "train", "NORMAL", "IM-0115-0001.jpeg")
image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found.")
    exit()

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(image)
blurred_img = cv2.GaussianBlur(clahe_img, (5, 5), 0)

# === Step 2: Display All Three Images ===
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title("Original")
axs[0].axis('off')

axs[1].imshow(clahe_img, cmap='gray')
axs[1].set_title("CLAHE")
axs[1].axis('off')

axs[2].imshow(blurred_img, cmap='gray')
axs[2].set_title("Gaussian Blur")
axs[2].axis('off')

plt.tight_layout()
plt.show()

# === Step 3: Batch Filter All Images in NORMAL/ ===
input_dir = os.path.join("data", "train", "NORMAL")
output_dir = os.path.join("data", "train", "NORMAL_filtered")
os.makedirs(output_dir, exist_ok=True)

for path in glob.glob(os.path.join(input_dir, "*.jpeg")):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue
    enhanced = clahe.apply(img)
    blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)
    filename = os.path.basename(path)
    out_path = os.path.join(output_dir, filename)
    cv2.imwrite(out_path, blurred)

# === Step 4: Plot Histogram Comparison ===
filtered_path = os.path.join(output_dir, "IM-0115-0001.jpeg")
filtered_img = cv2.imread(filtered_path, cv2.IMREAD_GRAYSCALE)

plt.hist(image.ravel(), bins=256, color='gray', alpha=0.5, label='Original')
plt.hist(filtered_img.ravel(), bins=256, color='blue', alpha=0.5, label='Filtered')
plt.legend()
plt.title("Pixel Intensity Distribution")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

from src.image_loader import list_images, read_image, preprocess_image
from pathlib import Path

images = list_images(Path("data/train/NORMAL_filtered"))
img = read_image(images[0])
proc = preprocess_image(img, target_size=(128, 128))
print("Processed shape:", proc.shape)

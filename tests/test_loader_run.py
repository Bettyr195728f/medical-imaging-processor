from pathlib import Path
from src.image_loader import list_images, read_image, preprocess_image

p = Path('data/chest_xray/train')
imgs = list_images(p)
print('found images:', len(imgs))
if imgs:
    img = read_image(imgs[0])
    print('original shape:', getattr(img,'shape', None))
    proc = preprocess_image(img, target_size=(128,128))
    print('processed shape:', proc.shape, 'min,max:', float(proc.min()), float(proc.max()))
else:
    print('No images found in', p)

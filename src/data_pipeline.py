"""Image preprocessing and the PyTorch Dataset shared across the notebook.

Kept in a real module (not a notebook cell) so DataLoader workers can import it
by path on Windows spawn, instead of re-executing the notebook's __main__.
"""

import random

import numpy as np
import torch
from PIL import Image, ImageEnhance, ImageOps
from torch.utils.data import Dataset

IMAGE_SIZE = 224
IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)

ENABLE_NORMALISATION = True
ENABLE_AUGMENTATION = True


def resize_image(image, size=IMAGE_SIZE):
    image = image.convert("RGB")

    # Pad to a square first so the animal features are not stretched.
    side = max(image.size)
    delta_w, delta_h = side - image.width, side - image.height
    padding = (
        delta_w // 2,
        delta_h // 2,
        delta_w - delta_w // 2,
        delta_h - delta_h // 2,
    )
    image = ImageOps.expand(image, border=padding, fill=(0, 0, 0))
    return image.resize((size, size), Image.BICUBIC)


def normalise_array(image):
    array = np.asarray(image, dtype=np.float32) / 255.0
    if not ENABLE_NORMALISATION:
        return array

    # Rescale an already-resized PIL image to [0, 1] and standardise with ImageNet statistics.
    return (array - IMAGENET_MEAN) / IMAGENET_STD


def normalise_image(image):
    return normalise_array(resize_image(image))


def augment_image(image, rng=random):
    if not ENABLE_AUGMENTATION:
        return resize_image(image)

    # Flip, small rotation and mild brightness/contrast changes keep the class label valid.
    image = resize_image(image)

    if rng.random() < 0.5:
        image = ImageOps.mirror(image)
    image = image.rotate(
        rng.uniform(-10, 10), resample=Image.BICUBIC, fillcolor=(0, 0, 0)
    )

    image = ImageEnhance.Brightness(image).enhance(rng.uniform(0.8, 1.2))
    image = ImageEnhance.Contrast(image).enhance(rng.uniform(0.8, 1.2))

    return image


class CatDogDataset(Dataset):
    def __init__(self, folder, image_ids, labels=None, augment=False):
        self.folder = folder
        self.image_ids = list(image_ids)
        self.labels = None if labels is None else list(labels)
        self.augment = augment

    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, index):
        with Image.open(self.folder / f"{self.image_ids[index]:05d}.jpg") as img:
            img = img.convert("RGB")
            # Augmentation resizes too; otherwise only resize, so every split shares the same preprocessing.
            image = augment_image(img) if self.augment else resize_image(img)
        array = normalise_array(image)
        tensor = torch.from_numpy(array).permute(2, 0, 1)  # HWC -> CHW
        if self.labels is None:
            return tensor
        return tensor, self.labels[index]

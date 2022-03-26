#!/usr/bin/env python
# coding: utf-8

from PIL import Image

import pyheif
import whatimage


def get_image(img_filename):
    with open(img_filename, 'rb') as f:
        image_bytes = f.read()
        img_format = whatimage.identify_image(image_bytes)

    if img_format in ['heic', 'avif']:
        heif_file = pyheif.read(img_filename)
        return Image.frombytes(heif_file.mode, heif_file.size,
            heif_file.data, 'raw', heif_file.mode, heif_file.stride)

    return Image.open(img_filename)

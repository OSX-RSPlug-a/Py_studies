import os
from PIL import Image

def compress_image(image_path, output_path, output_size, quality=85):
    """
    Parameters:
    - output_size: the desired output size of the image, in pixels
    - quality: the image quality, as a percentage (default is 85)
    """
    with Image.open(image_path) as img:
        img = img.resize((output_size, output_size), resample=Image.LANCZOS)
        img.save(output_path, quality=quality, optimize=True)

compress_image('RG_Imagem-0001_131219.png', 'RG_Imagem-0001_131219.png', 128)

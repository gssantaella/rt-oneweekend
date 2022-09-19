# IMPORTS
import numpy as np
from PIL import Image
import os


# CONTANTS
RES_PATH = 'res'
IMG_PATH = os.path.join(RES_PATH, 'img')
IMG_NAME = 'new.png'


# HELPER
def set_structure():
    os.makedirs(IMG_PATH, exist_ok=True)


# MAIN
def main():

    # IMAGE
    IMG_WIDTH = 256
    IMG_HEIGHT = 256

    # RENDER
    print(f'\nWIDTH: {IMG_WIDTH}\nHEIGHT: {IMG_HEIGHT}\n')

    pixels = []
    for j in range(IMG_HEIGHT-1, -1, -1):
        pixels_row = []
        for i in range(IMG_WIDTH):
            r = float(i) / (IMG_WIDTH-1)
            g = float(j) / (IMG_HEIGHT-1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            pixels_row.append((ir,ig,ib))
        pixels.append(pixels_row)


    # create image
    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image_path = os.path.join(IMG_PATH, IMG_NAME)
    new_image.save(new_image_path)
    print(f'IMAGE PATH: {new_image_path}\n')

    return


if __name__ == '__main__':
    set_structure()
    main()
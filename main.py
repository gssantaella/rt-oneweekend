# IMPORTS
import numpy as np
from PIL import Image

import os
import time


# CONTANTS
RES_PATH = 'res'
IMG_PATH = os.path.join(RES_PATH, 'img')
IMG_NAME = 'new1.png'


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

    start = time.time()
    array = create_image_array(IMG_WIDTH, IMG_HEIGHT)

    end = time.time()
    print(f'time numpy: {end-start}\n')
    
    create_image(array, os.path.join(IMG_PATH, IMG_NAME))

    return

def create_image_array(width, height):

    LENGTH = width * height

    xx, yy = np.meshgrid(np.linspace(0, 1, width), np.linspace(1, 0, height))
    z = np.array([0.25] * LENGTH)

    x = xx.flatten() * 255.999
    y = yy.flatten() * 255.999
    z *= 255.999

    return np.stack((x,y,z), axis=1).astype(np.uint8).reshape((height, width, 3))



def create_image(array, img_path):
    new_image = Image.fromarray(array)
    new_image.save(img_path)
    print(f'IMAGE PATH: {img_path}\n')


if __name__ == '__main__':
    set_structure()
    main()
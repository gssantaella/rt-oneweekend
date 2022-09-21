# IMPORTS
import numpy as np
from PIL import Image
from src.vector.vector3 import *
from src.ray.ray import *

import os
import time


# CONTANTS
RES_PATH = 'res'
IMG_FOLDER_PATH = os.path.join(RES_PATH, 'img')
IMG_NAME = 'new4.png'
IMG_PATH = os.path.join(IMG_FOLDER_PATH, IMG_NAME)


# HELPER
def set_structure():
    os.makedirs(IMG_FOLDER_PATH, exist_ok=True)


# FUNCTIONS
def xhit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction.length_squared()
    b = 2. * oc.dot(r.direction)
    c = oc.length_squared() - radius**2
    discriminant = b**2 - 4*a*c
    return discriminant > 0

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction.length_squared()
    b = 2. * oc.dot(r.direction)
    c = oc.length_squared() - radius**2
    discriminant = b**2 - 4*a*c
    return discriminant, a, b

def xray_color(r) -> RGB:
    t = 0.5 * (r.direction.normalize().y + 1.)
    return (1.-t) * RGB(1., 1., 1.) + t * RGB(0.5, 0.7, 1.0)

def ray_color(r,t) -> RGB:
    # t = hit_sphere(Point(0,0,-1), 0.5, r)
    if t > 0.0:
        N = (r.at(t) - Vec3(0,0,-1)).normalize()
        return 0.5 * RGB(N.x+1, N.y+1, N.z+1)
    t = 0.5 * (r.direction.normalize().y + 1.)
    return (1.-t) * RGB(1., 1., 1.) + t * RGB(0.5, 0.7, 1.0)

def shade(r,t):
    # print('1')
    N = (r.at(t) - Vec3(0,0,-1)).normalize()
    s = 0.5 * RGB(N.x+1, N.y+1, N.z+1)
    # print('Ss',s)
    return s
def lerp(r,t):
    # print('3')
    t = 0.5 * (r.direction.normalize().y + 1.)
    s = RGB(1., 1., 1.)*(1.-t) + RGB(0.5, 0.7, 1.0)*t
    # print('Sl',s)
    return s

def create_image_array(width, height, vw, vh, origin, vertical, horizontal, lower_left_corner):

    LENGTH = width * height

    xx, yy = np.meshgrid(np.linspace(0, 1, width), np.linspace(1, 0, height))

    u = Vec3(xx.flatten(), 0, 0)
    v = Vec3(0, yy.flatten(), 0)
    r = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
    p = Point(0,0,-1)

    hits, a, b = hit_sphere(p, 0.5, r)

    mask = (hits < 0)
    hits[~mask] = (-b[~mask] - np.sqrt(hits[~mask]) ) / (2. * a[~mask])
    hits[mask] = -1.

    mask = (hits > 0.0)
    r1 = Ray(r.origin, Vec3(r.direction.x[mask], r.direction.y[mask], -1.0))
    r2 = Ray(r.origin, Vec3(r.direction.x[~mask], r.direction.y[~mask], -1.0))

    a_hit = np.stack(shade(r1, hits[mask]).components(), axis=1)*255.999
    a_not_hit = np.stack(lerp(r2, hits[~mask]).components(), axis=1)*255.999

    mask = np.reshape(mask, (height, width))
    pc = np.empty((height, width, 3), np.uint8)

    pc[mask] = a_hit
    pc[~mask] = a_not_hit

    pixel_color = [(v) for v in pc]
    # print(pixel_color)
    # print(type(pixel_color))

    return np.reshape(pixel_color, (height, width, 3)).astype(np.uint8)
    #return np.stack((x,y,z), axis=1).astype(np.uint8).reshape((height, width, 3))


def create_image(array, IMG_FOLDER_PATH):
    new_image = Image.fromarray(array)
    new_image.save(IMG_FOLDER_PATH)
    print(f'IMAGE PATH: {IMG_FOLDER_PATH}\n')


# MAIN
def main():

    # IMAGE
    ASPECT_RATIO = 16. / 9.
    IMG_WIDTH = 400
    IMG_HEIGHT = int(IMG_WIDTH / ASPECT_RATIO)

    # CAMERA
    viewport_height = 2.
    viewport_width = ASPECT_RATIO * viewport_height
    focal_length = 1.

    origin = Point(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)

    # RENDER
    print(f'\nWIDTH: {IMG_WIDTH}\nHEIGHT: {IMG_HEIGHT}\n')

    start = time.time()
    array = create_image_array(IMG_WIDTH, IMG_HEIGHT, viewport_width, viewport_height, origin, vertical, horizontal, lower_left_corner)
    # print(array)
    end = time.time()
    print(f'time numpy: {end-start}\n')
    
    create_image(array, IMG_PATH)

    print('\nDone!\n')

    return


if __name__ == '__main__':
    
    set_structure()
    main()

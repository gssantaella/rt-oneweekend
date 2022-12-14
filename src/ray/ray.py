from src.vector.vector3 import *
import numbers
import numpy as np

class Ray(object):
    """docstring for Ray"""

    def __init__(self, origin=Point(), direction=Vec3()):
        self.origin = origin
        self.direction = direction

    def __str__(self) -> str:
        return f'ray(ori:{self.origin}, dir:{self.direction})'

    def at(self, t: float) -> Vec3:
            return self.origin + self.direction*t

if __name__ == '__main__':
    r = Ray()
    print(r)
from src.hittable.hittable import Hittable
from src.ray.ray import *
from src.vector.vector3 import *
import numpy as np


class Sphere(Hittable):

    # def __init__(self, p, normal, t, center, radius):
    #     super().__init__(p, normal, t)
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, r, t_min, t_max):
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = oc.dot(r.direction)
        c = oc.length_squared() - self.radius**2
        discriminant = half_b**2 - a*c
        return discriminant, a, half_b
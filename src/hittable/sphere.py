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

    def hitold(self, r, t_min, t_max):
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = oc.dot(r.direction)
        c = oc.length_squared() - self.radius**2
        discriminant = half_b**2 - a*c
        return discriminant, a, half_b
    
    def hit(self, r, t_min, t_max):
        # calcula o delta
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = oc.dot(r.direction)
        c = oc.length_squared() - self.radius**2
        discriminant = half_b**2 - a*c
        
        # realiza bhaskara para encontrar raizes
        # calcula primeiro menor raiz da interseccao, eh sempre a mais proxima da camera
        roots = discriminant.copy()
        mask = (roots < t_min) | (roots > t_max)
        roots[~mask] = (-half_b[~mask] - np.sqrt(roots[~mask]))/a[~mask]
        roots = np.nan_to_num(roots, nan=t_min-1)

        # calcula a segunda raiz apenas para as que precisarem
        # mask = (roots < t_min) | (roots > t_max)
        # roots[mask] = (-half_b[mask] + np.sqrt(roots[mask]))/a[mask]
        # roots = np.nan_to_num(roots, nan=t_min-1)

        # retorna -1 quando nao atinge a esfera
        mask = (roots < t_min) | (roots > t_max)
        roots[mask] = -1

        return roots
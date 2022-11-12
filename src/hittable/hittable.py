from src.ray.ray import *
import numpy as np
from abc import ABC, abstractmethod

class Hittable(ABC):
    """ """
    def __init__(self, p:Point, normal:Vec3, t:float):
        self.p: Point = p
        self.normal: Vec3 = normal
        self.t: float = t
    
    @abstractmethod
    def hit(self, r:Ray, t_min:float, t_max:float):
        pass
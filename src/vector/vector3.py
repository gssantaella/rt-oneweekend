from __future__ import annotations
import numbers
import numpy as np
from math import sqrt


class Vec3(object):
    """Representation of a 3-dimentional vector"""
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'Vec3({self.x}, {self.y}, {self.z})'

    def __eq__(self, v: Vec3) -> bool:
        return self.x == v.x and self.y == v.y and self.z == v.z

    def components(self) -> tuple:
        return (self.x, self.y, self.z)

    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, v: Vec3) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(self.x + v, self.y + v, self.z + v)

    def __radd__(self, v: Vec3) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(v.x + self.x, v.y + self.y, v.z + self.z)
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(v + self.x, v + self.y, v + self.z)

    def __iadd__(self, v: Vec3) -> Vec3:
        self.x += v.x
        self.y += v.y
        self.z += v.z
        return self

    def __sub__(self, v: Vec3) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(self.x - v.x, self.y - v.y, self.z - v.z)
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(self.x - v, self.y - v, self.z - v)

    def __rsub__(self, v: Vec3) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(v.x - self.x, v.y - self.y, v.z - self.z)
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(v - self.x, v - self.y, v - self.z)

    def __isub__(self, v: Vec3) -> Vec3:
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        return self

    def __mul__(self, v) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(v.x * self.x, v.y * self.y, v.z * self.z)
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(v * self.x, v * self.y, v * self.z)

    def __imul__(self, v) -> Vec3:
        if isinstance(v, Vec3):
            self.x *= v.x
            self.y *= v.y
            self.z *= v.z
            return self
        elif isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            self.x *= v
            self.y *= v
            self.z *= v
            return self
        
    def __truediv__(self, v: float) -> Vec3:
        if isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(self.x / v, self.y / v, self.z / v)

    def __rtruediv__(self, v: float) -> Vec3:
        if isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            return Vec3(v / self.x, v / self.y, v / self.z)

    def __itruediv__(self, v: float) -> Vec3:
        if isinstance(v, numbers.Number) or isinstance(v, np.ndarray):
            self.x /= v
            self.y /= v
            self.z /= v
            return self

    def sqrt(v) -> Vec3:
        return Vec3(np.sqrt(v.x), np.sqrt(v.y), np.sqrt(v.z)) 

    def dot(self, v) -> float:
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v: Vec3) -> Vec3:
        return Vec3(self.y * v.z - self.z * v.y,
                    self.z * v.x - self.x * v.z,
                    self.x * v.y - self.y * v.x)

    def length(self) -> float:
        return np.sqrt(self.length_squared())

    def length_squared(self) -> float:
        return self.dot(self)

    def normalize(self) -> Vec3:
        m = self.length()
        return self * (1.0 / np.where(m == 0, 1, m))


RGB = Vec3
Point = Vec3
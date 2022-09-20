import unittest
import numpy as np
from src.vector.vector3 import *


class TestVec3(unittest.TestCase):

    def test_components(self):
        v = Vec3(1,2,3)
        self.assertEqual(v.components(), (1,2,3))

    def test_equality(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(1,2,3)
        self.assertEqual(v1, v2)

    def test_negation(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(-1,-2,-3)
        self.assertEqual(-v1, v2)

    def test_addition(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(2,4,6)
        v3 = Vec3(3,6,9)
        self.assertEqual(v1+v2, v3)

    def test_addition_scalar(self):
        v1 = Vec3(1,2,3)
        n = 2
        self.assertEqual(v1+n, Vec3(3,4,5))

    def test_iaddition(self):
        v1 = Vec3(1,2,3)
        v1 += v1
        v2 = Vec3(2,4,6)
        self.assertEqual(v1, v2)

    def test_subtraction(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(2,4,6)
        self.assertEqual(v2-v1, v1)

    def test_isubtraction(self):
        v1 = Vec3(1,2,3)
        v1 -= v1
        v2 = Vec3(0,0,0)
        self.assertEqual(v1, v2)

    def test_multiplication_vector(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(1,4,9)
        self.assertEqual(v1*v1, v2)

    def test_multiplication_scalar(self):
        v1 = Vec3(1,2,3)
        t = 5
        self.assertEqual(v1*t, Vec3(5,10,15))

    def test_imultiplication_vector(self):
        v1 = Vec3(1,2,3)
        v1 *= v1
        v2 = Vec3(1,4,9)
        self.assertEqual(v1, v2)

    def test_imultiplication_scalar(self):
        v1 = Vec3(1,2,3)
        v1 *= 3
        v2 = Vec3(3,6,9)
        self.assertEqual(v1, v2)

    def test_division(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(0.5,1.,1.5)
        self.assertEqual(v1 / 2, v2)

    def test_idivision(self):
        v1 = Vec3(1,2,3)
        v1 /= 2.
        v2 = Vec3(0.5,1.,1.5)
        self.assertEqual(v1, v2)

    def test_length_squared(self):
        v1 = Vec3(1,2,3)
        self.assertEqual(v1.length_squared(), 14)

    def test_length(self):
        v1 = Vec3(1,2,3)
        t = 14 ** 0.5
        self.assertEqual(v1.length(), t)

    def test_dot(self):
        v1 = Vec3(3,3,3)
        v2 = Vec3(2,2,2)
        self.assertEqual(v1.dot(v2), 18)

    def test_cross(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(2,4,6)
        self.assertEqual(v1.cross(v2), Vec3(0,0,0))

    def test_normalize(self):
        v1 = Vec3(1,2,3)
        self.assertEqual(v1.normalize(), Vec3(0.2672612419124244, 0.5345224838248488, 0.8017837257372732))

if __name__ == '__main__':
    unittest.main()
import unittest

from src.vector.vector3 import *
from src.ray.ray import *


class TestRay(unittest.TestCase):

    def test_at(self):
        r = Ray(Vec3(1,1,0), Vec3(3,4,5))
        t = 10
        self.assertEqual(r.at(t), Vec3(31,41,50))

    
import unittest
from circle import area
from circle import perimeter
from math import pi


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10), 10 * 10 * pi)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(-1), "error")

    def test_perimetr(self):
        self.assertEqual(perimeter(10), 2 * pi * 10)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(-1), "error")

if __name__ == '__main__':
    unittest.main()

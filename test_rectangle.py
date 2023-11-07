import unittest
from rectangle import area
from rectangle import perimeter


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 5), 50)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(-1, 5), "error")

    def test_perimetr(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(0, 5), "error")
        self.assertEqual(perimeter(-1, 5), "error")


if __name__ == '__main__':
    unittest.main()

import unittest

from rectangle import area, perimeter


class TestRectangle(unittest.TestCase):
    def test_rectangle_area_1(self):
        a, b = 4, 6
        result = area(a, b)
        self.assertEqual(result, 24)

    def test_rectangle_perimeter_1(self):
        a, b = 4, 6
        result = perimeter(a, b)
        self.assertEqual(result, 20)

    def test_rectangle_area_2(self):
        a, b = 490, 631
        result = area(a, b)
        self.assertEqual(result, 309190)

    def test_rectangle_perimeter_2(self):
        a, b = 490, 631
        result = perimeter(a, b)
        self.assertEqual(result, 2242)

    def test_rectangle_area_3(self):
        a, b = 45.3, 61.23
        result = area(a, b)
        self.assertEqual(result, 2773.7189999999996)

    def test_rectangle_perimeter_3(self):
        a, b = 45.3, 61.23
        result = perimeter(a, b)
        self.assertEqual(result, 213.06)

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            area("invalid", "")

        with self.assertRaises(TypeError):
            perimeter("invalid", "")


if __name__ == "__main__":
    unittest.main()

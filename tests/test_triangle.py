import unittest

from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_triangle_area_1(self):
        a, h = 7, 14
        result = area(a, h)
        self.assertEqual(result, 49.0)

    def test_triangle_perimeter_1(self):
        a, b, c = 5, 12, 13
        result = perimeter(a, b, c)
        self.assertEqual(result, 30)

    def test_triangle_area_2(self):
        a, h = 128, 2048
        result = area(a, h)
        self.assertEqual(result, 131072.0)

    def test_triangle_perimeter_2(self):
        a, b, c = 1427, 2048, 3656
        result = perimeter(a, b, c)
        self.assertEqual(result, 8131)

    def test_triangle_area_3(self):
        a, h = 78.25, 15.8
        result = area(a, h)
        self.assertEqual(result, 617.75)

    def test_triangle_perimeter_3(self):
        a, b, c = 6.2, 7.5, 9.1
        result = perimeter(a, b, c)
        self.assertEqual(result, 22.8)

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            area("invalid", "")

        with self.assertRaises(TypeError):
            perimeter("invalid", "")


if __name__ == "__main__":
    unittest.main()


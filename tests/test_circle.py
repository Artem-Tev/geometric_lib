import unittest

from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_circle_area_1(self):
        r = 6
        result = area(r)
        self.assertAlmostEqual(result, 113.09733552923255, places=5)

    def test_circle_perimeter_1(self):
        r = 6
        result = perimeter(r)
        self.assertAlmostEqual(result, 37.69911184307752, places=5)

    def test_circle_area_2(self):
        r = 100000
        result = area(r)
        self.assertAlmostEqual(result, 31415926535.89793, places=5)

    def test_circle_perimeter_2(self):
        r = 100000
        result = perimeter(r)
        self.assertAlmostEqual(result, 628318.5307179586, places=5)

    def test_circle_area_3(self):
        r = 2.5
        result = area(r)
        self.assertAlmostEqual(result, 19.634954084936208, places=5)

    def test_circle_perimeter_3(self):
        r = 2.5
        result = perimeter(r)
        self.assertAlmostEqual(result, 15.707963267948966, places=5)

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            area("invalid")

        with self.assertRaises(TypeError):
            perimeter("invalid")


if __name__ == "__main__":
    unittest.main()

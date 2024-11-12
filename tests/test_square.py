import unittest

from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_square_area_1(self):
        a = 5
        result = area(a)
        self.assertEqual(result, 25)

    def test_square_perimeter_1(self):
        a = 5
        result = perimeter(a)
        self.assertEqual(result, 20)

    def test_square_area_2(self):
        a = 104857
        result = area(a)
        self.assertEqual(result, 10995187249)

    def test_square_perimeter_2(self):
        a = 104857
        result = perimeter(a)
        self.assertEqual(result, 419428)

    def test_square_area_3(self):
        a = 21.78
        result = area(a)
        self.assertEqual(result, 474.3684)

    def test_square_perimeter_3(self):
        a = 21.78
        result = perimeter(a)
        self.assertEqual(result, 87.12)

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            area("invalid")

        with self.assertRaises(TypeError):
            perimeter("invalid")


if __name__ == "__main__":
    unittest.main()


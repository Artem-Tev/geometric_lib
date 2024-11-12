import unittest
from calculate import calc


class TestCalc(unittest.TestCase):

    def test_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [7]
        result = calc(fig, size, func)
        self.assertAlmostEqual(result, 43.9823, places=4)

    def test_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [7]
        result = calc(fig, size, func)
        self.assertAlmostEqual(result, 153.9380, places=4)

    def test_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [6]
        result = calc(fig, size, func)
        self.assertEqual(result, 24)

    def test_square_area(self):
        fig = 'square'
        func = 'area'
        size = [6]
        result = calc(fig, size, func)
        self.assertEqual(result, 36)

    def test_invalid_figure(self):
        fig = 'hexagon'
        func = 'area'
        size = [6, 6, 6]
        with self.assertRaises(AssertionError):
            calc(fig, size, func)

    def test_invalid_function(self):
        fig = 'circle'
        func = 'diameter'
        size = [7]
        with self.assertRaises(AssertionError):
            calc(fig, size, func)

    def test_invalid_size_parameter(self):
        fig = 'square'
        func = 'area'
        size = ['invalid_size']
        with self.assertRaises(TypeError):
            calc(fig, size, func)


if __name__ == "__main__":
    unittest.main()

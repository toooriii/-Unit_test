import unittest
from triangle import area, perimeter, area_by_sides
import math

class TriangleTestCase(unittest.TestCase):
    # Тесты для функции area
    def test_area_positive(self):
        self.assertAlmostEqual(area(10, 5), 25.0, places=5)
        self.assertAlmostEqual(area(7.5, 4.3), 16.125, places=5)

    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 5)
        with self.assertRaises(ValueError):
            area(10, -5)

    # Тесты для функции perimeter
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(6.5, 7.5, 8.5), 22.5)

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)  # Невозможный треугольник
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    # Тесты для функции area_by_sides
    def test_area_by_sides_positive(self):
        self.assertAlmostEqual(area_by_sides(3, 4, 5), 6.0, places=5)
        self.assertAlmostEqual(area_by_sides(6.5, 7.5, 8.5), 23.092, places=3)

    def test_area_by_sides_invalid(self):
        with self.assertRaises(ValueError):
            area_by_sides(1, 2, 10)  # Невозможный треугольник
        with self.assertRaises(ValueError):
            area_by_sides(-3, 4, 5)

if __name__ == '__main__':
    unittest.main()

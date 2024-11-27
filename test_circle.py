import unittest
from circle import area, circumference
import math

class CircleTestCase(unittest.TestCase):
    # Тесты для функции area
    def test_area_positive(self):
        self.assertAlmostEqual(area(1), math.pi, places=5)
        self.assertAlmostEqual(area(2), 4 * math.pi, places=5)
        self.assertAlmostEqual(area(0.5), 0.25 * math.pi, places=5)
    
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-1)
    
    # Тесты для функции circumference
    def test_circumference_positive(self):
        self.assertAlmostEqual(circumference(1), 2 * math.pi, places=5)
        self.assertAlmostEqual(circumference(2), 4 * math.pi, places=5)
        self.assertAlmostEqual(circumference(0.5), math.pi, places=5)
    
    def test_circumference_zero(self):
        self.assertEqual(circumference(0), 0)
    
    def test_circumference_negative(self):
        with self.assertRaises(ValueError):
            circumference(-1)

if __name__ == '__main__':
    unittest.main()

import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    # Тесты для функции area
    def test_area_positive(self):
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(2.5, 4), 10.0)
    
    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(10, 0), 0)
    
    def test_area_negative(self):
        self.assertEqual(area(-5, 10), -50)
        self.assertEqual(area(5, -10), -50)
    
    # Тесты для функции perimeter
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(2.5, 4), 13.0)
    
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(10, 0), 20)
    
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5, 10), 10)
        self.assertEqual(perimeter(5, -10), -10)

if __name__ == '__main__':
    unittest.main()

import math

def area(base, height):
    """Вычисление площади треугольника."""
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return 0.5 * base * height

def perimeter(a, b, c):
    """Вычисление периметра треугольника."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Сумма двух сторон должна быть больше третьей")
    return a + b + c

def area_by_sides(a, b, c):
    """Вычисление площади треугольника по трём сторонам (формула Герона)."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if a + b <= c

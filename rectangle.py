def area(a, b):
    '''Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b'''
    if a >= 0 and type(a) in [int, float] and b >= 0 and type(b) in [int, float]:
        return a * b
    else:
        return "error"


def perimeter(a, b):
    '''Принимает числа a и b, возвращает периметр прямоугольника со сторонами a и b'''
    if a > 0 and type(a) in [int, float] and b > 0 and type(b) in [int, float]:
        return (a + b) * 2
    else:
        return "error"

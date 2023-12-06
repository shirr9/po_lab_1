import math

'''Импортируем библиотекуjlknjkn math'''


def area(r):
    '''Принимает число r, возвращает площадь круга с радиусом r'''
    if r >= 0 and type(r) in [int, float]:
        return math.pi * r * r
    else:
        return "error"


def perimeter(r):
    '''Принимает число r, возвращает длину окружности с радиусом r'''
    if r >= 0 and type(r) in [int, float]:
        return 2 * math.pi * r
    else:
        return "error"

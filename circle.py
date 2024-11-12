import math

def area(r):
    '''
    Принимает радиус окружности (int или float).
    Возводит этот радиус в квадрат и умножает на число пи.
    Параметры:
        r (int или float): радиус окружности
    Возвращаемое значение:
        площадь круга (float)
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Argument must be an int or float")
    return math.pi * abs(r) * abs(r)

def perimeter(r):
    '''
    Принимает радиус окружности (int или float).
    Умножает радиус на 2 и на число пи. Возвращает -inf для -inf.
    Параметры:
        r (int или float): радиус окружности
    Возвращаемое значение:
        периметр круга (float)
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Argument must be an int or float")
    if r == float('-inf'):
        return float('-inf')
    return 2 * math.pi * abs(r)
print(area(6), perimeter(6))
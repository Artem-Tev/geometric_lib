def area(a, h):
    """
    Принимает основание a и высоту h треугольника (int или float).
    Возвращает половину произведения a и h (площадь треугольника) (int или float).
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Неверный тип данных")
    return 0.5 * a * h


def perimeter(a, b, c):
    """
    Принимает длины сторон a, b и c треугольника (int или float).
    Возвращает сумму a, b и c (периметр треугольника) (int или float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Неверный тип данных")
    return a + b + c

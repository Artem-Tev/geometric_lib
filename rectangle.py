def area(a, b):
    """
    Принимает длину a и ширину b прямоугольника (int или float).
    Возвращает произведение a и b (площадь прямоугольника) (int или float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Неверный тип данных")
    return a * b


def perimeter(a, b):
    """
    Принимает длину a и ширину b прямоугольника (int или float).
    Возвращает удвоенную сумму a и b (периметр прямоугольника) (int или float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Неверный тип данных")
    return 2 * (a + b)

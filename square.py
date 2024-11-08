def area(a):
    '''
    Принимает сторону квадрата a (int или float).
    Возвращает квадрат стороны a (площадь квадрата) (int или float).
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Неверный тип данных")
    return a * a

def perimeter(a):
    '''
    Принимает сторону квадрата a (int или float).
    Возвращает сторону a, умноженную на 4 (периметр квадрата) (int или float).
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Неверный тип данных")
    return 4 * a

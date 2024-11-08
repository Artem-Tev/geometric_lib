import pytest
from square import area, perimeter  # замените `your_module` на имя вашего файла без расширения .py


def test_area():
    assert area(1) == 1
    assert area(0) == 0
    assert area(2.5) == pytest.approx(6.25, 0.0001)
    assert area(-3) == pytest.approx(9, 0.0001)  # отрицательное значение стороны
    assert area(float('inf')) == float('inf')
    assert area(float('-inf')) == float('inf')

    # Проверка обработки некорректных типов данных
    with pytest.raises(TypeError):
        area("string")
    with pytest.raises(TypeError):
        area(None)


def test_perimeter():
    assert perimeter(1) == 4
    assert perimeter(0) == 0
    assert perimeter(2.5) == pytest.approx(10, 0.0001)
    assert perimeter(-3) == pytest.approx(-12, 0.0001)  # отрицательное значение стороны
    assert perimeter(float('inf')) == float('inf')
    assert perimeter(float('-inf')) == float('-inf')

    # Проверка обработки некорректных типов данных
    with pytest.raises(TypeError):
        perimeter("string")
    with pytest.raises(TypeError):
        perimeter(None)

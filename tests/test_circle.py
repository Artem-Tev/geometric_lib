import pytest
import math
from circle import area, perimeter  # Замените `your_circle_module` на имя файла с функциями для окружности


def test_area():
    # Основные тесты
    assert area(1) == pytest.approx(math.pi, 0.0001)
    assert area(0) == 0
    assert area(2.5) == pytest.approx(math.pi * 2.5 * 2.5, 0.0001)
    assert area(-3) == pytest.approx(math.pi * 3 * 3, 0.0001)  # проверка на отрицательный радиус

    # Граничные значения
    assert area(float('inf')) == float('inf')
    assert area(float('-inf')) == float('inf')

    # Проверка обработки некорректных типов данных
    with pytest.raises(TypeError):
        area("string")
    with pytest.raises(TypeError):
        area(None)


def test_perimeter():
    # Основные тесты
    assert perimeter(1) == pytest.approx(2 * math.pi, 0.0001)
    assert perimeter(0) == 0
    assert perimeter(2.5) == pytest.approx(2 * math.pi * 2.5, 0.0001)
    assert perimeter(-3) == pytest.approx(2 * math.pi * 3, 0.0001)  # проверка на отрицательный радиус

    # Граничные значения
    assert perimeter(float('inf')) == float('inf')
    assert perimeter(float('-inf')) == float('-inf')

    # Проверка обработки некорректных типов данных
    with pytest.raises(TypeError):
        perimeter("string")
    with pytest.raises(TypeError):
        perimeter(None)

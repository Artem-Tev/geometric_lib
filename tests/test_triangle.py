import pytest
from triangle import area, perimeter

def test_area():
    # Основные тесты
    assert area(3, 4) == 6
    assert area(0, 5) == 0
    assert area(2.5, 4) == pytest.approx(5.0, 0.0001)
    assert area(-3, 4) == pytest.approx(-6.0, 0.0001)

    # Тесты с бесконечностью
    assert area(float('inf'), 1) == float('inf')
    assert area(1, float('inf')) == float('inf')
    assert area(float('-inf'), 1) == float('-inf')
    assert area(1, float('-inf')) == float('-inf')

    # Тесты на исключения
    with pytest.raises(TypeError):
        area("string", 3)
    with pytest.raises(TypeError):
        area(2, "string")
    with pytest.raises(TypeError):
        area(None, 3)
    with pytest.raises(TypeError):
        area(2, None)

def test_perimeter():
    # Основные тесты
    assert perimeter(3, 4, 5) == 12
    assert perimeter(0, 0, 0) == 0
    assert perimeter(2.5, 4, 3.5) == pytest.approx(10.0, 0.0001)
    assert perimeter(-3, 4, 5) == 6

    # Тесты с бесконечностью
    assert perimeter(float('inf'), 1, 2) == float('inf')
    assert perimeter(1, float('inf'), 2) == float('inf')
    assert perimeter(1, 2, float('inf')) == float('inf')
    assert perimeter(float('-inf'), 1, 2) == float('-inf')

    # Тесты на исключения
    with pytest.raises(TypeError):
        perimeter("string", 3, 4)
    with pytest.raises(TypeError):
        perimeter(3, "string", 4)
    with pytest.raises(TypeError):
        perimeter(3, 4, None)

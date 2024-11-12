import pytest
from rectangle import area, perimeter

def test_area():
    # Основные тесты
    assert area(2, 3) == 6
    assert area(0, 5) == 0
    assert area(2.5, 4) == pytest.approx(10.0, 0.0001)
    assert area(-3, 4) == -12

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
    assert perimeter(2, 3) == 10
    assert perimeter(0, 5) == 10
    assert perimeter(2.5, 4) == pytest.approx(13.0, 0.0001)
    assert perimeter(-3, 4) == 2

    # Тесты с бесконечностью
    assert perimeter(float('inf'), 1) == float('inf')
    assert perimeter(1, float('inf')) == float('inf')
    assert perimeter(float('-inf'), 1) == float('-inf')
    assert perimeter(1, float('-inf')) == float('-inf')

    # Тесты на исключения
    with pytest.raises(TypeError):
        perimeter("string", 3)
    with pytest.raises(TypeError):
        perimeter(2, "string")
    with pytest.raises(TypeError):
        perimeter(None, 3)
    with pytest.raises(TypeError):
        perimeter(2, None)

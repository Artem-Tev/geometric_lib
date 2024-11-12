import pytest
from calculate import calc

@pytest.mark.parametrize("fig, func, size, expected", [
    ('circle', 'perimeter', [5], 31.4159),
    ('circle', 'area', [5], 78.5398),
    ('square', 'perimeter', [4], 16),
    ('square', 'area', [4], 16),
])
def test_calc_valid(fig, func, size, expected):
    result = calc(fig, func, size)
    if isinstance(expected, float):
        assert pytest.approx(result, rel=1e-4) == expected
    else:
        assert result == expected

@pytest.mark.parametrize("fig, func, size", [
    ('triangle', 'area', [5, 5, 5]),
    ('circle', 'volume', [5]),
])
def test_calc_invalid_inputs(fig, func, size):
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_invalid_size_parameter():
    fig = 'square'
    func = 'area'
    size = ['invalid_size']
    with pytest.raises(TypeError):
        calc(fig, func, size)

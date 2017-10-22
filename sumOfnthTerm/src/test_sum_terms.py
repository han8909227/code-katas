# Test #
import pytest


@pytest.mark.parametrize('num, result', [(1, '1.00'), (2, '1.25'), (3, '1.39'), (4, '1.49'), (5, '1.57'), (6, '1.63')])
def test_sum_series(num, result):
    """test sum series function"""
    from sum_terms import series_sum
    assert series_sum(num) == result

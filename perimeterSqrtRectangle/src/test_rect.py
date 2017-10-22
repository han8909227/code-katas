import pytest


@pytest.mark.parametrize('side, result', [(5, 80), (7, 216), (20, 114624), (30, 14098308), (100, 6002082144827584333104), (8, 352), (22, 300096), (120, 90793496208027455827902724)])
def test_rect(side, result):
    """."""
    from rect import perimeter
    assert perimeter(side) == result

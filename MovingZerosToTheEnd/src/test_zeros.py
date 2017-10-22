import pytest


@pytest.mark.parametrize('array, result', [([1, 2, 3, 4, 5, 0, 9, 9, 9], [1, 2, 3, 4, 5, 9, 9, 9, 0]),
(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9],["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]),
([0,1,None,2,False,1,0],[1,None,2,False,1,0,0]), (["a","b"], ["a","b"]), (["a"],["a"]), ([0,0],[0,0]),
([0],[0]), ([],[])])
def test_move_zeros(array, result):
    """."""
    from zeros import move_zeros
    assert move_zeros(array) == result

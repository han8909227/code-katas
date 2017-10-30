"""Test the paren validation function."""
from parenthetics import paren


def test_good_pairs():
    """Will test if a good combo of parens is accepted."""
    assert paren('((()()()))') == 0


def test_no_closing_pairs():
    """Will test if a bad combo (no closing paren) returns 1."""
    assert paren('(()()') == 1


def test_no_open_pairs():
    """Will test if a bad combo (no open parens) returns -1."""
    assert paren('()())') == -1

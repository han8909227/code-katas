"""Test for the sort_card kata."""
from sort_cards import sort_cards
import pytest


def test_for_accuracy_1():
    """Test the accuracy of the sort card method."""
    result = sort_cards(list('39A5T824Q7J6K'))
    assert result == list('A23456789TJQK')


def test_for_accuracy_2():
    """Test the accuracy of the sort card method."""
    result = sort_cards(list('Q286JK395A47T'))
    assert result == list('A23456789TJQK')


def test_for_accuracy_3():
    """Test the accuracy of the sort card method."""
    result = sort_cards(list('54TQKJ69327A8'))
    assert result == list('A23456789TJQK')


def test_for_accuracy_4():
    """Test the accuracy of the sort card method."""
    result = sort_cards(list('765432A'))
    assert result == list('A234567')


def test_for_accuracy_5():
    """Test the accuracy of the sort card method."""
    result = sort_cards(list('32A'))
    assert result == list('A23')


def test_for_accuracy_6():
    """Test the accuracy of the sort card method."""
    result = sort_cards(list('32A654'))
    assert result == list('A23456')


def test_invalid_card():
    """Test if we can sort invalid cards."""
    with pytest.raises(ValueError):
        sort_cards(list('0FWTQ'))


def test_invalid_card_1():
    """Test if we can sort invalid cards."""
    with pytest.raises(ValueError):
        sort_cards(list('~+_,.'))


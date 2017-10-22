import pytest

# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)


@pytest.mark.parametrize('str, result', [('    (', False), (')test', False), ('', True), ('hi())(', False), ('hi(hi)()', True), ('mytest)()()))', False), ('((mytest))', True)])
def test_valid_parens(str, result):
    """."""
    from parens import valid_parentheses
    assert valid_parentheses(str) == result

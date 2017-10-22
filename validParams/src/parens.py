"""Kata: Valid Parentheses - determine if a set of parentheses is valid

#1 Best Practices Solution by albarralnunez and others

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
"""


def valid_parentheses(string):
    """."""
    stack = []
    for i in string:
        if i == '(':
            stack.append(0)
        elif i == ')':
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []

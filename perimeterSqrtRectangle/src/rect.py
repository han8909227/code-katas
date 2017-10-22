"""Kata: Parameters of squares in a rectangle - determine the parameters of all the squares in a rectangle

#1 Best Practices Solution by EarlGrey

def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b
        else:
            a, b = b, a+b
            yield b

def perimeter(n):
    return sum(fib(n)) * 4
"""


def perimeter(n):
    """."""
    p = 1
    a = 0
    b = 1
    for i in range(n):
        p += a + b
        c = a
        a = b
        b += c
    return p * 4

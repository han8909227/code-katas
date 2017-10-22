"""Kata: Sum of nth series - find the sum of a series up to the nth term

#1 Best Practices Solution by MMMAAANNN and others

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Find the sum of a series up to nth term"""
    sum = 1.00
    if n < 1:
        return '0.00'
    if n == 1:
        return '1.00'
    for num in range(2, n + 1):
        sum += 1.00 / (3 * num - 2)

    return '{:.2f}'.format(sum)

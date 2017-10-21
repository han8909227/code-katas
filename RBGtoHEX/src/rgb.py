"""Kata: RGB to Hex Conversion - Given RGB format color return valid it valid Hex format

#1 Best Practices Solution by yanykin

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""


def rgb(r, g, b):
    """."""
    col = [max(min(x, 255), 0) for x in [r, g, b]]
    return ''.join([hex(i)[2:].upper() if i > 16 else "0" + hex(i)[2:] for i in col])


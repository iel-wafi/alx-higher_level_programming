#!/us/bin/python3
"""
This is the module of "0-add_integer".
0-add_integer is module supplies one, add_integer(a, b).
"""


def add_integer(a, b=98):

    """Return addition of tow numbers."""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

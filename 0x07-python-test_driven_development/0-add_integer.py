#!/usr/bin/python3
"""
Module 0-add_integer
Accepts two values and casts them into integers
Returns the sum of those integers
"""


def add_integer(a, b=98):
    """
    Returns an integer sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

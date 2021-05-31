#!/usr/bin/python3
"""
Module 4-inherits_from
instance of a class that inherited from a specific class
directly or indirectly
"""


def inherits_from(obj, a_class):
    """Returns true if inherited"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

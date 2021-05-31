#!/usr/bin/python3
"""
Module 2-is_same_class
checks the instance of a specific class
returns true if found
"""


def is_same_class(obj, a_class):
    """returns true if instance of a class"""
    return type(obj) == a_class

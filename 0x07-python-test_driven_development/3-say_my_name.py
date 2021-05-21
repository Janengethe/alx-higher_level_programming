#!/usr/bin/python3
"""
Module 3-say_my_name
Prints the first and last name
Returns the name in str
"""


def say_my_name(first_name, last_name=""):
    """
    Returns the first and last name as long as they are str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

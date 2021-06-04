#!/usr/bin/python3
"""
Module base

Defined by private class attribute __nb_objects
"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of class constructors"""
        if id:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

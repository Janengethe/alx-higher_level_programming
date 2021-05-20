#!/usr/bin/python3
"""
Module 4-square
Defines a square by private attribute size,

"""


class Square:
    """
    Creates class
    Functions:
        __init__(self, size=0)
        size(self)
        size(self, value)
        area(self)
    """
    def __init__(self, size=0):
        """private instance attribute - size"""
        if type(size)is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """"getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of a square
        Returns the area
        """
        return (self.__size)**2

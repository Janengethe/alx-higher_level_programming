#!/usr/bin/python3
"""
Module 102-square
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

        if type(value) is not int or float:
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

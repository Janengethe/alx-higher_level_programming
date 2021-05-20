#!/usr/bin/python3
"""
Module 3-square
Defines a square with private attribute size and public
attribute area
"""


class Square:
    """created class"""
    def __init__(self, size=0):
        """private instance attribute - size"""
        if type(size)is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates area of a square
        Returns the area
        """
        return (self.__size)**2

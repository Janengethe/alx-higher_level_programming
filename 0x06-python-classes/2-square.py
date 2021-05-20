#!/usr/bin/python3
"""
Module 2-square
Defines a square by private attribute size and validates size
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

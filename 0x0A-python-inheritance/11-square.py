#!/usr/bin/python3
"""
Module 11-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
        __str___(self)
    """
    def __init__(self, size):
        """initializes size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """allows print to print"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

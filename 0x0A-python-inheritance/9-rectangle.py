#!/usr/bin/python3
"""
Module 9-rectangle
inherits from class BaseGeometry
and initializes
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits frpm BaseGeometry
    methods:
    __init__(self, width, height)
    area(self)
    __str__(self)
    """

    def __init__(self, width, height):
        """
        initialization of width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Implements the area"""
        return self.__width * self.__height

    def __str__(self):
        """Allows print to print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

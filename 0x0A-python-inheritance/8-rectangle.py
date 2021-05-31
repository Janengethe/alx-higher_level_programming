#!/usr/bin/python3
"""
Module 8-rectangle
inherits from class BaseGeometry
and initializes
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits frpm BaseGeometry"""
    def __init__(self, width, height):
        """
        initialization of width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

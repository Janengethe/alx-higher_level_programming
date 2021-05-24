#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle
Initializes width and height
"""


class Rectangle:
    """
    private attributes width and height
    Arguments:
        width
        height
    Methods:
        __init__(self, width=0, height= 0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter, to retieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, to set width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter, to retieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter, to set height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

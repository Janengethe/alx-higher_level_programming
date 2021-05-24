#!/usr/bin/python3
"""
Module 7-rectangle
Defines a rectangle with private instance attributes
width and height and public area and perimeter
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
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter, to retieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, to set width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ Prints rectangle with #'s """
        if self.width == 0 or self.height == 0:
            return ""
        i = "\n".join([str(self.print_symbol) * self.width
                       for rows in range(self.height)])
        return i

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """deleted instance of a class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

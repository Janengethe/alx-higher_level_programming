#!/usr/bin/python3
"""Module 5-square"""


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
        return (self.__size)**2

    def my_print(self):
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))

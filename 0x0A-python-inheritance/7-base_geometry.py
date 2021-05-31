#!/usr/bin/python3
"""
Module 7-base_geometry

Has a public instance methods
"""


class BaseGeometry:
    """With public instance method
    methods:
    area(self)
    integer_validator(self, name, value)
    """
    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

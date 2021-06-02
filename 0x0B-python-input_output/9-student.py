#!/usr/bin/python3
"""
Module 9-student
Defines a student by public instance attributes:
first_name, last_name and age
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """etrieves a dict representation of a Student instance"""
        return self.__dict__

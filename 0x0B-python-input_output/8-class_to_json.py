#!/usr/bin/python3
"""
Module 10-class_to_json
Contains function that
returns dictionary description with simple data structure
(list, dictionary, dictionary, string)
for JSON serialization of an object
"""


def class_to_json(obj):
    return obj.__dict__

#!/usr/bin/python3
"""
Module base

Defined by private class attribute __nb_objects
"""


import json

class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of class constructors"""
        if id:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
        list dictionary
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        list_objs is a list of instances who inherits of Base
        """
        objs = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for ob in list_objs:
                objs.append(cls.to_dictionary(ob))
            with open(filename, "w") as f:
                f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Return list of json string representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        lists = []
        filename = cls.__name__ + ".json"
        

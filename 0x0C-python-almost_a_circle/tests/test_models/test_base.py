#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """Total tests = 14"""
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_id_given(self):
        """Tests the matching of id given"""
        self.assertTrue(Base(100), self.id == 100)
        self.assertTrue(Base(-1), self.id == -1)
        self.assertTrue(Base(87432), self.id == 87432)
        self.assertTrue(Base(0), self.id == 0)

    def test_id_is_none(self):
        """Test id will be assigned the increment value
        of private class attribute __nb_objects
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_invalid_args(self):
        """Tests more than one args given"""
        with self.assertRaises(TypeError):
            Base(10, 13)

    def test_private_att_access(self):
        """Tests access of private attribute"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects
            Base.nb_objects
            Base._nb_objects

    def test_class(self):
        """Test whether class is Base"""
        self.assertTrue(Base(2), self.__class__ == Base)

    def test_to_json_string(self):
        """Tests JSON string representation of a dict"""
        dic1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        dic2 = {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}
        string = Base.to_json_string([dic1, dic2])
        self.assertTrue(type(dic1) == dict)
        self.assertTrue(type(dic2) == dict)
        self.assertTrue(type(string) == str)
        self.assertTrue(string,
                        [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
                         {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}])

    def test_empty_to_json_string(self):
        """Tests when the dict is empty"""
        dic3 = {}
        stri = Base.to_json_string([dic3])
        self.assertTrue(type(stri) == str)
        self.assertTrue(len(dic3) == 0)
        self.assertTrue(stri, [])

    def test_none_to_json_string(self):
        """Tests when the dict is none"""
        dic4 = None
        stri = Base.to_json_string([dic4])
        self.assertTrue(type(stri) == str)
        self.assertTrue(stri, [])

    def test_save_to_file(self):
        """Tests writing json string rep to file"""
        r1 = Rectangle(10, 7, 2, 8, 9)
        r2 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_empty_save_to_file(self):
        """Tests when the list is empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_none_save_to_file(self):
        """Tests when list is none"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_from_json_string(self):
        """Tests list of json string representation"""
        list1 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        jsonlist1 = Base.from_json_string(list1)
        self.assertTrue(type(list1) == str)
        self.assertTrue(type(jsonlist1) == list)
        self.assertTrue(type(jsonlist1[0]) == dict)
        self.assertTrue(jsonlist1,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(jsonlist1[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_empty_from_json_string(self):
        """Tests when list is empty"""
        list2 = ""
        jsonlist2 = Base.from_json_string(list2)
        self.assertTrue(type(jsonlist2) == list)
        self.assertTrue(jsonlist2 == [])

    def test_none_from_json_string(self):
        """Tests when the list is none"""
        list3 = None
        jsonlist3 = Base.from_json_string(list3)
        self.assertTrue(type(jsonlist3) == list)
        self.assertTrue(jsonlist3 == [])

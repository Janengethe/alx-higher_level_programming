#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
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

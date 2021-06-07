#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_default_attr(self):
        """Tests the attributes by default"""
        rec =  Rectangle(5, 6)
        self.assertTrue(rec.width == 5)
        self.assertTrue(rec.height == 6)
        
    def test_args(self):
        """Tests the args given to rep"""
        rec = Rectangle(2, 3, 4, 5, 6)
        self.assertTrue(rec.width == 2)
        self.assertTrue(rec.height == 3)
        self.assertTrue(rec.x == 4)
        self.assertTrue(rec.y == 5)
        self.assertTrue(rec.id == 6)

    def test_more_args(self):
        """Tests if more arguments passed"""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 6, 7, 8)

    def test_less_args(self):
        """Tests few arguments passed"""
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_no_args(self):
        """Tests when no args passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_private_att_access(self):
        """Tests access of private attributes"""
        with self.assertRaises(AttributeError):
            Rectangle.__width
            Rectangle.__height
            Rectangle.__x
            Rectangle.__y
            
    def test_class(self):
        """Tests class is indeed Rectangle"""
        self.assertTrue(Rectangle(5, 6), self.__class__ == Rectangle)

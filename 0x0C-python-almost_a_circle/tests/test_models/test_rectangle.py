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
        self.assertTrue(rec.x == 0)
        self.assertTrue(rec.y == 0)
        self.assertTrue(rec.id is not None)
        
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

    def test_att_values(self):
        """Tests the values given for the
        attributes and error raised where necessary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 3, 4, 5, 6)
            Rectangle([2, 3], 4, 5, 6, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (3, 5), 4, 5, 7)
            Rectangle(2, {6: 7}, 5, 6, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 3, 4)
            Rectangle(1, 2, (ten), 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "one", 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 3, 4, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4, 5, 6, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -2, 4, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(20, 30, 25, -45, 60)

    def test_rec_area(self):
        """Tests the area of the rectangle"""
        self.assertEqual(Rectangle(4, 5).area(), 20)
        self.assertEqual(Rectangle(2, 3, 0, 0, 7).area(), 6)
        self.assertEqual(Rectangle(8, 20, 3, 4, 76).area(), 160)
        self.assertEqual(Rectangle(4, 7, 2, 1).area(), 28)

    def test_str(self):
        """Tests how it prints out the rectangle"""
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rec), '[Rectangle] (5) 3/4 - 1/2')

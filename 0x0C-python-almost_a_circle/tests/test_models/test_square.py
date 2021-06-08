#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_default_attr(self):
        """Tests the attributes by default"""
        sq =  Square(62)
        self.assertTrue(sq.width == 62)
        self.assertTrue(sq.height == 62)
        self.assertTrue(sq.x == 0)
        self.assertTrue(sq.y == 0)
        self.assertTrue(sq.id is not None)
        
    def test_args(self):
        """Tests the args given to rep"""
        sq = Square(2, 4, 5, 6)
        self.assertTrue(sq.width == 2)
        self.assertTrue(sq.height == 2)
        self.assertTrue(sq.x == 4)
        self.assertTrue(sq.y == 5)
        self.assertTrue(sq.id == 6)

    def test_more_args(self):
        """Tests if more arguments passed"""
        with self.assertRaises(TypeError):
            Square(2, 3, 4, 5, 6, 7, 8)

    def test_no_args(self):
        """Tests when no args passed"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_class(self):
        """Tests class is indeed Square"""
        self.assertTrue(Square(6), self.__class__ == Square)

    def test_att_values(self):
        """Tests the values given for the
        attributes and error raised where necessary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", 3, 4, 5)
            Square([2, 3], 4, 5, 6)
            Square({2, })
            Square({"sq": 2})
            Square(None)
            Square((3, 2), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
            Square(-1)
            Square(0, 2, 3, 4)
            Square(-3, 4, 5, 7)

    def test_square_area(self):
        """Tests the area of the Square"""
        self.assertEqual(Square(4).area(), 16)
        self.assertEqual(Square(2, 0, 0, 7).area(), 4)
        self.assertEqual(Square(8, 3, 4, 76).area(), 64)
        self.assertEqual(Square(4, 2, 1).area(), 16)

    def test_str(self):
        """Tests how it prints out the Square"""
        sq = Square(1, 2, 3, 44)
        sq.size = 50
        self.assertEqual(str(sq), '[Square] (44) 2/3 - 50')

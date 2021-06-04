#!/usr/bin/python3
"""
Module Square
Inherits from class Rectangle,
That inherits from class Base
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from class Rectangle
    Methods:
        def __init__(self,size,x,y,id)
        def __str__(self)
    Getter:
       def size(self)
    Setter:
        def size(self, value)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization
        calls the supper class rectangle
        and assigns width and height to size
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides to return
        "[Square] (<id>) <x>/<y> - <size>"
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

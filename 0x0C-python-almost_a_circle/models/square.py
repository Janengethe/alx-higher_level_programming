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
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization
        calls the supper class rectangle
        and assigns width and height to size
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Overrides to return
        "[Square] (<id>) <x>/<y> - <size>"
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

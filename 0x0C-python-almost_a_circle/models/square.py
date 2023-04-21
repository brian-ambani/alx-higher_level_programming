#!/usr/bin/python3
"""
A model containing a class name square
"""

from models.rectangle import Rectangle


class Square(Ractangle):
    """
        A class representing a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initializes instances
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            A string representation of class
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Gets the value of size
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Sets the value of size
        """
        if type(value) is not int:
            raise TypeError("width nust be an integer")
        if value <= 0:
            raise ValueError("Width mudt be > 0")
        self.__width = value
        self.__height = value

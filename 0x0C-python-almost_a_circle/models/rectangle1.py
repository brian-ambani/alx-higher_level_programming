#!/usr/bin/python3
"""
Module with a class Rectangle
that inherits from class Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Class representing a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A method containing attributes
        of the object
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """
            Gets the value of width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            Sets the value of width
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")

            if value <= 0:
                raise ValueError("with must be > 0")

            self.width = value

        @property
        def height(self):
            """
            gets the value of height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            sets the value of the height
            """
            if type(value) is not int:
                raise TypeError("heigth must be an integer")

            if value < 0:
                raise ValueError("height must >= 0")

        @property
        def x(self):
            """
            Gets the value of x
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            Sets the value of x
            """
            if type(value) is not int:
                raise TypeError("x must be an integer")

            if value < 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """
            Gets the value of y
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            Sets the value of y
            """
            if type(value) is not int:
                raise TypeError("y must be an integer")

            if value < 0:
                raise ValueError("y must be > 0")
            self.__y = value

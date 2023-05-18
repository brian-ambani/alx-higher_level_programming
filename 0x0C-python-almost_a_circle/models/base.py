#!/usr/bin/python3
"""
This module contains the base class
for other classes
"""


class Base:
    """
    Represents the base class for
    the other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method that initializes instances
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

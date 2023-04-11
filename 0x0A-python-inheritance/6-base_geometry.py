#!/usr/bin/python3
"""
Module containing a class BaseGeometry
"""


class BaseGeometry:
    """
    A class containing one method area
    """
    def area(self):
        """
        Method that raises an exception the
        area is not implemented
        """

        raise Exception("area() is not implemnted")

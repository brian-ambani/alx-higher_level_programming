#!/usr/bin/python3
"""
A module with a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns true/false,
    if the obj is an instanceof, or if the
    object is an instance of a class
    inherited from, the specified class.

    Args:
        obj: an object
        a_class: a class

    Return:
        True if the obj is an instance of a_class
        Else return false
    """

    return isinstance(obj, a_class)

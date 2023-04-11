#!/usr/bin/python3
"""
A module with a function is_same_class

"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is
    exactly an instance of the specified class,
    otherwise it returns false

    Args:
        obj:
            An objected passed
        a_class:
            A passed class
    Return:
        True if typeofobject is a_class
        False,otherwise

    """
    return type(obj) is a_class

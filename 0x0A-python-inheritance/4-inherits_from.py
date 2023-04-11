#!/usr/bin/python3
"""
A module contain a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    A function returns true/false if object is an
    instance of a class that inherited

    Args:
        obj: an object
        a_class: a class

    Returns:
        True if object is an instance of a class
        inherited otherwise false

    """

    if type(obj) is a_class:
        return False
    return isiinstance(obj, a_class)

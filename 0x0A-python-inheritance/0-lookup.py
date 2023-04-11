#!/usr/bin/python3

def lookup(obj):
    """
    Function that returns a list of available
    attributes and methods of an object

    Args:
        obj:
            instance of the class

    Return:
        list object
    """

    return dir(obj)

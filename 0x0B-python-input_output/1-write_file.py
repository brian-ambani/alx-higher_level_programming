#!/usr/bin/python3
"""
Module containing a function write_file
"""


def write_file(filename="", text=""):
    """
    A function that writes a string a
    string to a text file and returns the
    no. of characters.

    Args:
        filename: the name of the file
        text: text file

    Returns: the no of charcters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

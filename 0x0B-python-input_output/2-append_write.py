#!/usr/bin/python3
""" Module that contains a function that reads n lines of a text file
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end
    of a text file
    Args:
        filename: name of the file
        text: text in the text file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

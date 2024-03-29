#!/usr/bin/python3
"""
A module with a function that prints a square
"""


def print_square(size):
    """ Function that prints a square with the character #
    Args:
        size: size of the square printed
    Returns:
        No return
    Raises:
        TypeError: If size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print("#" * size)

#!/usr/bin/python3
""" A module that defines a square
"""


class square:
    """ A class that defines a square by its size
    """

    def __init__(self, size=0):
        """ A method to initialize the square
        Args:
            size(int): this is the size of the square

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

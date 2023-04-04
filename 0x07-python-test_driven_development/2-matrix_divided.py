#!/usr/bin/python3
"""
Module with a function that divides the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides integer or float numbers in a matrix

    Args:
        matrix: contains elements of a list
        div: number that divides the matrix

    Return:
        results of the division

    Raises:
        TyeError:
            When elements in matrix are not lists
            If elements in the lists are not integers
            If div is not an integer or float
            When the lists in the matrix are not of the same size

        ZeroDivisionError: If div is zero

    """
    error_txt1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_txt2 = "Each row of the matrix must have the same size"
    size = 0

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_txt1)

    for items in matrix:
        if not items or not isinstance(items, list):
            raise TypeError(error_txt1)

        if size != 0 and len(items) != size:
            raise TypeError(error_txt2)

        for item in items:
            if not type(item) in (int, float):
                raise TypeError(error_txt1)

        size = len(items)

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mt = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return (mt)

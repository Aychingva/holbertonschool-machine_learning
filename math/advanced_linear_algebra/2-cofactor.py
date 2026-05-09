#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix"""

minor = __import__("1-minor").minor


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix

    Args:
        matrix (list of lists): matrix whose cofactor matrix
            should be calculated

    Returns:
        list of lists: the cofactor matrix of matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square or is empty
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]] or len(matrix[0]) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    minor_matrix = minor(matrix)

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * minor_matrix[i][j])
        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix

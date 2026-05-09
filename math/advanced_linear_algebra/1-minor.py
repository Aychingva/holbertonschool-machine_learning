#!/usr/bin/env python3
"""Module for calculating the minor matrix of a matrix"""

determinant = __import__("0-determinant").determinant


def minor(matrix):
    """Calculates the minor matrix of a matrix

    Args:
        matrix (list of lists): matrix whose minor matrix should be calculated

    Returns:
        list of lists: the minor matrix of matrix

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

    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            submatrix = [
                [matrix[row][col] for col in range(n) if col != j]
                for row in range(n) if row != i
            ]
            minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix

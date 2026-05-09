#!/usr/bin/env python3
"""Module for calculating the definiteness of a matrix"""

import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix

    Args:
        matrix (numpy.ndarray): matrix of shape (n, n)

    Returns:
        str: the definiteness of the matrix or None

    Raises:
        TypeError: if matrix is not a numpy.ndarray
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.size == 0 or len(matrix.shape) != 2:
        return None

    if matrix.shape[0] != matrix.shape[1]:
        return None

    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    if np.all(eigenvalues < 0):
        return "Negative definite"
    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"

    return "Indefinite"

#!/usr/bin/env python3
"""Function that calculates the mean and covariance of a data set"""

import numpy as np


def mean_cov(X):
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.sum(X, axis=0, keepdims=True) / n

    X_centered = X - mean
    cov = (X_centered.T @ X_centered) / (n - 1)

    return mean, cov 

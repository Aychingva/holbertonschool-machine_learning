#!/usr/bin/env python3
"""Class that represents a Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Constructor"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.sum(data, axis=1, keepdims=True) / n
        X_centered = data - self.mean
        self.cov = (X_centered @ X_centered.T) / (n - 1)
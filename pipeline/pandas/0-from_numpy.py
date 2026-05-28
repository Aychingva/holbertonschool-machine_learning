#!/usr/bin/env python3
"""Module for creating a pandas DataFrame from a numpy ndarray."""
import pandas as pd


def from_numpy(array):
    """Create a pd.DataFrame from a np.ndarray.

    Args:
        array: the np.ndarray to convert

    Returns:
        the newly created pd.DataFrame
    """
    cols = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)

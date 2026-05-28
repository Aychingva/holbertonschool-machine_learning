#!/usr/bin/env python3
"""Module for converting last 10 rows of High and Close to numpy array."""
import pandas as pd


def array(df):
    """Select last 10 rows of High and Close columns as numpy.ndarray.

    Args:
        df: the pd.DataFrame to convert

    Returns:
        the numpy.ndarray
    """
    return df[['High', 'Close']].tail(10).to_numpy()

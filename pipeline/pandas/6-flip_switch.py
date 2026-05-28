#!/usr/bin/env python3
"""Module for sorting and transposing a pd.DataFrame."""


def flip_switch(df):
    """Sort data in reverse chronological order and transpose.

    Args:
        df: the pd.DataFrame to transform

    Returns:
        the transformed pd.DataFrame
    """
    return df.sort_index(ascending=False).transpose()

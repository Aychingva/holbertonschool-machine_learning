#!/usr/bin/env python3
"""Module for removing NaN values from Close column in a pd.DataFrame."""


def prune(df):
    """Remove entries where Close has NaN values.

    Args:
        df: the pd.DataFrame to modify

    Returns:
        the modified pd.DataFrame
    """
    return df.dropna(subset=['Close'])

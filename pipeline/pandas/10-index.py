#!/usr/bin/env python3
"""Module for setting Timestamp as index in a pd.DataFrame."""


def index(df):
    """Set the Timestamp column as the index of the dataframe.

    Args:
        df: the pd.DataFrame to modify

    Returns:
        the modified pd.DataFrame
    """
    return df.set_index('Timestamp')

#!/usr/bin/env python3
"""Module for sorting a pd.DataFrame by High price."""


def high(df):
    """Sort the pd.DataFrame by High price in descending order.

    Args:
        df: the pd.DataFrame to sort

    Returns:
        the sorted pd.DataFrame
    """
    return df.sort_values(by='High', ascending=False)

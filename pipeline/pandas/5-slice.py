#!/usr/bin/env python3
"""Module for slicing a pd.DataFrame."""


def slice(df):
    """Extract High, Low, Close, Volume_(BTC) columns every 60th row.

    Args:
        df: the pd.DataFrame to slice

    Returns:
        the sliced pd.DataFrame
    """
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]

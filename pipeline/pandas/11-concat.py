#!/usr/bin/env python3
"""Module for concatenating two pd.DataFrames."""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Concatenate bitstamp and coinbase dataframes.

    Args:
        df1: the coinbase pd.DataFrame
        df2: the bitstamp pd.DataFrame

    Returns:
        the concatenated pd.DataFrame
    """
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[df2.index <= 1417411920]
    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

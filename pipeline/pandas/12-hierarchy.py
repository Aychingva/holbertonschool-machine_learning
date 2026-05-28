#!/usr/bin/env python3
"""Module for creating a hierarchical pd.DataFrame."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate bitstamp and coinbase with Timestamp as first index level.

    Args:
        df1: the coinbase pd.DataFrame
        df2: the bitstamp pd.DataFrame

    Returns:
        the concatenated pd.DataFrame
    """
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1.loc[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2 = df2.loc[(df2.index >= 1417411980) & (df2.index <= 1417417980)]
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    df = df.swaplevel(0, 1).sort_index()
    return df

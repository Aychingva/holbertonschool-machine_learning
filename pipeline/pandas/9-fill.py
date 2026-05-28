#!/usr/bin/env python3
"""Module for filling missing values in a pd.DataFrame."""


def fill(df):
    """Remove Weighted_Price and fill missing values.

    Args:
        df: the pd.DataFrame to modify

    Returns:
        the modified pd.DataFrame
    """
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
    return df

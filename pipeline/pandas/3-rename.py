#!/usr/bin/env python3
"""Module for renaming and converting Timestamp column in a pd.DataFrame."""
import pandas as pd


def rename(df):
    """Rename Timestamp column to Datetime and convert to datetime values.

    Args:
        df: the pd.DataFrame to modify

    Returns:
        the modified pd.DataFrame
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]

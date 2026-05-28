#!/usr/bin/env python3
"""Module for computing descriptive statistics of a pd.DataFrame."""


def analyze(df):
    """Compute descriptive statistics for all columns except Timestamp.

    Args:
        df: the pd.DataFrame to analyze

    Returns:
        a new pd.DataFrame containing the descriptive statistics
    """
    return df.drop(columns=['Timestamp']).describe()

#!/usr/bin/env python3
"""Sum of squares"""


def summation_i_squared(n):
    """Calculate sum of squares from 1 to n"""
    if not isinstance(n, (int, float)) or isinstance(n, bool):
        return None
    if n < 1:
        return None
    return int(n * (n + 1) * (2 * n + 1) / 6)

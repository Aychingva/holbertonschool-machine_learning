#!/usr/bin/env python3
"""Polynomial derivative"""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    derivative = [i * poly[i] for i in range(1, len(poly))]
    if all(c == 0 for c in derivative):
        return [0]
    return derivative

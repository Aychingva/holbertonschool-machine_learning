#!/usr/bin/env python3
"""Module for plotting y as a solid red line."""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot y = x^3 as a solid red line with x range 0 to 10."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(range(11), y, 'r-')
    plt.xlim(0, 10)
    plt.show()

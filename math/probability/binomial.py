#!/usr/bin/env python3
"""Module for Binomial distribution"""


class Binomial:
    """Represents a Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculates the PMF value for a given k"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        n_fact = 1
        for i in range(1, self.n + 1):
            n_fact *= i
        k_fact = 1
        for i in range(1, k + 1):
            k_fact *= i
        nk_fact = 1
        for i in range(1, self.n - k + 1):
            nk_fact *= i
        combination = n_fact / (k_fact * nk_fact)
        return combination * self.p ** k * (1 - self.p) ** (self.n - k)

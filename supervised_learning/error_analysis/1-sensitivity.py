#!/usr/bin/env python3
"""Calculates the sensitivity for each class in a confusion matrix"""

import numpy as np


def sensitivity(confusion):
    """
    Calculates the sensitivity for each class in a confusion matrix

    parameters:
        confusion [numpy.ndarray of shape (classes, classes)]:
            row indices represent the correct labels
            column indices represent the predicted labels
            classes: number of classes

    returns:
        [numpy.ndarray of shape (classes,)]:
            contains the sensitivity of each class
    """
    true_positives = np.diagonal(confusion)
    actual_positives = np.sum(confusion, axis=1)

    return true_positives / actual_positives
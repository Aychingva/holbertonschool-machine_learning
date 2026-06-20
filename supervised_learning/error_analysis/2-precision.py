#!/usr/bin/env python3
"""Calculates the precision for each class in a confusion matrix"""

import numpy as np


def precision(confusion):
    """
    Calculates the precision for each class in a confusion matrix

    parameters:
        confusion [numpy.ndarray of shape (classes, classes)]:
            row indices represent the correct labels
            column indices represent the predicted labels
            classes: number of classes

    returns:
        [numpy.ndarray of shape (classes,)]:
            contains the precision of each class
    """
    true_positives = np.diagonal(confusion)
    predicted_positives = np.sum(confusion, axis=0)

    return true_positives / predicted_positives

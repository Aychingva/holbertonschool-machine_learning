#!/usr/bin/env python3
"""Calculates the F1 score for each class in a confusion matrix"""

import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    Calculates the F1 score for each class in a confusion matrix

    parameters:
        confusion [numpy.ndarray of shape (classes, classes)]:
            row indices represent the correct labels
            column indices represent the predicted labels
            classes: number of classes

    returns:
        [numpy.ndarray of shape (classes,)]:
            contains the F1 score of each class
    """
    sens = sensitivity(confusion)
    prec = precision(confusion)

    return 2 * (prec * sens) / (prec + sens)

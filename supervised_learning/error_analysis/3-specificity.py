#!/usr/bin/env python3
"""Calculates the specificity for each class in a confusion matrix"""

import numpy as np


def specificity(confusion):
    """
    Calculates the specificity for each class in a confusion matrix

    parameters:
        confusion [numpy.ndarray of shape (classes, classes)]:
            row indices represent the correct labels
            column indices represent the predicted labels
            classes: number of classes

    returns:
        [numpy.ndarray of shape (classes,)]:
            contains the specificity of each class
    """
    total = np.sum(confusion)
    true_positives = np.diagonal(confusion)
    actual_positives = np.sum(confusion, axis=1)
    predicted_positives = np.sum(confusion, axis=0)

    false_positives = predicted_positives - true_positives
    false_negatives = actual_positives - true_positives
    true_negatives = total - (true_positives + false_positives + false_negatives)

    return true_negatives / (true_negatives + false_positives)

#!/usr/bin/env python3
"""Creates a confusion matrix"""

import numpy as np


def create_confusion_matrix(labels, logits):
    """
    Creates a confusion matrix

    parameters:
        labels [numpy.ndarray of shape (m, classes)]:
            contains the correct labels for each data point, one-hot
            m: number of data points
            classes: number of classes
        logits [numpy.ndarray of shape (m, classes)]:
            contains the predicted labels, one-hot

    returns:
        confusion [numpy.ndarray of shape (classes, classes)]:
            row indices represent the correct labels
            column indices represent the predicted labels
    """
    return np.matmul(labels.T, logits)

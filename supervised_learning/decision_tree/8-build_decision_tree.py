#!/usr/bin/env python3
"""Defines Node, Leaf, and Decision_Tree classes for a decision tree"""

import numpy as np


class Node:
    """Represents an internal node of a decision tree"""

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """
        Initializes a Node

        parameters:
            feature: the feature used for splitting
            threshold: the threshold value used for splitting
            left_child [Node]: the left child of this node
            right_child [Node]: the right child of this node
            is_root [bool]: whether this node is the root of the tree
            depth [int]: the depth of this node in the tree
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        Calculates the maximum depth of the tree below this node

        returns:
            [int]: the maximum depth among the nodes below this one
        """
        left_depth = self.left_child.max_depth_below()
        right_depth = self.right_child.max_depth_below()

        return max(left_depth, right_depth)

    def count_nodes_below(self, only_leaves=False):
        """
        Counts the number of nodes below this node

        parameters:
            only_leaves [bool]: if True, only count leaf nodes

        returns:
            [int]: the number of nodes below this node
        """
        left_count = self.left_child.count_nodes_below(
            only_leaves=only_leaves)
        right_count = self.right_child.count_nodes_below(
            only_leaves=only_leaves)

        if only_leaves:
            return left_count + right_count

        return 1 + left_count + right_count

    def left_child_add_prefix(self, text):
        """
        Adds a prefix to the text representation of the left child

        parameters:
            text [str]: the text to prefix

        returns:
            [str]: the prefixed text
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            if x == "":
                continue
            new_text += ("    |  " + x) + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        """
        Adds a prefix to the text representation of the right child

        parameters:
            text [str]: the text to prefix

        returns:
            [str]: the prefixed text
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            if x == "":
                continue
            new_text += ("       " + x) + "\n"
        return new_text

    def __str__(self):
        """
        Returns a string representation of this node and its children

        returns:
            [str]: the string representation of the node
        """
        if self.is_root:
            node_text = f"root [feature={self.feature}, " \
                        f"threshold={self.threshold}]\n"
        else:
            node_text = f"-> node [feature={self.feature}, " \
                        f"threshold={self.threshold}]\n"

        left_str = self.left_child_add_prefix(str(self.left_child))
        right_str = self.right_child_add_prefix(str(self.right_child))

        return node_text + left_str + right_str

    def get_leaves_below(self):
        """
        Returns the list of all leaves below this node

        returns:
            [list]: the list of Leaf objects below this node
        """
        return self.left_child.get_leaves_below() + \
            self.right_child.get_leaves_below()

    def update_bounds_below(self):
        """
        Recursively computes the lower and upper bound dictionaries
        for this node and all nodes below it
        """
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -1 * np.inf}

        for child in [self.left_child, self.right_child]:
            child.lower = self.lower.copy()
            child.upper = self.upper.copy()

            if child == self.left_child:
                child.lower[self.feature] = self.threshold
            else:
                child.upper[self.feature] = self.threshold

        for child in [self.left_child, self.right_child]:
            child.update_bounds_below()

    def update_indicator(self):
        """
        Computes the indicator function for this node based on its
        lower and upper bound dictionaries, and stores it in the
        indicator attribute
        """
        def is_large_enough(x):
            """
            Checks whether each individual's features are all
            strictly greater than the node's lower bounds

            parameters:
                x [numpy.ndarray]: shape (n_individuals, n_features)

            returns:
                [numpy.ndarray]: 1D boolean array of size n_individuals
            """
            checks = [np.greater(x[:, key], self.lower[key])
                      for key in list(self.lower.keys())]
            return np.all(np.array(checks), axis=0)

        def is_small_enough(x):
            """
            Checks whether each individual's features are all
            less than or equal to the node's upper bounds

            parameters:
                x [numpy.ndarray]: shape (n_individuals, n_features)

            returns:
                [numpy.ndarray]: 1D boolean array of size n_individuals
            """
            checks = [np.less_equal(x[:, key], self.upper[key])
                      for key in list(self.upper.keys())]
            return np.all(np.array(checks), axis=0)

        self.indicator = lambda x: np.all(
            np.array([is_large_enough(x), is_small_enough(x)]), axis=0)

    def pred(self, x):
        """
        Predicts the value for a single individual by traversing
        the tree based on the feature threshold

        parameters:
            x [numpy.ndarray]: a single individual's feature values

        returns:
            the predicted value from the appropriate leaf
        """
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        else:
            return self.right_child.pred(x)


class Leaf(Node):
    """Represents a leaf node of a decision tree"""

    def __init__(self, value, depth=None):
        """
        Initializes a Leaf

        parameters:
            value: the value predicted by this leaf
            depth [int]: the depth of this leaf in the tree
        """
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
        Returns the depth of this leaf

        returns:
            [int]: the depth of this leaf
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
        Returns the count of this leaf node

        parameters:
            only_leaves [bool]: if True, only count leaf nodes

        returns:
            [int]: always 1, since a leaf counts as one node
        """
        return 1

    def __str__(self):
        """
        Returns a string representation of this leaf

        returns:
            [str]: the string representation of the leaf
        """
        return (f"-> leaf [value={self.value}]")

    def get_leaves_below(self):
        """
        Returns this leaf as a single-element list

        returns:
            [list]: a list containing only this leaf
        """
        return [self]

    def update_bounds_below(self):
        """
        Leaves have no children to propagate bounds to, so this
        method does nothing
        """
        pass

    def pred(self, x):
        """
        Returns the predicted value stored in this leaf

        parameters:
            x [numpy.ndarray]: a single individual's feature values

        returns:
            the value of this leaf
        """
        return self.value


class Decision_Tree():
    """Represents a decision tree"""

    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        """
        Initializes a Decision_Tree

        parameters:
            max_depth [int]: the maximum depth of the tree
            min_pop [int]: the minimum population required to split
            seed [int]: the seed for the random number generator
            split_criterion [str]: the criterion used for splitting
            root [Node]: the root node of the tree
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
        Calculates the maximum depth of the decision tree

        returns:
            [int]: the maximum depth of the tree
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
        Counts the number of nodes in the decision tree

        parameters:
            only_leaves [bool]: if True, only count leaf nodes

        returns:
            [int]: the number of nodes in the tree
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """
        Returns a string representation of the decision tree

        returns:
            [str]: the string representation of the tree
        """
        return self.root.__str__()

    def get_leaves(self):
        """
        Returns the list of all leaves in the decision tree

        returns:
            [list]: the list of Leaf objects in the tree
        """
        return self.root.get_leaves_below()

    def update_bounds(self):
        """
        Computes the lower and upper bound dictionaries for every
        node in the decision tree
        """
        self.root.update_bounds_below()

    def update_predict(self):
        """
        Computes the prediction function for the whole tree by
        leveraging the indicator function of every leaf, and
        stores it in the predict attribute
        """
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()

        self.predict = lambda A: np.sum(
            np.array([leaf.indicator(A) * leaf.value for leaf in leaves]),
            axis=0)

    def pred(self, x):
        """
        Predicts the value for a single individual by traversing
        the tree from the root

        parameters:
            x [numpy.ndarray]: a single individual's feature values

        returns:
            the predicted value
        """
        return self.root.pred(x)

    def fit(self, explanatory, target, verbose=0):
        """
        Trains the decision tree on the given data

        parameters:
            explanatory [numpy.ndarray of shape (m, n)]:
                the explanatory features of the training individuals
            target [numpy.ndarray of shape (m,)]:
                the target class of each training individual
            verbose [int]: if 1, prints training statistics
        """
        if self.split_criterion == "random":
            self.split_criterion = self.random_split_criterion
        else:
            self.split_criterion = self.Gini_split_criterion
        self.explanatory = explanatory
        self.target = target
        self.root.sub_population = np.ones_like(self.target, dtype='bool')

        self.fit_node(self.root)

        self.update_predict()

        if verbose == 1:
            print(f"""  Training finished.
- Depth                     : { self.depth()       }
- Number of nodes           : { self.count_nodes() }
- Number of leaves          : { self.count_nodes(only_leaves=True) }
- Accuracy on training data : { self.accuracy(self.explanatory,
                                                self.target)    }""")

    def np_extrema(self, arr):
        """
        Returns the minimum and maximum of a numpy array

        parameters:
            arr [numpy.ndarray]: the array to inspect

        returns:
            [tuple]: (min, max) of the array
        """
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        """
        Randomly selects a feature and a threshold to split a node

        parameters:
            node [Node]: the node to split

        returns:
            [tuple]: (feature, threshold)
        """
        diff = 0
        while diff == 0:
            feature = self.rng.integers(0, self.explanatory.shape[1])
            feature_min, feature_max = self.np_extrema(
                self.explanatory[:, feature][node.sub_population])
            diff = feature_max - feature_min
        x = self.rng.uniform()
        threshold = (1 - x) * feature_min + x * feature_max
        return feature, threshold

    def fit_node(self, node):
        """
        Recursively splits a node into children, either leaves or
        further nodes, based on the split criterion

        parameters:
            node [Node]: the node to split
        """
        node.feature, node.threshold = self.split_criterion(node)

        left_population = node.sub_population & \
            (self.explanatory[:, node.feature] > node.threshold)
        right_population = node.sub_population & \
            (self.explanatory[:, node.feature] <= node.threshold)

        # Is left node a leaf ?
        left_size = np.sum(left_population)
        left_classes = np.unique(self.target[left_population]).size
        is_left_leaf = left_size < self.min_pop
        is_left_leaf = is_left_leaf or node.depth + 1 == self.max_depth
        is_left_leaf = is_left_leaf or left_classes == 1

        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)

        # Is right node a leaf ?
        right_size = np.sum(right_population)
        right_classes = np.unique(self.target[right_population]).size
        is_right_leaf = right_size < self.min_pop
        is_right_leaf = is_right_leaf or node.depth + 1 == self.max_depth
        is_right_leaf = is_right_leaf or right_classes == 1

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def get_leaf_child(self, node, sub_population):
        """
        Creates a leaf child for the given node, with the value set
        to the most represented class among the sub population

        parameters:
            node [Node]: the parent node
            sub_population [numpy.ndarray]: boolean mask of
                individuals belonging to this leaf

        returns:
            [Leaf]: the newly created leaf
        """
        target_values = self.target[sub_population]
        values, counts = np.unique(target_values, return_counts=True)
        value = values[np.argmax(counts)]
        leaf_child = Leaf(value)
        leaf_child.depth = node.depth + 1
        leaf_child.subpopulation = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """
        Creates a node child for the given node

        parameters:
            node [Node]: the parent node
            sub_population [numpy.ndarray]: boolean mask of
                individuals belonging to this node

        returns:
            [Node]: the newly created node
        """
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def accuracy(self, test_explanatory, test_target):
        """
        Computes the accuracy of the tree's predictions on a test set

        parameters:
            test_explanatory [numpy.ndarray]: the explanatory
                features of the test individuals
            test_target [numpy.ndarray]: the true target classes

        returns:
            [float]: the fraction of correct predictions
        """
        predictions = self.predict(test_explanatory)
        return np.sum(np.equal(predictions, test_target)) / test_target.size

    def possible_thresholds(self, node, feature):
        """
        Computes the possible thresholds for a given feature at a
        node, as the midpoints between consecutive unique values

        parameters:
            node [Node]: the node whose sub population is considered
            feature [int]: the index of the feature

        returns:
            [numpy.ndarray]: the possible threshold values
        """
        values = np.unique(
            (self.explanatory[:, feature])[node.sub_population])
        return (values[1:] + values[:-1]) / 2

    def Gini_split_criterion_one_feature(self, node, feature):
        """
        Computes the best threshold for a given feature at a node,
        according to the average Gini impurity of the resulting
        children

        parameters:
            node [Node]: the node to split
            feature [int]: the index of the feature to consider

        returns:
            [numpy.ndarray]: a 2-element array containing the best
                threshold and its corresponding average Gini impurity
        """
        thresholds = self.possible_thresholds(node, feature)

        classes = np.unique(self.target[node.sub_population])
        target_sub = self.target[node.sub_population]
        feat_vals = self.explanatory[:, feature][node.sub_population]

        class_indicator = (target_sub[:, None] == classes[None, :])
        greater_than = feat_vals[:, None] > thresholds[None, :]

        Left_F = greater_than[:, :, None] & class_indicator[:, None, :]
        Right_F = (~greater_than)[:, :, None] & class_indicator[:, None, :]

        left_counts = np.sum(Left_F, axis=0)
        right_counts = np.sum(Right_F, axis=0)

        left_totals = np.sum(left_counts, axis=1)
        right_totals = np.sum(right_counts, axis=1)

        left_props = left_counts / left_totals[:, None]
        right_props = right_counts / right_totals[:, None]

        left_gini = 1 - np.sum(left_props ** 2, axis=1)
        right_gini = 1 - np.sum(right_props ** 2, axis=1)

        n_total = feat_vals.size
        gini_avg = (left_totals / n_total) * left_gini + \
            (right_totals / n_total) * right_gini

        best_idx = np.argmin(gini_avg)
        return np.array([thresholds[best_idx], gini_avg[best_idx]])

    def Gini_split_criterion(self, node):
        """
        Determines the best feature and threshold to split a node,
        based on the smallest average Gini impurity across all
        features

        parameters:
            node [Node]: the node to split

        returns:
            [tuple]: (feature, threshold) for the best split
        """
        X = np.array([self.Gini_split_criterion_one_feature(node, i)
                      for i in range(self.explanatory.shape[1])])
        i = np.argmin(X[:, 1])
        return i, X[i, 0]

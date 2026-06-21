def max_depth_below(self):
    """
    Calculates the maximum depth of the tree below this node

    returns:
        [int]: the maximum depth among the nodes below this one
    """
    left_depth = self.left_child.max_depth_below()
    right_depth = self.right_child.max_depth_below()

    return max(left_depth, right_depth)

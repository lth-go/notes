#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        rest = sum - root.val

        if rest == 0 and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)

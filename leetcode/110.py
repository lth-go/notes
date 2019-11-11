#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def foo(node):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return 1

            if node.left is None:
                return foo(node.right) + 1

            if node.right is None:
                return foo(node.left) + 1

            left_dep = foo(node.left)
            right_dep = foo(node.right)

            return min(left_dep, right_dep) + 1

        return foo(root)

#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []

        def foo(node):
            if node is None:
                return []
            return foo(node.left) + [node.val] + foo(node.right)

        result = foo(root)

        return len(set(result)) == len(result) and sorted(result) == result

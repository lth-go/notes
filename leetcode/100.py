#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def foo(node):
            if node is None:
                return [None]

            if node.left is None and node.right is None:
                return [node.val]

            return foo(node.left) + [node.val] + foo(node.right)

        return foo(p) == foo(q)

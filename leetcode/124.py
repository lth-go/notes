#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = - 2 << 64

        def foo(root):
            if not root:
                return 0

            left = foo(root.left)
            right = foo(root.right)

            self.result = max(left + right + root.val, self.result)
            return max(0, max(left, right) + root.val)

        foo(root)

        return self.result

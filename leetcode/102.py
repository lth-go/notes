#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = {}

        def foo(node, level):
            if not node:
                return
            result.setdefault(level, [])
            result[level].append(node.val)

            foo(node.left, level + 1)
            foo(node.right, level + 1)

        foo(root, 1)

        bar = []
        for key in sorted(result.keys()):
            bar.append(result[key])

        return bar

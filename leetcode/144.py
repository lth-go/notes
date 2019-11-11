#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = [root]
        result = []

        while True:
            if not stack:
                break

            node = stack.pop()
            if not node:
                continue

            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return result

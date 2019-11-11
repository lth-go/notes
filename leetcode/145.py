#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
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

            result.insert(0, node.val)

            stack.append(node.left)
            stack.append(node.right)

        return result

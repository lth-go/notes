#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        result = []

        def foo(node):
            if node is None:
                return []
            return foo(node.left) + [node.val] + foo(node.right)

        result = foo(root)
        sort = sorted(result)

        for index in range(len(result)):
            if result[index] != sort[index]:
                a = result[index]
                b = sort[index]
                break

        def foo(node):
            if not node:
                return

            if node.val == a:
                node.val = b
            elif node.val == b:
                node.val = a

            foo(node.left)
            foo(node.right)

        foo(root)
        return

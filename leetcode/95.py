#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def foo(num_list):
            if len(num_list) == 0:
                return [None]

            elif len(num_list) == 1:
                return [TreeNode(num_list[0])]

            result = []
            for index, num in enumerate(num_list):

                left_node_list = foo(num_list[:index])
                right_node_list = foo(num_list[index + 1:])

                for left in left_node_list:
                    for right in right_node_list:
                        root = TreeNode(num)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        return foo(range(1, n + 1))

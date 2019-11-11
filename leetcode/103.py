#!/usr/bin/env python
# encoding: utf-8

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
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

        left = True
        for key in sorted(result.keys()):
            if left:
                bar.append(result[key])
                left = False

            else:
                bar.append(result[key][::-1])
                left = True

        return bar

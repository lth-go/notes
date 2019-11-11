#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = set()

        def foo(node, level):
            if not node:
                return
            result.add(level)

            foo(node.left, level + 1)
            foo(node.right, level + 1)

        foo(root, 1)

        return len(result)

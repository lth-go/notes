#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []

        def foo(root, sum, num_list):
            if not root:
                return False

            rest = sum - root.val

            if rest == 0 and root.left is None and root.right is None:
                num_copy_list = num_list[:] + [root.val]
                result.append(num_copy_list)
                return True

            foo(root.left, rest, num_list[:] + [root.val])
            foo(root.right, rest, num_list[:] + [root.val])

        foo(root, sum, [])

        return result

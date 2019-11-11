#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        index = len(nums) / 2

        node = TreeNode(nums[index])
        node.left = self.sortedArrayToBST(nums[:index])
        node.right = self.sortedArrayToBST(nums[index + 1:])

        return node

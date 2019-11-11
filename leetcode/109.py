#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def foo(nums):
            if not nums:
                return None

            index = len(nums) / 2

            node = TreeNode(nums[index])
            node.left = foo(nums[:index])
            node.right = foo(nums[index + 1:])

            return node

        def node_to_list(head):
            num_list = []

            node = head
            while node:
                num_list.append(node.val)
                node = node.next

            return num_list

        return foo(node_to_list(head))

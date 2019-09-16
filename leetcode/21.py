#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        l1_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        l2_list = []
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        merge_list = sorted(l1_list + l2_list)

        first_node = ListNode(0)

        pre_node = first_node

        for v in merge_list:

            node = ListNode(v)

            pre_node.next = node
            pre_node = node

        return first_node.next

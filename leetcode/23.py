#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merge_list = []
        for node in lists:
            while node:
                merge_list.append(node.val)
                node = node.next

        merge_list = sorted(merge_list)

        first_node = ListNode(0)

        pre_node = first_node

        for v in merge_list:
            node = ListNode(v)

            pre_node.next = node
            pre_node = node

        return first_node.next

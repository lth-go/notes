#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return head

        node = head

        node_list = []
        less_list = []
        while node:
            if node.val < x:
                less_list.append(node.val)
            else:
                node_list.append(node.val)

            node = node.next

        first = ListNode(0)
        node = first

        for val in less_list + node_list:
            node.next = ListNode(val)
            node = node.next

        return first.next

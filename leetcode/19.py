#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        first = head

        two_node = head

        for _ in range(n):
            head = head.next

        if head is None:
            return first.next

        while head.next:
            head = head.next
            two_node = two_node.next

        two_node.next = two_node.next.next

        return first

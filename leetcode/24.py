#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        l = []

        node = head
        while node:
            l.append(node.val)
            node = node.next

        length = len(l)

        for i in range(length / 2):
            i = i * 2
            l[i], l[i + 1] = l[i + 1], l[i]

        first_node = ListNode(0)

        pre_node = first_node

        for v in l:
            node = ListNode(v)

            pre_node.next = node

            pre_node = node

        return first_node.next

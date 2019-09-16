#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return None

        l = []

        node = head
        while node:
            l.append(node.val)
            node = node.next

        for i in range(len(l) / k):
            index = i * k
            l[index: index + k] = reversed(l[index: index + k])

        first_node = ListNode(0)

        pre_node = first_node

        for v in l:
            node = ListNode(v)

            pre_node.next = node

            pre_node = node

        return first_node.next

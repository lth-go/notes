#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        def get_len(head):
            node = head

            length = 0
            while node:
                node = node.next
                length += 1

            return length

        a_len = get_len(headA)
        b_len = get_len(headB)

        nodeA = headA
        nodeB = headB

        if a_len < b_len:
            nodeA, nodeB = nodeB, nodeA

        minus = abs(a_len - b_len)

        while minus > 0:
            nodeA = nodeA.next
            minus -= 1

        while nodeA:
            if nodeA == nodeB:
                return nodeA

            nodeA = nodeA.next
            nodeB = nodeB.next

        return None

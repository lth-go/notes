#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        one = head
        two = head

        while True:
            one = one.next
            two = two.next

            if two is None:
                return None

            two = two.next
            if two is None:
                return None

            if one == two:
                break

        one = head

        while one != two:
            one = one.next
            two = two.next

        return two

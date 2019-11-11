#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        one = head
        two = head.next

        if two is None:
            return False

        while True:
            one = one.next
            two = two.next

            if two is None:
                return False

            if one == two:
                return True

            two = two.next
            if two is None:
                return False

            if one == two:
                return True

#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def foo(head):
            if not head:
                return None, None

            if not head.next:
                return head, head

            node, end = foo(head.next)
            end.next = head

            head.next = None

            return node, head

        return foo(head)[0]

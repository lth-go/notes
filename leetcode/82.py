#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        first = ListNode(0)
        first.next = head

        node = first

        delete = False

        while node.next:
            if delete:
                if node.next.next:
                    if node.next.val == node.next.next.val:
                        node.next.next = node.next.next.next
                        continue

                node.next = node.next.next
                delete = False
                continue

            if node.next.next:
                if node.next.val == node.next.next.val:
                    delete = True
                    node.next.next = node.next.next.next
                    continue

            node = node.next

        return first.next

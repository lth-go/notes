#!/usr/bin/env python
# encoding: utf-8


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        cache = {}

        def foo(head):
            if head is None:
                return None

            head_id = id(head)
            if head_id in cache:
                return cache[head_id]

            new_head = Node(head.val, None, None)

            cache[head_id] = new_head

            new_head.next = foo(head.next)
            new_head.random = foo(head.random)

            return new_head

        return foo(head)

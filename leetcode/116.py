#!/usr/bin/env python
# encoding: utf-8


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        if root.left:
            root.left.next = root.right

        if root.next and root.next.left:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

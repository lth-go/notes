#!/usr/bin/env python
# encoding: utf-8


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return '(%s, %s, %s)' % (self.val, self.left, self.right)


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        if root.left is None and root.right is None:
            return root

        if root.left and root.right:
            root.left.next = root.right

        foo_node = root.right or root.left

        node = root.next

        next_node = None
        while node:
            next_node = node.left or node.right
            if next_node:
                break

            node = node.next

        foo_node.next = next_node

        self.connect(root.right)
        self.connect(root.left)

        return root


if __name__ == '__main__':
    s = Solution()

    def foo(bar):
        if bar is None:
            return None

        left = foo(bar['left'])
        right = foo(bar['right'])
        val = bar['val']

        return Node(val, left, right, None)

    input_dict = {
        "$id": "1",
        "left": {
            "$id": "2",
            "left": {
                "$id": "3",
                "left": {
                    "$id": "4",
                    "left": None,
                    "next": None,
                    "right": None,
                    "val": 2
                },
                "next": None,
                "right": None,
                "val": 0
            },
            "next": None,
            "right": {
                "$id": "5",
                "left": {
                    "$id": "6",
                    "left": None,
                    "next": None,
                    "right": None,
                    "val": 1
                },
                "next": None,
                "right": {
                    "$id": "7",
                    "left": {
                        "$id": "8",
                        "left": None,
                        "next": None,
                        "right": None,
                        "val": 7
                    },
                    "next": None,
                    "right": None,
                    "val": 0
                },
                "val": 7
            },
            "val": 1
        },
        "next": None,
        "right": {
            "$id": "9",
            "left": {
                "$id": "10",
                "left": None,
                "next": None,
                "right": None,
                "val": 9
            },
            "next": None,
            "right": {
                "$id": "11",
                "left": {
                    "$id": "12",
                    "left": None,
                    "next": None,
                    "right": None,
                    "val": 8
                },
                "next": None,
                "right": {
                    "$id": "13",
                    "left": None,
                    "next": None,
                    "right": None,
                    "val": 8
                },
                "val": 1
            },
            "val": 3
        },
        "val": 2
    }

    node = foo(input_dict)

    result = s.connect(node)

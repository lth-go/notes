#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        node_list = []

        node = head
        while node:
            node_list.append(node)
            node = node.next

        length = len(node_list)

        node_list = node_list[-(length / 2):][::-1]

        node = head

        while node and node_list:
            tmp = node.next

            node.next = node_list.pop(0)

            node.next.next = tmp

            node = tmp

        if node:
            node.next = None

        return


if __name__ == '__main__':
    from utils import list_to_node

    solution = Solution()

    head = list_to_node([1, 2, 3, 4, 5])

    solution.reorderList(head)
    print(head)

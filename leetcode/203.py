#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node_list = []

        node = head
        while node:
            if node.val != val:
                node_list.append(node)

            node = node.next

        if not node_list:
            return None

        head = ListNode(0)
        tmp_node = head

        for node in node_list:
            tmp_node.next = node
            tmp_node = node

        tmp_node.next = None

        return head.next


if __name__ == '__main__':
    from utils import list_to_node

    s = Solution()

    head = list_to_node([1, 2, 6, 3, 4, 5, 6])
    val = 6
    result = s.removeElements(head, val)
    print result

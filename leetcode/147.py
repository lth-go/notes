#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        one = ListNode(float('-inf'))
        two = head

        while two:

            insert = two
            two = two.next

            parent = one
            node = parent.next

            while True:
                if node is None:
                    parent.next = insert
                    insert.next = None
                    break

                if parent.val <= insert.val <= node.val:
                    parent.next = insert
                    insert.next = node
                    break

                parent = node
                node = parent.next

                if node is None:
                    parent.next = insert
                    insert.next = None
                    break

        return one.next


if __name__ == '__main__':
    from utils import list_to_node

    s = Solution()

    head = list_to_node([-1])

    result = s.insertionSortList(head)
    print(str(result))

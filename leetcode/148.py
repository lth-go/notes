#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        first = ListNode(None)
        node = first
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next

            node = node.next

        if left:
            node.next = left
        else:
            node.next = right

        return first.next


if __name__ == '__main__':
    from utils import list_to_node

    s = Solution()

    head = list_to_node([4, 2, 1, 3])

    print(s.sortList(head))

#!/usr/bin/env python
# encoding: utf-8

#  反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

#  说明:
#  1 ≤ m ≤ n ≤ 链表长度。

#  示例:

#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
#  输出: 1->4->3->2->5->NULL


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        left = None
        mid = head

        index = 1
        while index != m:
            index += 1
            left = mid
            mid = mid.next

        count = n - m + 1

        first = True
        foo = None

        r_node = None

        while count:
            if first:
                first = False
                foo = mid

            tmp_r = r_node
            next_node = mid.next

            r_node = mid
            r_node.next = tmp_r
            mid = next_node

            count -= 1

        if mid:
            right = mid
            foo.next = right

        if left:
            left.next = r_node
            return head

        else:
            return r_node


if __name__ == '__main__':
    from utils import list_to_node, node_to_list
    s = Solution()

    #  num_list = [1, 2, 3, 4, 5]
    #  num_list = [5]
    #  num_list = [3, 5]
    num_list = [1, 2, 3]

    head = list_to_node(num_list)

    #  result = s.reverseBetween(head, 2, 4)
    #  result = s.reverseBetween(head, 1, 1)
    #  result = s.reverseBetween(head, 1, 2)
    result = s.reverseBetween(head, 3, 3)

    print(node_to_list(result))

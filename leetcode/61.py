#!/usr/bin/env python
# encoding: utf-8

#  给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

#  示例 1:

#  输入: 1->2->3->4->5->NULL, k = 2
#  输出: 4->5->1->2->3->NULL
#  解释:
#  向右旋转 1 步: 5->1->2->3->4->NULL
#  向右旋转 2 步: 4->5->1->2->3->NULL

#  示例 2:

#  输入: 0->1->2->NULL, k = 4
#  输出: 2->0->1->NULL
#  解释:
#  向右旋转 1 步: 2->0->1->NULL
#  向右旋转 2 步: 1->2->0->NULL
#  向右旋转 3 步: 0->1->2->NULL
#  向右旋转 4 步: 2->0->1->NULL


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        node_list = []
        node = head

        while node:
            node_list.append(node.val)
            node = node.next

        node_len = len(node_list)
        k = k % node_len

        new_node_list = node_list[-k:] + node_list[:-k]

        first_node = ListNode(0)

        pre_node = first_node

        for v in new_node_list:
            node = ListNode(v)

            pre_node.next = node

            pre_node = node

        return first_node.next

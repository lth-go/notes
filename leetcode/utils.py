#!/usr/bin/env python
# encoding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s -> %s' % (self.val, self.next)


def list_to_node(num_list):
    if not num_list:
        return None

    head = ListNode(num_list[0])
    node = head

    for num in num_list[1:]:
        node.next = ListNode(num)
        node = node.next

    return head


def node_to_list(head):
    num_list = []

    node = head
    while node:
        num_list.append(node.val)
        node = node.next

    return num_list


#
# TreeNode
#
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_tree_node(num_list):
    pass


def cache(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]

        rv = function(*args)
        memo[args] = rv
        return rv

    return wrapper

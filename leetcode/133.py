#!/usr/bin/env python
# encoding: utf-8


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        cache = {}

        def foo(node):
            if id(node) in cache:
                return cache[id(node)]

            new_node = Node(node.val, [])

            cache[id(node)] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(foo(neighbor))

            return new_node

        return foo(node)

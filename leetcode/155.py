#!/usr/bin/env python
# encoding: utf-8


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)

        if self.min_list and x > self.min_list[-1]:
            self.min_list.append(self.min_list[-1])
        else:
            self.min_list.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.list:
            return
        self.list.pop()
        self.min_list.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.list:
            return None

        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_list:
            return None

        return self.min_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

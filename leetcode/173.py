#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list = []
        self.index = 0

        def foo(root):
            if not root:
                return

            foo(root.left)
            self.list.append(root.val)
            foo(root.right)

        foo(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        val = self.list[self.index]
        self.index += 1

        return val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """

        return self.index < len(self.list)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

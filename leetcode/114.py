#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '(%s, %s, %s)' % (self.val, self.left, self.right)


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        old_right = None

        if root.right:
            self.flatten(root.right)
            old_right = root.right

        if root.left:
            self.flatten(root.left)
            root.right = root.left
            root.left = None

            if root.right:
                node = root.right
                while node.right:
                    node = node.right

                node.right = old_right


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    s.flatten(root)
    print(root)

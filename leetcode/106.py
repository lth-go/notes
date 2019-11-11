#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not postorder:
            return None

        root = TreeNode(postorder[-1])

        if len(postorder) == 1:
            return root

        b_index = inorder.index(postorder[-1])

        b_left = inorder[:b_index]
        b_right = inorder[b_index + 1:]

        a_left = postorder[: len(b_left)]
        a_right = postorder[len(b_left):-1]

        root.left = self.buildTree(b_left, a_left)
        root.right = self.buildTree(b_right, a_right)

        return root

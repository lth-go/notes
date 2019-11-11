#!/usr/bin/env python
# encoding: utf-8

#  根据一棵树的前序遍历与中序遍历构造二叉树。

#  注意:
#  你可以假设树中没有重复的元素。

#  例如，给出

#  前序遍历 preorder = [3,9,20,15,7]
#  中序遍历 inorder = [9,3,15,20,7]

#  返回如下的二叉树：

#      3
#     / \
#    9  20
#      /  \
#     15   7


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str((self.val, str(self.left), str(self.right)))


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        b_index = inorder.index(preorder[0])

        b_left = inorder[:b_index]
        b_right = inorder[b_index + 1:]

        a_left = preorder[1: len(b_left) + 1]
        a_right = preorder[len(b_left) + 1:]

        root.left = self.buildTree(a_left, b_left)
        root.right = self.buildTree(a_right, b_right)

        return root


if __name__ == '__main__':
    s = Solution()

    #  preorder = [3, 9, 20, 15, 7]
    #  inorder = [9, 3, 15, 20, 7]

    #  preorder = [1, 2, 3]
    #  inorder = [2, 3, 1]

    #  preorder = [1, 2, 3]
    #  inorder = [1, 2, 3]

    preorder = [1, 2, 3]
    inorder = [3, 2, 1]

    result = s.buildTree(preorder, inorder)
    print(result)

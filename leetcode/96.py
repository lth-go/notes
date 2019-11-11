#!/usr/bin/env python
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        cache = {0: 1, 1: 1}

        def foo(n):
            if n in cache:
                return cache[n]

            result = 0
            for index in range(n):
                left = index
                right = n - index - 1

                result += (foo(left) * foo(right))

            cache[n] = result
            return result

        return foo(n)


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 20):
        result = s.numTrees(i)
        print('%s: %s,' % (i, result))

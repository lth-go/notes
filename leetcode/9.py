#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        x = str(x)

        length = len(x)

        for i in range(length / 2):
            if x[i] != x[-1 - i]:
                return False

        return True

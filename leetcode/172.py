#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0

        while n:
            m = n / 5
            result += m
            n = m

        return result

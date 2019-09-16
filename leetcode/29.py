#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        return divmod(dividend, divisor)[1]

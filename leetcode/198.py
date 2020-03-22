#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def cache(function):
            memo = {}

            def wrapper(*args):
                if args in memo:
                    return memo[args]

                rv = function(*args)
                memo[args] = rv
                return rv

            return wrapper

        @cache
        def foo(nums):
            if not nums:
                return 0

            if len(nums) <= 2:
                return max(nums)

            a = nums[0] + foo(nums[2:])
            b = foo(nums[1:])

            return max(a, b)

        return foo(tuple(nums))

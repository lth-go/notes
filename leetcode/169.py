#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = {}

        max_count = 0
        result = None

        for num in nums:
            m.setdefault(num, 0)
            m[num] += 1

            if m[num] > len(nums) / 2.0:
                return num

            if m[num] > max_count:
                max_count = m[num]
                result = num

        return result

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) / 2

            mid_num = nums[mid]

            if nums[mid + 1] < mid_num:
                right = mid
            else:
                left += 1

        return left

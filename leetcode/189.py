#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)

        k = k % nums_len

        nums[:] = nums[-k:] + nums[:-k]

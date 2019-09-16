#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        length = len(nums)

        pre = nums[0]
        index = 1

        for i in range(length):
            if nums[i] == pre:
                continue

            nums[index] = pre = nums[i]
            index += 1

        return index

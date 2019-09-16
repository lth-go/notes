#!/usr/bin/env python
# encoding: utf-8

#  实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

#  必须原地修改，只允许使用额外常数空间。

#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
#  1,2,3 → 1,3,2
#  3,2,1 → 1,2,3
#  1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                break
        else:
            nums[:] = sorted(nums)
            return

        current = nums[i - 1]
        the_min = None
        the_min_index = None

        for index, num in enumerate(nums[i:]):
            if the_min is None or the_min > num > current:
                the_min = num
                the_min_index = index + i

        nums[i - 1], nums[the_min_index] = nums[the_min_index], nums[i - 1]

        nums[i:] = sorted(nums[i:])

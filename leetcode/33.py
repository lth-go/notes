#!/usr/bin/env python
# encoding: utf-8

#  假设按照升序排序的数组在预先未知的某个点上进行了旋转。

#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

#  你可以假设数组中不存在重复的元素。

#  你的算法时间复杂度必须是 O(log n) 级别。

#  示例 1:

#  输入: nums = [4,5,6,7,0,1,2], target = 0
#  输出: 4

#  示例 2:

#  输入: nums = [4,5,6,7,0,1,2], target = 3
#  输出: -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        nums_len = len(nums)

        left = 0
        right = nums_len - 1
        mid = nums_len / 2

        while True:
            left_num = nums[left]
            right_num = nums[right]
            mid_num = nums[mid]

            if target == left_num:
                return left
            elif target == right_num:
                return right
            elif target == mid_num:
                return mid

            if mid_num > left_num:
                if target < mid_num:
                    if target > left_num:
                        right = mid
                        mid = (left + right) / 2
                    elif target < left_num:
                        left = mid
                        mid = (left + right) / 2
                    else:
                        return left
                elif target > mid_num:
                    left = mid
                    mid = (left + right) / 2
                else:
                    return mid

            elif mid_num < left_num:
                if target > mid_num:
                    if target < right_num:
                        left = mid
                        mid = (left + right) / 2
                    elif target > right_num:
                        right = mid
                        mid = (left + right) / 2
                    else:
                        return right

                elif target < mid_num:
                    right = mid
                    mid = (left + right) / 2

                else:
                    return mid
            else:
                return -1

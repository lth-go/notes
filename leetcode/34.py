#!/usr/bin/env python
# encoding: utf-8

#  给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

#  你的算法时间复杂度必须是 O(log n) 级别。

#  如果数组中不存在目标值，返回 [-1, -1]。

#  示例 1:

#  输入: nums = [5,7,7,8,8,10], target = 8
#  输出: [3,4]

#  示例 2:

#  输入: nums = [5,7,7,8,8,10], target = 6
#  输出: [-1,-1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        nums_len = len(nums)

        left = 0
        right = nums_len - 1
        mid = nums_len / 2

        one = None
        two = None

        while True:
            left_num = nums[left]
            right_num = nums[right]
            mid_num = nums[mid]

            if mid_num > target:
                right = mid
                old_mid = mid
                mid = (left + right) / 2
                if mid == old_mid:
                    mid -= 1
                    if mid < 0 or nums[mid] < target:
                        return [-1, -1]

            elif mid_num < target:
                left = mid
                old_mid = mid
                mid = (left + right) / 2
                if mid == old_mid:
                    mid += 1
                    if (mid > nums_len - 1) or nums[mid] > target:
                        return [-1, -1]
            else:
                if left_num < target:
                    old_left = left
                    left = sum(divmod(left + mid, 2))
                    if left == old_left:
                        one = -1

                else:
                    if left > 0 and nums[left - 1] == target:
                        #  old_left = left
                        #  left -= (mid - left) / 2
                        #  if left == old_left:
                        #      left -= 1
                        left -= 1
                    else:
                        one = left

                if right_num > target:
                    old_right = right
                    right = (right + mid) / 2
                    if right == old_right:
                        two = -1

                else:
                    if (right < nums_len - 2) and nums[right + 1] == target:
                        #  old_right = right
                        #  right += (right - mid) / 2
                        #  if right == old_right:
                        #      right += 1
                        right += 1
                    else:
                        two = right

                if one is not None and two is not None:
                    return [one, two]

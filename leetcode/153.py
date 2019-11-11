#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        left = 0
        right = length - 1

        left_num = nums[left]
        right_num = nums[right]

        if left_num <= right_num:
            return left_num

        while True:
            mid = (left + right) / 2

            left_num = nums[left]
            right_num = nums[right]
            mid_num = nums[mid]

            if mid == left:
                return right_num

            if mid_num > left_num:
                left = mid
            else:
                right = mid


if __name__ == '__main__':
    s = Solution()

    #  nums = [3, 4, 5, 1, 2]
    nums = [4, 5, 6, 7, 0, 1, 2]

    result = s.findMin(nums)

    print(result)

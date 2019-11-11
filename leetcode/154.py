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

        if left_num < right_num:
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
                continue

            if mid_num < right_num:
                right = mid
                continue

            if mid_num == left_num:
                left += 1
                if nums[left] < left_num:
                    return nums[left]

                continue

            if mid_num == right_num:
                right -= 1


if __name__ == '__main__':
    s = Solution()

    #  nums = [2, 2, 2, 0, 1]
    #  nums = [3, 1, 3]
    #  nums = [10, 1, 10, 10, 10]
    #  nums = [10, 10, 1, 10, 10, 10]
    nums = [3, 1, 1]
    #  nums = [3, 3, 1, 3]

    result = s.findMin(nums)

    print(result)

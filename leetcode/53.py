#!/usr/bin/env python
# encoding: utf-8

#  给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

#  示例:

#  输入: [-2,1,-3,4,-1,2,1,-5,4],
#  输出: 6
#  解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

#  进阶:

#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        end = 0
        max_sum = None
        sum_ = 0

        nums_len = len(nums)

        while end < nums_len:
            sum_ += nums[end]
            max_sum = max(max_sum, sum_)

            if sum_ < 0:
                sum_ = 0

            end += 1

        return max_sum


if __name__ == '__main__':
    s = Solution()
    result = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)

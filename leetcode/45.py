#!/usr/bin/env python
# encoding: utf-8

#  给定一个非负整数数组，你最初位于数组的第一个位置。

#  数组中的每个元素代表你在该位置可以跳跃的最大长度。

#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。

#  示例:

#  输入: [2,3,1,1,4]
#  输出: 2
#  解释: 跳到最后一个位置的最小跳跃数是 2。
#       从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

#  说明:

#  假设你总是可以到达数组的最后一个位置。


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        start = 0
        end = 0
        far = 0

        nums_len = len(nums)

        while end < nums_len - 1:
            count += 1

            for i in range(start, end + 1):
                far = max(far, nums[i] + i)

            start = end + 1
            end = far

        return count


if __name__ == '__main__':
    solution = Solution()

    nums_list = [
        [2, 3, 1, 1, 4],
        [3, 2, 1],
        [1, 2, 3],
    ]

    for nums in nums_list:
        result = solution.jump(nums)
        print(result)

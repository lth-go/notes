#!/usr/bin/env python
# encoding: utf-8

#  给定一个没有重复数字的序列，返回其所有可能的全排列。

#  示例:

#  输入: [1,2,3]
#  输出:
#  [
#    [1,2,3],
#    [1,3,2],
#    [2,1,3],
#    [2,3,1],
#    [3,1,2],
#    [3,2,1]
#  ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        result = [[nums[0]]]

        for num in nums[1:]:
            new_result = []
            for foo in result:
                for i in range(len(foo) + 1):
                    new_foo = foo[:i] + [num] + foo[i:]
                    new_result.append(new_foo)

            result = new_result

        return result


if __name__ == '__main__':
    s = Solution()

    nums_list = [
        [1, 2, 3, 4],
    ]

    for nums in nums_list:
        result = s.permute(nums)
        print(result)

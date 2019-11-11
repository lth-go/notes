#!/usr/bin/env python
# encoding: utf-8

#  给定一个可包含重复数字的序列，返回所有不重复的全排列。

#  示例:

#  输入: [1,1,2]
#  输出:
#  [
#    [1,1,2],
#    [1,2,1],
#    [2,1,1]
#  ]


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        result = set()
        result.add((nums[0],))

        for num in nums[1:]:
            new_result = set()
            for foo in result:
                for i in range(len(foo) + 1):
                    new_foo = foo[:i] + (num,) + foo[i:]
                    new_result.add(new_foo)

            result = new_result

        return list(result)


if __name__ == '__main__':
    s = Solution()

    nums_list = [
        [1, 1, 2],
    ]

    for nums in nums_list:
        result = s.permuteUnique(nums)
        print(result)

#!/usr/bin/env python
# encoding: utf-8

#  给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

#  说明：解集不能包含重复的子集。

#  示例:

#  输入: nums = [1,2,3]
#  输出:
#  [
#    [3],
#    [1],
#    [2],
#    [1,2,3],
#    [1,3],
#    [2,3],
#    [1,2],
#    []
#  ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def foo(num_list):
            result = []
            for index, num in enumerate(num_list):
                sub_num_list = num_list[index + 1:]
                sub_foo = foo(sub_num_list)

                for bar in sub_foo:
                    result.append([num] + bar)

                result.append([num])

            return result

        return foo(nums) + [[]]


if __name__ == "__main__":
    s = Solution()

    result = s.subsets(
        [1, 2, 3]
    )
    print(result)

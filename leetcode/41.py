#!/usr/bin/env python
# encoding: utf-8

#  给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

#  示例 1:

#  输入: [1,2,0]
#  输出: 3

#  示例 2:

#  输入: [3,4,-1,1]
#  输出: 2

#  示例 3:

#  输入: [7,8,9,11,12]
#  输出: 1

#  说明:

#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        new_nums = nums[:nums_len]
        for num in nums:
            if num > 0 and num <= nums_len:
                new_nums[num - 1] = num

        index = -1
        for index, num in enumerate(new_nums):
            real_num = index + 1
            if num != real_num:
                return real_num
        else:
            index += 1

        return index + 1


if __name__ == '__main__':
    s = Solution()
    nums_list = [
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12],
        [1],
        [],
        [2, 1],
    ]
    for nums in nums_list:
        result = s.firstMissingPositive(nums)
        print(result)

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count_map = {}
        result = set()

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        unique_nums = count_map.keys()

        for index1, num1 in enumerate(unique_nums):
            for num2 in unique_nums[index1 + 1:]:
                num3 = -(num1 + num2)
                if num3 in count_map:
                    if num1 == num3 or num2 == num3:
                        if count_map[num3] < 2:
                            continue

                    result.add(tuple(sorted([num1, num2, num3])))

        if count_map.get(0, 0) >= 3:
            result.add((0, 0, 0))

        return list(result)

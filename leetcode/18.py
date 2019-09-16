#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)

        count_dict = {}
        sum_dict = {}

        for index1, num1 in enumerate(nums):
            count_dict[num1] = count_dict.get(num1, 0) + 1

            for num2 in nums[index1 + 1:]:
                num_tuple = (num1, num2)
                num_sum = num1 + num2

                sum_dict.setdefault(num_sum, [])
                if num_tuple not in sum_dict[num_sum]:
                    sum_dict[num_sum].append(num_tuple)

        result = set()
        for num1, num1_list in sum_dict.items():
            num2 = target - num1

            num2_list = sum_dict.get(num2)
            if num2_list:
                for num1_tuple in num1_list:
                    for num2_tuple in num2_list:
                        result.add(tuple(sorted(num1_tuple + num2_tuple)))

        filter_list = []
        for num_tuple in result:
            for num in num_tuple:
                if num_tuple.count(num) > count_dict[num]:
                    break
            else:
                filter_list.append(num_tuple)

        return filter_list

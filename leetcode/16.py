#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)

        num_range = range(nums[0], nums[-1] + 1)

        diff_map = {}
        count_map = {}

        for num in nums:
            diff_map[num] = 0
            count_map[num] = count_map.get(num, 0) + 1

        max_diff = 2 << 32
        last = nums[0]
        for i in num_range:
            diff = diff_map.get(i, max_diff)
            if diff != 0:
                diff2 = last - i

                if abs(diff2) < abs(diff):
                    diff_map[i] = diff2
            else:
                last = i

        last = nums[-1]
        for i in reversed(num_range):
            diff = diff_map.get(i, max_diff)
            if diff != 0:
                diff2 = last - i

                if abs(diff2) < abs(diff):
                    diff_map[i] = diff2
            else:
                last = i

        diff = None
        result = None
        for index1, num1 in enumerate(nums):
            for num2 in nums[index1 + 1:]:

                num3 = target - num1 - num2

                if nums[0] > num3 > nums[-1]:
                    num3_diff = nums[-1] - num3

                else:
                    num3_diff = diff_map.get(num3)

                if diff is None or abs(num3_diff) < abs(diff):
                    real_num3 = num3 + num3_diff

                    if real_num3 == num1 or real_num3 == num2:
                        if real_num3 == num1 == num2:
                            if not count_map[real_num3] >= 3:
                                continue
                        if not count_map[real_num3] >= 2:
                            continue

                    result = num1 + num2 + num3 + num3_diff
                    diff = num3_diff

        return result

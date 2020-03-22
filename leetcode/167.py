#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers) - 1

        while True:
            left_num = numbers[left]
            right_num = numbers[right]

            s = left_num + right_num

            if s == target:
                return left + 1, right + 1
            elif s > target:
                right -= 1
            elif s < target:
                left += 1

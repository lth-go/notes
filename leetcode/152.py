#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1 and nums[0] < 0:
            return nums[0]

        foo = []

        def x(a, b):
            return a * b

        def reduce_plus(nums):
            if not nums:
                return 0

            return reduce(x, nums)

        def bar(nums, foo):
            if not nums:
                return 0

            if len(foo) % 2 == 0:
                return reduce_plus(nums)

            left = foo[0]
            right = foo[-1]

            if left == right or right - left == 1:
                return max(reduce_plus(nums[:left]), reduce_plus(nums[left + 1:]))

            mid_mul = reduce_plus(nums[left + 1: right])

            left_mul = reduce_plus(nums[:left + 1])
            right_mul = reduce_plus(nums[right:])

            if left_mul < right_mul:
                return mid_mul * left_mul
            else:
                return mid_mul * right_mul

        for index, num in enumerate(nums):
            if num == 0:
                left = bar(nums[:index], foo)
                return max(left, self.maxProduct(nums[index + 1:]))

            if num < 0:
                foo.append(index)

        return bar(nums, foo)


if __name__ == '__main__':
    s = Solution()

    #  nums = [2, 3, -2, 4]
    #  nums = [-2, 0, -1]
    nums = [-2]

    result = s.maxProduct(nums)

    print(result)

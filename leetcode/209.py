#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if sum(nums) < s:
            return 0

        min_len = float('inf')

        total = 0
        end = 0

        for i in range(len(nums)):
            start = i

            if i == 0:
                for index, num in enumerate(nums):
                    total += num

                    if total >= s:
                        min_len = index + 1
                        end = index
                        break
            else:
                before = nums[start - 1]
                current_total = total - before

                while current_total < s and end < len(nums) - 1:
                    end += 1
                    current_total += nums[end]

                if current_total >= s:
                    min_len = min(min_len, end - start + 1)

                total = current_total

        return min_len


if __name__ == '__main__':
    solution = Solution()

    #  s = 7
    #  nums = [2, 3, 1, 2, 4, 3]
    s = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

    result = solution.minSubArrayLen(s, nums)

    print(result)

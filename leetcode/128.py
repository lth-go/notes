#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        foo = set(nums)
        bar = 1

        for num in foo:
            if (num - 1) not in foo:
                current = num
                length = 1
                while True:
                    current += 1
                    if current not in foo:
                        break

                    length += 1

                bar = max(bar, length)

        return bar


if __name__ == '__main__':
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]

    result = solution.longestConsecutive(nums)

    print(result)

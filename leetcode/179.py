#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_str_list = map(str, nums)

        def cmp(a, b):
            ab = a + b
            ba = b + a

            if ab > ba:
                return 1
            elif ab == ba:
                return 0
            elif ab < ba:
                return -1

            return 1

        result = ''.join(sorted(num_str_list, cmp=cmp, reverse=True))

        if result[0] == '0':
            return '0'

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [3, 30, 34, 5, 9]
    result = s.largestNumber(nums)
    print(result)

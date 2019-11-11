#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        elif x == 1:
            return 1

        left = 0
        right = x

        while True:
            mid = (left + right) / 2

            if mid == left:
                return left

            elif mid == right:
                return right

            sqrt = mid * mid

            if sqrt == x:
                return mid

            elif sqrt > x:
                right = mid

            elif sqrt < x:
                left = mid

        return mid


if __name__ == '__main__':
    s = Solution()

    x_list = [1, 2, 4, 8, 9, 10]

    for x in x_list:
        result = s.mySqrt(x)
        print(result)

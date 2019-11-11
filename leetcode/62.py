#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        a = m - 1
        b = n - 1

        total = a + b

        def factorial(n):
            num = 1
            for i in range(1, n + 1):
                num *= i

            return num

        return factorial(total) / (factorial(a) * factorial(b))


if __name__ == '__main__':
    s = Solution()
    result = s.uniquePaths(7, 3)
    print(result)

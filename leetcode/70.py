#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n):
            num = 1
            for i in range(1, n + 1):
                num *= i

            return num

        def c(m, n):
            return f(m) / (f(n) * f(m - n))

        two_count = n / 2

        total = 0
        for i in range(two_count + 1):
            a = n - i
            total += c(a, i)

        return total


if __name__ == '__main__':
    s = Solution()
    n_list = [2, 3]

    for n in n_list:
        result = s.climbStairs(n)
        print(result)

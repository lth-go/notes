#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache = set()

        while True:
            if n == 1:
                return True

            s = 0
            for num in str(n):
                num = int(num)
                s += num ** 2

            n = s
            if n in cache:
                return False

            cache.add(n)


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))

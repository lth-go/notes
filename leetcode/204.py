#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        cache = [1] * n

        cache[0] = cache[1] = 0

        for num in range(2, int(n ** 0.5) + 1):
            if cache[num]:
                j = num + num
                while j < n:
                    cache[j] = 0
                    j += num

        return sum(cache)


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))

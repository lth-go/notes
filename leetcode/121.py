#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        result = 0
        min_price = 2 << 32

        for i in prices:
            if i > min_price:
                result = max(result, i - min_price)
            else:
                min_price = i

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))

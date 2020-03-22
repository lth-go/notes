#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        length = len(prices)
        point_list = []
        high_list = []
        for index in range(1, length - 1):
            before = prices[index - 1]
            current = prices[index]
            after = prices[index + 1]
            if before < current and after <= current:
                point_list.append(index)

        def foo(prices):
            result = 0
            min_price = float('inf')

            for i in prices:
                if i > min_price:
                    result = max(result, i - min_price)
                else:
                    min_price = i

            return result

        if not point_list:
            the_max = max(0, prices[-1] - min(prices))
            return the_max

        the_max = 0
        for index in point_list:
            the_max = max(the_max, foo(prices[:index + 1]) + foo(prices[index:]))

        return the_max


if __name__ == '__main__':
    s = Solution()
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(s.maxProfit(k, prices))

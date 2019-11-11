#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        cache = {1: [1]}

        def foo(numRows):
            result = cache.get(numRows)
            if result:
                return result

            pre = foo(numRows - 1)

            result = []
            for i in range(numRows):
                if i == 0 or i == (numRows - 1):
                    result.append(1)
                else:
                    result.append(pre[i - 1] + pre[i])

            cache[numRows] = result
            return result

        foo(numRows)

        result = []
        for key in range(1, numRows + 1):
            result.append(cache[key])
        return result


if __name__ == '__main__':
    s = Solution()

    print (s.generate(5))

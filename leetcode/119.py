#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 0:
            return [1]

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

        foo(rowIndex + 1)

        return cache[rowIndex + 1]


if __name__ == '__main__':
    s = Solution()

    print (s.getRow(3))

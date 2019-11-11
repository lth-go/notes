#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def foo(n):
            if n == 0:
                return ['0']

            if n == 1:
                return ['0', '1']

            sub_list = foo(n - 1)

            left = []
            right = []

            for sub in sub_list:
                left.append('0' + sub)
                right.insert(0, '1' + sub)

            return left + right

        result = []

        for num in foo(n):
            result.append(int(num, 2))

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.grayCode(0)
    print(result)

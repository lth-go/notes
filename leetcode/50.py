#!/usr/bin/env python
# encoding: utf-8
#  实现 pow(x, n) ，即计算 x 的 n 次幂函数。

#  示例 1:

#  输入: 2.00000, 10
#  输出: 1024.00000

#  示例 2:

#  输入: 2.10000, 3
#  输出: 9.26100

#  示例 3:

#  输入: 2.00000, -2
#  输出: 0.25000
#  解释: 2-2 = 1/22 = 1/4 = 0.25

#  说明:

#      -100.0 < x < 100.0
#      n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = n * -1
            return 1.0 / self.myPow(x, n)

        elif n == 0:
            return 1

        elif n == 1:
            result = x

        else:
            div, mod = divmod(n, 2)
            if mod:
                result = self.myPow(x * x, div) * x
            else:
                result = self.myPow(x * x, div)

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.myPow(2.10000, 3)
    print(result)

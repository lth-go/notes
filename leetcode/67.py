#!/usr/bin/env python
# encoding: utf-8

#  给定两个二进制字符串，返回他们的和（用二进制表示）。

#  输入为非空字符串且只包含数字 1 和 0。

#  示例 1:

#  输入: a = "11", b = "1"
#  输出: "100"

#  示例 2:

#  输入: a = "1010", b = "1011"
#  输出: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_len = len(a)
        b_len = len(b)

        max_len = a_len

        if a_len > b_len:
            b = b.rjust(a_len, '0')

        elif b_len > a_len:
            a = a.rjust(b_len, '0')
            max_len = b_len

        add = False

        i = max_len - 1

        c = []

        while i >= 0:
            a_num = int(a[i])
            b_num = int(b[i])

            c_num = a_num + b_num

            if add:
                c_num += 1

            if c_num > 1:
                add = True
            else:
                add = False

            c.insert(0, str(c_num % 2))

            i -= 1

        if add:
            c.insert(0, '1')

        return ''.join(c)


if __name__ == '__main__':
    s = Solution()
    result = s.addBinary('1010', '1011')
    print(result)

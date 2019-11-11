#!/usr/bin/env python
# encoding: utf-8

#  一条包含字母 A-Z 的消息通过以下方式进行了编码：

#  'A' -> 1
#  'B' -> 2
#  ...
#  'Z' -> 26

#  给定一个只包含数字的非空字符串，请计算解码方法的总数。

#  示例 1:

#  输入: "12"
#  输出: 2
#  解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

#  示例 2:

#  输入: "226"
#  输出: 3
#  解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


class Solution(object):
    cache = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 1:
            if s == '0':
                return 0
            return 1

        one = int(s[0])
        two = int(s[1])

        if len(s) == 2:
            if one > 2:
                if two == 0:
                    return 0
                return 1

            if one == 0:
                return 0

            if two == 0:
                return 1

            if one == 2 and two > 6:
                return 1

            return 2

        if s in self.cache:
            return self.cache[s]

        if one == 0:
            return 0

        if one > 2:
            if two == 0:
                return 0
            return self.numDecodings(s[1:])

        if two == 0:
            return self.numDecodings(s[2:])

        if one == 2 and two > 6:
            return self.numDecodings(s[2:])

        result = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        self.cache[s] = result
        return result


if __name__ == '__main__':
    s = Solution()
    string = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    result = s.numDecodings(string)
    print(result)

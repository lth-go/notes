#!/usr/bin/env python
# encoding: utf-8

#  给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

#  例如，给出 n = 3，生成结果为：

#  [
#    "((()))",
#    "(()())",
#    "(())()",
#    "()(())",
#    "()()()"
#  ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        elif n == 1:
            return ['()']

        result = set()
        for i in range(1, n):
            a = self.generateParenthesis(i)
            b = self.generateParenthesis(n - i)

            if i == 1:
                for sub in b:
                    result.add('(' + sub + ')')

            for _a in a:
                for _b in b:
                    result.add(_a + _b)

        return list(result)

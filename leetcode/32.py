#!/usr/bin/env python
# encoding: utf-8
#  给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

#  示例 1:

#  输入: "(()"
#  输出: 2
#  解释: 最长有效括号子串为 "()"

#  示例 2:

#  输入: ")()())"
#  输出: 4
#  解释: 最长有效括号子串为 "()()"


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        left = '('

        current_len = 0
        max_len = 0

        base = -1
        for index, c in enumerate(s):
            if c == left:
                stack.append((c, index))

            else:
                if stack and stack.pop()[0] == left:
                    if stack:
                        current_base = stack[-1][1]
                    else:
                        current_base = base

                    current_len = index - current_base
                    if current_len > max_len:
                        max_len = current_len

                else:
                    stack = []
                    if current_len > max_len:
                        max_len = current_len
                    current_len = 0
                    base = index

        if stack:
            last_len = index - stack[-1][1]
            if last_len > max_len:
                max_len = last_len
        else:
            if current_len > max_len:
                max_len = current_len

        return max_len

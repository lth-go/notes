#!/usr/bin/env python
# encoding: utf-8

#  给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

#  你可以对一个单词进行如下三种操作：

#      插入一个字符
#      删除一个字符
#      替换一个字符

#  示例 1:

#  输入: word1 = "horse", word2 = "ros"
#  输出: 3
#  解释:
#  horse -> rorse (将 'h' 替换为 'r')
#  rorse -> rose (删除 'r')
#  rose -> ros (删除 'e')

#  示例 2:

#  输入: word1 = "intention", word2 = "execution"
#  输出: 5
#  解释:
#  intention -> inention (删除 't')
#  inention -> enention (将 'i' 替换为 'e')
#  enention -> exention (将 'n' 替换为 'x')
#  exention -> exection (将 'n' 替换为 'c')
#  exection -> execution (插入 'u')


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        word1_len = len(word1)
        word2_len = len(word2)

        dp = [[0] * (word1_len + 1) for _ in range(word2_len + 1)]

        for x in range(1, word1_len + 1):
            dp[0][x] = dp[0][x - 1] + 1

        for y in range(1, word2_len + 1):
            dp[y][0] = dp[y - 1][0] + 1

        for y in range(1, word2_len + 1):
            for x in range(1, word1_len + 1):
                if word1[x - 1] == word2[y - 1]:
                    dp[y][x] = dp[y - 1][x - 1]
                else:
                    dp[y][x] = min(dp[y - 1][x - 1], dp[y][x - 1], dp[y - 1][x]) + 1

        return dp[-1][-1]

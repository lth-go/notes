#  给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

#  示例 1：

#  输入: "babad"
#  输出: "bab"
#  注意: "aba" 也是一个有效答案。

#  示例 2：

#  输入: "cbbd"
#  输出: "bb"

#  动态规划的方法 对于字符串str，假设dp[i,j]=1表示str[i...j]是回文子串，那个必定存在dp[i+1,j-1]=1。


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        len_s = len(s)
        if len_s == 1:
            return s

        longest = 1
        start = 0

        dp = [[0] * len_s for _ in range(len_s)]

        for i in range(len_s):
            dp[i][i] = 1

            if i < len_s - 1:
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = 1
                    start = i
                    longest = 2

        for l in range(3, len_s + 1):  # 子串长度
            for i in range(0, len_s + 1 - l):
                j = l + i - 1  # 终点
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    start = i
                    longest = l
        return s[start: start + longest]

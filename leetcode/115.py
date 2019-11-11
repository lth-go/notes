#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_len = len(s)
        t_len = len(t)

        dp = [[0 for _ in range(t_len + 1)] for _ in range(s_len + 1)]

        for i in range(s_len + 1):
            dp[i][0] = 1

        for i in range(1, s_len + 1):
            for j in range(1, t_len + 1):
                s_char = s[i - 1]
                t_char = t[j - 1]
                if s_char == t_char:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    S = "rabbbit"
    T = "rabbit"
    #  S = "babgbag"
    #  T = "bag"
    result = s.numDistinct(S, T)
    print(result)

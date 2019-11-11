#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if sorted(s1 + s2) != sorted(s3):
            return False

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len == 0:
            return s2 == s3

        if s2_len == 0:
            return s1 == s3

        dp = [[False] * (s2_len + 1) for _ in range(s1_len + 1)]

        for i in range(s1_len + 1):
            for j in range(s2_len + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue

                if i == 0:
                    dp[i][j] = s2[:j] == s3[:j]
                    continue

                if j == 0:
                    dp[i][j] = s1[:i] == s3[:i]
                    continue

                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()

    #  s1 = "aabcc"
    #  s2 = "dbbca"
    #  s3 = "aadbbcbcac"

    #  s1 = "aabcc"
    #  s2 = "dbbca"
    #  s3 = "aadbbbaccc"

    s1 = "aabaac"
    s2 = "aadaaeaaf"
    s3 = "aadaaeaabaafaac"
    result = s.isInterleave(s1, s2, s3)
    print(result)

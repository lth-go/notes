#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        x_len = len(triangle)
        if x_len == 0:
            return 0
        y_len = len(triangle[-1])

        if y_len == 0:
            return 0

        dp = [[0 for _ in range(y_len)] for _ in range(x_len)]

        for i in range(x_len):
            for j in range(y_len):
                if j >= len(triangle[i]):
                    continue

                if i == 0:
                    dp[i][j] = triangle[0][0]
                    continue

                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                else:
                    if (j >= len(triangle[i - 1])):
                        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    result = s.minimumTotal(triangle)
    print(result)

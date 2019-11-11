#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        max_x = len(obstacleGrid[0])
        max_y = len(obstacleGrid)

        dp = [[0] * max_x for _ in range(max_y)]

        for x in range(max_x):
            for y in range(max_y):

                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                    continue

                if x == 0 and y == 0:
                    dp[0][0] = 1
                    continue

                up = 0
                left = 0

                if x > 0:
                    left = dp[y][x - 1]

                if y > 0:
                    up = dp[y - 1][x]

                dp[y][x] = left + up

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    result = s.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])
    print(result)

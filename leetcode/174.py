#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        x_len = len(dungeon[0])
        y_len = len(dungeon)

        dp = [[float('inf') for _ in range(x_len + 1)] for _ in range(y_len + 1)]

        for x in range(x_len - 1, -1, -1):
            for y in range(y_len - 1, -1, -1):

                right = dp[y][x + 1]
                down = dp[y + 1][x]

                at_least = min(right, down)
                if at_least == float('inf'):
                    at_least = 0

                current = dungeon[y][x]

                if at_least - current < 0:
                    dp[y][x] = 0
                else:
                    dp[y][x] = at_least - current

        return dp[0][0] + 1


if __name__ == '__main__':
    s = Solution()
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5],
    ]

    result = s.calculateMinimumHP(dungeon)

    print(result)

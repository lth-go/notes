#!/usr/bin/env python
# encoding: utf-8

#  给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

#  说明：每次只能向下或者向右移动一步。

#  示例:

#  输入:
#  [
#    [1,3,1],
#    [1,5,1],
#    [4,2,1]
#  ]
#  输出: 7
#  解释: 因为路径 1→3→1→1→1 的总和最小。


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_x = len(grid[0])
        max_y = len(grid)

        dp = [[None for _ in range(max_x)] for _ in range(max_y)]

        dp[0][0] = grid[0][0]

        for x in range(max_x):
            for y in range(max_y):

                if x == 0 and y == 0:
                    continue

                left = None
                up = None

                if y > 0:
                    up = dp[y - 1][x]

                if x > 0:
                    left = dp[y][x - 1]

                if left is None:
                    min_num = up
                elif up is None:
                    min_num = left
                else:
                    min_num = min(left, up)

                dp[y][x] = min_num + grid[y][x]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()

    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = s.minPathSum(grid)
    print(result)

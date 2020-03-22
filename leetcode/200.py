#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        y_len = len(grid)
        x_len = len(grid[0])

        foo = set()
        count = 0

        def found(x, y):
            if x < 0 or y < 0 or x >= x_len or y >= y_len:
                return

            if (x, y) in foo:
                return

            foo.add((x, y))

            val = grid[y][x]
            if val == '0':
                return

            up = (x, y - 1)
            down = (x, y + 1)
            left = (x - 1, y)
            right = (x + 1, y)

            found(*up)
            found(*down)
            found(*left)
            found(*right)

        for y in range(y_len):
            for x in range(x_len):
                val = grid[y][x]
                if val == '0':
                    continue

                if (x, y) in foo:
                    continue

                found(x, y)

                count += 1

        return count

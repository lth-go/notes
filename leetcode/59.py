#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num_list = range(1, n * n + 1)

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        left = 1
        down = 2
        right = 3
        up = 4

        x = y = 0

        direct = right
        for num in num_list:
            matrix[y][x] = num

            if direct == right:
                if x < n - 1 and matrix[y][x + 1] == 0:
                    x += 1
                else:
                    y += 1
                    direct = down

            elif direct == down:
                if y < n - 1 and matrix[y + 1][x] == 0:
                    y += 1
                else:
                    x -= 1
                    direct = left

            elif direct == left:
                if x > 0 and matrix[y][x - 1] == 0:
                    x -= 1
                else:
                    y -= 1
                    direct = up

            elif direct == up:
                if y > 0 and matrix[y - 1][x] == 0:
                    y -= 1
                else:
                    x += 1
                    direct = right

        return matrix


if __name__ == '__main__':
    s = Solution()

    result = s.generateMatrix(3)

    print(result)

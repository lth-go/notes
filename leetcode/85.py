#!/usr/bin/env python
# encoding: utf-8
#  给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

#  示例:

#  输入: [ ["1","0","1","0","0"], ["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"] ] 输出: 6


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        if not matrix[0]:
            return 0

        x_max = len(matrix[0])
        y_max = len(matrix)

        for y in range(y_max):
            for x in range(x_max):
                if matrix[y][x] == '0':
                    matrix[y][x] = 0
                    continue

                if y > 0:
                    matrix[y][x] = matrix[y - 1][x] + 1
                else:
                    matrix[y][x] = 1

        return max(map(self.largestRectangleArea, matrix))

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        stack = []
        max_area = 0

        heights = [0] + heights + [0]
        heights_len = len(heights)

        for index in range(heights_len):
            height = heights[index]

            while stack and height < heights[stack[-1]]:
                h = stack.pop()
                max_area = max(heights[h] * (index - stack[-1] - 1), max_area)

            stack.append(index)

        return max_area


if __name__ == '__main__':
    s = Solution()
    #  matrix = [
    #      ["1", "0", "1", "0", "0"],
    #      ["1", "0", "1", "1", "1"],
    #      ["1", "1", "1", "1", "1"],
    #      ["1", "0", "0", "1", "0"],
    #  ]
    matrix = [
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
    ]
    result = s.maximalRectangle(matrix)
    from pprint import pprint
    pprint(result)

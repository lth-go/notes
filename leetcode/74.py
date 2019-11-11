#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        if not matrix[0]:
            return False

        #  max_x = len(matrix[0])
        max_y = len(matrix)

        left_y = 0
        right_y = max_y

        while True:
            y = (left_y + right_y) / 2

            if left_y == right_y:
                break

            if matrix[y][0] <= target <= matrix[y][-1]:
                break

            if target < matrix[y][0]:
                right_y = y
            elif target > matrix[y][-1]:
                if left_y == y:
                    left_y += 1
                    if left_y >= max_y:
                        break
                else:
                    left_y = y

        return target in matrix[y]


if __name__ == '__main__':
    s = Solution()
    input_list = [
        (
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            3
        ),
        (
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            13
        ),
        (
            [
                [1],
            ],
            2
        )
    ]

    for input_ in input_list:
        result = s.searchMatrix(*input_)
        print(result)

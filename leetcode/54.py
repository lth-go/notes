#!/usr/bin/env python
# encoding: utf-8

#  给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

#  示例 1:

#  输入:
#  [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
#  ]
#  输出: [1,2,3,6,9,8,7,4,5]

#  示例 2:

#  输入:
#  [
#    [1, 2, 3, 4],
#    [5, 6, 7, 8],
#    [9,10,11,12]
#  ]
#  输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        result = []

        right = 1
        down = 2
        left = 3
        up = 4

        direct = right
        while matrix:
            if direct == right:
                result.extend(matrix.pop(0))
                direct = down

            elif direct == down:
                for row in matrix:
                    if row:
                        result.append(row.pop())

                direct = left

            elif direct == left:
                result.extend(reversed(matrix.pop()))
                direct = up

            elif direct == up:
                new = []
                for row in matrix:
                    if row:
                        new.append(row.pop(0))

                result.extend(reversed(new))

                direct = right
            else:
                break

        return result


if __name__ == '__main__':
    s = Solution()

    matrix_list = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ],
        [[7], [9], [6]],
    ]

    for matrix in matrix_list:
        result = s.spiralOrder(matrix)
        print(result)

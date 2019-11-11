#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        x_len = len(board[0])
        y_len = len(board)

        exclude_set = set()

        def foo(x, y):
            if x < 0 or y < 0:
                return

            if x >= x_len or y >= y_len:
                return

            if board[y][x] == 'X':
                return

            if (x, y) in exclude_set:
                return

            exclude_set.add((x, y))

            foo(x - 1, y)
            foo(x + 1, y)
            foo(x, y - 1)
            foo(x, y + 1)

        for x in range(x_len):
            foo(x, 0)
            foo(x, y_len - 1)

        for y in range(y_len):
            foo(0, y)
            foo(x_len - 1, y)

        for y in range(y_len):
            for x in range(x_len):
                if board[y][x] == 'O' and (x, y) not in exclude_set:
                    board[y][x] = 'X'


if __name__ == '__main__':
    solution = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    solution.solve(board)

    print(board)

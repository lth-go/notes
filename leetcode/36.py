#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = []
            for num in board[i]:
                if num == '.':
                    continue
                row.append(num)

            if len(row) != len(set(row)):
                return False

            column = []
            for line in board:
                num = line[i]
                if num == '.':
                    continue
                column.append(num)

            if len(column) != len(set(column)):
                return False

            box = []
            x_index = range((i % 3) * 3, (i % 3) * 3 + 3)
            y_index = range((i / 3) * 3, (i / 3) * 3 + 3)

            for y in y_index:
                for x in x_index:
                    num = board[y][x]

                    if num == '.':
                        continue
                    box.append(num)

            if len(box) != len(set(box)):
                return False

        return True

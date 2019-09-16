#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint
import time


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        guess_dict = self.board_to_guess_dict(board)

        new_guess_dict = self.complete_and_guess(guess_dict)

        board[:] = self.guess_dict_to_board(new_guess_dict)

        return None

    def complete_and_guess(self, guess_dict):
        guess_dict = self.complete(guess_dict)
        if guess_dict is None:
            return None

        guess_dict = self.guess(guess_dict)
        if guess_dict is None:
            return None

        return guess_dict

    def guess(self, guess_dict):
        min_value_set_len = 10

        for x in range(9):
            for y in range(9):
                value_set = guess_dict[(x, y)]

                value_set_len = len(value_set)
                if value_set_len == 1:
                    continue

                if value_set_len < min_value_set_len:
                    min_value_set_len = value_set_len

                    if min_value_set_len == 2:
                        break

        if min_value_set_len == 10:
            return guess_dict

        for guess_value in value_set:
            new_guess_dict = self.copy_guess_dict(guess_dict)

            new_guess_dict[(x, y)] = set([guess_value])

            new_guess_dict = self.complete_and_guess(new_guess_dict)

            if new_guess_dict:
                return new_guess_dict

        return None

    def complete(self, guess_dict):
        x_dict = {}
        y_dict = {}
        box_dict = {}

        box = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in range(9):
            x_dict[i] = set()
            y_dict[i] = set()
            box_dict[i] = set()

        for index, value_set in guess_dict.items():
            x, y = index
            value_set_len = len(value_set)

            if value_set_len == 1:
                num = list(value_set)[0]

                x_dict[x].add(num)
                y_dict[y].add(num)

                box_index = box[y / 3][x / 3]
                box_dict[box_index].add(num)

        update = False

        for index, value_set in guess_dict.items():
            x, y = index
            value_set_len = len(value_set)

            if value_set_len > 1:
                box_index = box[y / 3][x / 3]

                before_len = len(value_set)

                new_value_set = value_set - x_dict[x] - y_dict[y] - box_dict[box_index]
                if not new_value_set:
                    return None

                after_len = len(new_value_set)
                if after_len < before_len:
                    update = True

                if after_len == 1:
                    num = list(new_value_set)[0]
                    x_dict[x].add(num)
                    y_dict[y].add(num)
                    box_dict[box_index].add(num)

                guess_dict[(x, y)] = new_value_set

        if update:
            return self.complete(guess_dict)

        return guess_dict

    def board_to_guess_dict(self, board):
        num_set = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        guess_dict = {}

        x_dict = {}
        y_dict = {}
        box_dict = {}

        box = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in range(9):
            x_dict[i] = set()
            y_dict[i] = set()
            box_dict[i] = set()

        for y, row in enumerate(board):
            for x, num in enumerate(row):

                box_index = box[y / 3][x / 3]

                if num != '.':
                    new_value_set = set([num])

                    x_dict[x].add(num)
                    y_dict[y].add(num)
                    box_dict[box_index].add(num)

                    guess_dict[(x, y)] = new_value_set

        for y, row in enumerate(board):
            for x, num in enumerate(row):

                box_index = box[y / 3][x / 3]

                if num == '.':
                    new_value_set = num_set - x_dict[x] - y_dict[y] - box_dict[box_index]
                    if not new_value_set:
                        return None

                    guess_dict[(x, y)] = new_value_set

        return guess_dict

    def guess_dict_to_board(self, guess_dict):
        board = [['.' for _ in range(9)] for _ in range(9)]
        for index, value_set in guess_dict.items():
            if not len(value_set) == 1:
                continue

            x, y = index
            board[y][x] = list(value_set)[0]
        return board

    def copy_guess_dict(self, guess_dict):
        new_guess_dict = guess_dict.copy()

        for k, v in new_guess_dict.items():
            if isinstance(v, set):
                new_guess_dict[k] = v.copy()

        return new_guess_dict


if __name__ == '__main__':
    board_list = [
        #  [
        #      ['.', '.', '9', '7', '4', '8', '.', '.', '.'],
        #      ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
        #      ['.', '2', '.', '1', '.', '9', '.', '.', '.'],
        #      ['.', '.', '7', '.', '.', '.', '2', '4', '.'],
        #      ['.', '6', '4', '.', '1', '.', '5', '9', '.'],
        #      ['.', '9', '8', '.', '.', '.', '3', '.', '.'],
        #      ['.', '.', '.', '8', '.', '3', '.', '2', '.'],
        #      ['.', '.', '.', '.', '.', '.', '.', '.', '6'],
        #      ['.', '.', '.', '2', '7', '5', '9', '.', '0']
        #  ],
        [
            [".", ".", ".", "2", ".", ".", ".", "6", "3"],
            ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
            [".", ".", "1", ".", ".", "3", "9", "8", "."],
            [".", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "3", "8", ".", ".", "."],
            [".", "3", ".", ".", ".", ".", ".", ".", "."],
            [".", "2", "6", "3", ".", ".", "5", ".", "."],
            ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
            ["4", "7", ".", ".", ".", "1", ".", ".", "."]
        ],
    ]

    for board in board_list:
        start = time.time()
        s = Solution()
        s.solveSudoku(board)
        print(time.time() - start)
        pprint(board)

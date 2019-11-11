#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n

        default_guess_dict = {}
        for x in range(n):
            for y in range(n):
                default_guess_dict[(x, y)] = None

        guess_dict_list = self.guess(0, default_guess_dict)

        return [self.format(guess_dict) for guess_dict in guess_dict_list]

    def guess(self, y, guess_dict):
        guess_dict_list = []

        found = False
        for x in range(self.n):
            index = (x, y)
            if guess_dict[index] is None:
                new_guess_dict = guess_dict.copy()
                new_guess_dict[index] = True

                self.complete(new_guess_dict, x, y)

                if y + 1 == self.n:
                    guess_dict_list.append(new_guess_dict)
                    found = True
                else:
                    sub = self.guess(y + 1, new_guess_dict)
                    if sub:
                        found = True
                        guess_dict_list.extend(sub)
        if not found:
            return []

        return guess_dict_list

    def complete(self, guess_dict, x, y):
        for i in range(self.n):
            guess_dict[(x, i)] = False
            guess_dict[(i, y)] = False

        # 左上
        i = 1
        while True:
            xx = x - i
            yy = y - i

            if xx < 0 or yy < 0:
                break

            guess_dict[(xx, yy)] = False

            i += 1

        # 左下
        i = 1
        while True:
            xx = x - i
            yy = y + i

            if xx < 0 or yy == self.n:
                break

            guess_dict[(xx, yy)] = False

            i += 1

        # 右上
        i = 1
        while True:
            xx = x + i
            yy = y - i

            if xx == self.n or yy < 0:
                break

            guess_dict[(xx, yy)] = False

            i += 1

        # 右下
        i = 1
        while True:
            xx = x + i
            yy = y + i

            if xx == self.n or yy == self.n:
                break

            guess_dict[(xx, yy)] = False

            i += 1

        guess_dict[(x, y)] = True

    def format(self, guess_dict):

        result = ['' for _ in range(self.n)]
        for x in range(self.n):
            for y in range(self.n):
                if guess_dict[(x, y)]:

                    result[y] = x * '.' + 'Q' + (self.n - x - 1) * '.'
                    break

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.solveNQueens(0)
    pprint(result)

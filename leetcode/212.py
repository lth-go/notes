#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        y_len = len(board)
        x_len = len(board[0])

        foo = {}
        for x in range(x_len):
            for y in range(y_len):
                foo[(x, y)] = False

        def match(word, point=None):
            if not word:
                return True

            if point is None:

                char = word[0]

                for x in range(x_len):
                    for y in range(y_len):
                        if char == board[y][x]:
                            foo[(x, y)] = True

                            ok = match(word[1:], (x, y))

                            foo[(x, y)] = False

                            if ok:
                                return True
                return False

            x, y = point

            up = x, y - 1
            down = x, y + 1
            left = x - 1, y
            right = x + 1, y

            if x == 0:
                left = None

            if y == 0:
                up = None

            if x == x_len - 1:
                right = None

            if y == y_len - 1:
                down = None

            char = word[0]
            for direct in [up, down, left, right]:
                if direct:
                    x_, y_ = direct
                    if char == board[y_][x_] and not foo[(x_, y_)]:
                        foo[(x_, y_)] = True

                        ok = match(word[1:], (x_, y_))

                        foo[(x_, y_)] = False

                        if ok:
                            return True

            return False

        result = []
        for word in words:
            if match(word):
                result.append(word)

        return result


if __name__ == '__main__':
    from pprint import pprint

    s = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]

    pprint(s.findWords(board, words))

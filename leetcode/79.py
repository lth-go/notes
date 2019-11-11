#!/usr/bin/env python
# encoding: utf-8

#  给定一个二维网格和一个单词，找出该单词是否存在于网格中。

#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

#  示例:

#  board =
#  [
#    ['A','B','C','E'],
#    ['S','F','C','S'],
#    ['A','D','E','E']
#  ]

#  给定 word = "ABCCED", 返回 true.
#  给定 word = "SEE", 返回 true.
#  给定 word = "ABCB", 返回 false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        user_set = set()

        max_x = len(board[0])
        max_y = len(board)

        def match(user_set, index, word):
            if not word:
                return True

            x, y = index
            left = (x - 1, y)
            right = (x + 1, y)
            up = (x, y - 1)
            down = (x, y + 1)
            if x == 0:
                left = None
            if y == 0:
                up = None
            if x == max_x - 1:
                right = None
            if y == max_y - 1:
                down = None
            next_list = filter(None, [left, right, up, down])

            current_word = word[0]

            for index in next_list:
                if index in user_set:
                    continue

                x, y = index
                if board[y][x] == current_word:
                    new_user_set = user_set.copy()
                    new_user_set.add(index)
                    ok = match(new_user_set, index, word[1:])
                    if ok:
                        return True

            return False

        first_word = word[0]

        for y in range(max_y):
            for x in range(max_x):
                if board[y][x] == first_word:
                    index = (x, y)
                    new_user_set = user_set.copy()
                    new_user_set.add(index)
                    ok = match(new_user_set, index, word[1:])
                    if ok:
                        return True
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "SEE",
    )

    print(result)

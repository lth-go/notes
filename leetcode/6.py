#  将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

#  L   C   I   R
#  E T O E S I I G
#  E   D   H   N

#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

#  请你实现这个将字符串进行指定行数变换的函数：

#  string convert(string s, int numRows);


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        len_s = len(s)

        # 一下一上的字符数
        num = numRows * 2 - 2

        num_col = (len_s / num + 1) * (1 + numRows - 2)

        array = [[''] * num_col for _ in range(numRows)]

        i = 0
        j = 0
        up = True
        for char in s:
            array[i][j] = char

            if up:
                i += 1
                if i == numRows - 1:
                    up = False
            else:
                i -= 1
                if i == 0:
                    up = True

                j += 1

        result = ''
        for char_list in array:
            for char in char_list:
                result += char

        return result

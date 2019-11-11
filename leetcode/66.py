#!/usr/bin/env python
# encoding: utf-8

#  给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

#  你可以假设除了整数 0 之外，这个整数不会以零开头。

#  示例 1:

#  输入: [1,2,3]
#  输出: [1,2,4]
#  解释: 输入数组表示数字 123。

#  示例 2:

#  输入: [4,3,2,1]
#  输出: [4,3,2,2]
#  解释: 输入数组表示数字 4321。


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        add = False
        digits_len = len(digits)

        index = digits_len - 1

        digits[index] = digits[index] + 1

        while True:
            num = digits[index]

            if add:
                num += 1

            digits[index] = num % 10

            if num < 10:
                break

            index -= 1
            add = True

            if index < 0:
                digits.insert(0, 1)
                break

        return digits


if __name__ == '__main__':
    s = Solution()

    digits_list = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9, 9, 9],
    ]

    for digits in digits_list:
        result = s.plusOne(digits)
        print(result)

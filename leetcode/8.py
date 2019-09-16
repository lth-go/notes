#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        positive = None
        start = False
        num = ''
        for char in str:
            if char == ' ':
                if start:
                    break
                continue

            if char == '-':
                if positive is not None:
                    break

                if start:
                    break

                positive = False
                start = True

            elif char == '+':
                if positive is not None:
                    break

                if start:
                    break

                positive = True
                start = True

            elif char in num_list:
                num += char
                start = True

            else:
                break

        if not num:
            return 0

        num = int(num)

        if positive is False:
            num = -1 * num

        if num < -(2 ** 31):
            return -(2 ** 31)

        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return num

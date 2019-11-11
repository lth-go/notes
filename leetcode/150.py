#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        while tokens:
            token = tokens.pop(0)

            if token in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    result = num2 + num1
                elif token == '-':
                    result = num2 - num1
                elif token == '*':
                    result = num2 * num1
                elif token == '/':
                    result = int(float(num2) / num1)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == '__main__':
    s = Solution()

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    result = s.evalRPN(tokens)
    print(result)

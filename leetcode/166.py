#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        minus = numerator * denominator >= 0

        numerator = abs(numerator)
        denominator = abs(denominator)

        interger, numerator = divmod(numerator, denominator)

        if not minus:
            interger = '-%s' % interger
        else:
            interger = str(interger)

        if numerator == 0:
            return interger

        def reduce_a_fraction(num1, num2):
            if num1 == 0:
                return (0, 1)

            n, m = num1, num2

            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n

            return num1 / n, num2 / n

        numerator, denominator = reduce_a_fraction(numerator, denominator)

        foo = {}

        s = ''

        while True:
            if numerator in foo:
                loop = s[foo[numerator]:]
                s = s.replace(loop, '(%s)' % loop)
                break

            foo[numerator] = len(s)

            i, numerator = divmod(numerator * 10, denominator)

            s += str(i)

            if numerator == 0:
                break

        if s == '0':
            return interger

        return '%s.%s' % (interger, s)


if __name__ == '__main__':
    s = Solution()

    #  numerator = 1
    #  denominator = 2

    #  numerator = 2
    #  denominator = 1

    #  numerator = 2
    #  denominator = 3

    #  numerator = 1234
    #  denominator = 1235

    #  numerator = -50
    #  denominator = 8

    #  numerator = 2
    #  denominator = 1

    numerator = 7
    denominator = -12

    result = s.fractionToDecimal(numerator, denominator)

    print(result)

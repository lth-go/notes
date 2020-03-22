#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ascii_uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        x = len(ascii_uppercase)

        b = []
        while n != 0:
            s, y = divmod(n - 1, x)

            b.insert(0, ascii_uppercase[y])

            n = s

        return ''.join(b)


if __name__ == '__main__':
    s = Solution()

    print(s.convertToTitle(701))

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.replace('CM', 'DCCCC')
        s = s.replace('CD', 'CCCC')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('XL', 'XXXX')
        s = s.replace('IX', 'VIIII')
        s = s.replace('IV', 'IIII')

        d = {
            'M': 0,
            'D': 0,
            'C': 0,
            'L': 0,
            'X': 0,
            'V': 0,
            'I': 0,
        }

        for char in s:
            d[char] = d[char] + 1

        return 1000 * d['M'] + 500 * d['D'] + 100 * d['C'] + 50 * d['L'] + 10 * d['X'] + 5 * d['V'] + d['I']

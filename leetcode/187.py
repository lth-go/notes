#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        foo = {}

        for i in range(len(s) - 9):
            string = s[i: i + 10]
            foo.setdefault(string, 0)
            foo[string] += 1

        result = []
        for k, v in foo.items():
            if v > 1:
                result.append(k)

        return result

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        a.reverse()

        return ' '.join(a)

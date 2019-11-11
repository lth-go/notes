#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip(' ').rsplit(' ', 1)[-1])

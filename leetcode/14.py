#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        min_str = min(strs)
        min_len = len(min(strs))

        p = ''
        for i in range(min_len):
            char = min_str[i]

            for s in strs:
                if s[i] != char:
                    return p

            p += char

        return p

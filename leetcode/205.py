#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cache = {}
        cache_b = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in cache:
                if cache[a] != b:
                    return False

            cache[a] = b

            if b in cache_b:
                if cache_b[b] != a:
                    return False
            cache_b[b] = a

        return True

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(s, p):
            if p == '':
                return s == ''

            if len(p) == 1:
                if len(s) != 1:
                    return False

                return p[0] in ['.', s[0]]

            if p[1] == '*':
                if len(s) == 0 or p[0] not in ['.', s[0]]:
                    return match(s, p[2:])

                ok = match(s[1:], p)
                if ok:
                    return True

                return match(s, p[2:])

            else:
                if not s:
                    return False

                if p[0] not in ['.', s[0]]:
                    return False

                return match(s[1:], p[1:])

        return match(s, p)

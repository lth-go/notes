#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    cache = set()

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1, s2) in self.cache:
            return False

        if s1 == s2:
            return True

        s1_len = len(s1)

        if s1_len == 1:
            return False

        if sorted(s1) != sorted(s2):
            return False

        for index in range(1, s1_len):
            prefix = s1[:index]
            ext = s1[index:]

            if self.isScramble(prefix, s2[:index]):
                if self.isScramble(ext, s2[index:]):
                    return True

            if self.isScramble(prefix, s2[-index:]):
                if self.isScramble(ext, s2[:-index]):
                    return True

        self.cache.add((s1, s2))

        return False


if __name__ == '__main__':
    #  s1 = "abcde"
    #  s2 = "caebd"
    #  s1 = "great"
    #  s2 = "rgeat"
    #  s1 = 'abb'
    #  s2 = 'bba'
    #  s1 = 'abc'
    #  s2 = 'cba'

    #  s1 = "abcdefghij"
    #  s2 = "efghijcadb"

    s1 = "abcdefghijklmn"
    s2 = "efghijklmncadb"
    s = Solution()
    print(s.isScramble(s1, s2))

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowercase = set('abcdefghijklmnopqrstuvwxyz0123456789')

        char_list = []

        for char in s:
            char = char.lower()
            if char in lowercase:
                char_list.append(char)

        char_len = len(char_list)
        if char_len <= 1:
            return True

        a = char_list[:char_len / 2]
        b = char_list[-len(a):][::-1]

        return a == b


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("aaa"))

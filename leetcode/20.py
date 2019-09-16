#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)

            elif char == ')':
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False

            elif char == ']':
                if not stack:
                    return False
                if stack.pop() != '[':
                    return False

            elif char == '}':
                if not stack:
                    return False
                if stack.pop() != '{':
                    return False

        if stack:
            return False

        return True

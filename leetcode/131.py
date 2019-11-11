#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        cache = {}

        def is_loop(string):
            if string in cache:
                return cache[string]

            length = len(string)
            if length == 1:
                cache[string] = True
                return True

            mid = length / 2

            for i in range(mid):
                if string[i] != string[length - 1 - i]:
                    cache[string] = False
                    return False

            cache[string] = True
            return True

        def foo(s):
            if not s:
                return [[]]

            result = []
            for i in range(1, len(s) + 1):
                if is_loop(s[:i]):
                    sub = foo(s[i:])
                    for bar in sub:
                        bar.insert(0, s[:i])
                    result.extend(sub)

            return result

        return foo(s)


if __name__ == '__main__':
    solution = Solution()

    s = "aab"

    result = solution.partition(s)
    print(result)

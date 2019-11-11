#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)

        def cache(function):
            memo = {}

            def wrapper(*args):
                if args in memo:
                    return memo[args]

                rv = function(*args)
                memo[args] = rv
                return rv

            return wrapper

        @cache
        def foo(s):
            result = []
            if s in word_set:
                result.append([s])

            for i in range(len(s)):
                if s[:i + 1] in word_set:
                    sub = foo(s[i + 1:])[:]
                    new = []
                    for bar in sub:
                        new.append([s[:i + 1]] + bar[:])
                    result.extend(new)

            return result

        result = []

        for sub in foo(s):
            result.append(' '.join(sub))

        return result


if __name__ == '__main__':
    print(Solution.wordBreak(None, "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

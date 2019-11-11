#!/usr/bin/env python
# encoding: utf-8

#  给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

#  说明：

#      拆分时可以重复使用字典中的单词。
#      你可以假设字典中没有重复的单词。

#  示例 1：

#  输入: s = "leetcode", wordDict = ["leet", "code"]
#  输出: true
#  解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

#  示例 2：

#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
#  输出: true
#  解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#       注意你可以重复使用字典中的单词。

#  示例 3：

#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#  输出: false


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
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
            if s in word_set:
                return True

            for i in range(len(s)):
                if s[:i + 1] in word_set:
                    ok = foo(s[i + 1:])
                    if ok:
                        return True
            return False

        return foo(s)


if __name__ == '__main__':
    print(Solution.wordBreak(None, "applepenapple", ["apple", "pen"]))

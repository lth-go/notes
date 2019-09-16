#!/usr/bin/env python
# encoding: utf-8

#  给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

#  示例 1：

#  输入：
#    s = "barfoothefoobarman",
#    words = ["foo","bar"]
#  输出：[0,9]
#  解释：
#  从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
#  输出的顺序不重要, [9,0] 也是有效答案。

#  示例 2：

#  输入：
#    s = "wordgoodgoodgoodbestword",
#    words = ["word","good","best","word"]
#  输出：[]


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not words:
            return []

        word_len = len(words[0])
        words_len = len(words)

        sorted_words = sorted(words)

        result = []
        for i in range(word_len):
            split_s = s[i:]

            split_list = []
            for j in range(len(split_s) / word_len):
                split_list.append(split_s[j * word_len: (j + 1) * word_len])

            for split_index in range(len(split_list) - words_len + 1):
                if sorted(split_list[split_index: split_index + words_len]) == sorted_words:
                    result.append(split_index * word_len + i)

        return result

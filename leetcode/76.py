#!/usr/bin/env python
# encoding: utf-8

#  给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

#  示例：

#  输入: S = "ADOBECODEBANC", T = "ABC"
#  输出: "BANC"

#  说明：

#      如果 S 中不存这样的子串，则返回空字符串 ""。
#      如果 S 中存在这样的子串，我们保证它是唯一的答案。


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_len = len(s)
        t_len = len(t)

        count_dict = {}
        current_dict = {}

        for char in t:
            count_dict.setdefault(char, 0)
            count_dict[char] += 1

            current_dict.setdefault(char, 0)

        start = 0
        end = t_len - 1
        for char in s[start: end + 1]:
            if char in count_dict:
                current_dict[char] += 1

        def check(count_dict, current_dict):
            for char in count_dict:
                if current_dict.get(char, 0) < count_dict[char]:
                    return False

            return True

        if check(count_dict, current_dict):
            return s[start: end + 1]

        min_string = ''
        min_len = s_len + 1

        add = True
        while start <= s_len - t_len:
            if end - start + 1 <= t_len:
                add = True

            if end >= s_len - 1:
                add = False

            if add:
                end += 1
                current = s[end]
                if current in count_dict:
                    current_dict[current] += 1

            else:
                current = s[start]
                if current in count_dict:
                    current_dict[current] -= 1
                start += 1
                add = True

            if check(count_dict, current_dict):
                add = False
                current_len = end - start + 1
                if current_len < min_len:
                    min_len = current_len
                    min_string = s[start: end + 1]

        return min_string


if __name__ == "__main__":
    s = Solution()

    result = s.minWindow(
        "of_characters_and_as",
        "aas"
    )
    print(result)

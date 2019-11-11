#!/usr/bin/env python
# encoding: utf-8

#  给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

#  示例:

#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
#  输出:
#  [
#    ["ate","eat","tea"],
#    ["nat","tan"],
#    ["bat"]
#  ]

#  说明：

#      所有输入均为小写字母。
#      不考虑答案输出的顺序。


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}

        for string in strs:
            key = tuple(sorted(string))
            d.setdefault(key, [])
            d[key].append(string)

        return d.values()


if __name__ == '__main__':
    s = Solution()
    strs_list = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
    ]

    for strs in strs_list:
        result = s.groupAnagrams(strs)
        print(result)

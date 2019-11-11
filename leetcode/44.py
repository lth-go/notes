#!/usr/bin/env python
# encoding: utf-8

#  给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

#  '?' 可以匹配任何单个字符。
#  '*' 可以匹配任意字符串（包括空字符串）。

#  两个字符串完全匹配才算匹配成功。

#  说明:

#      s 可能为空，且只包含从 a-z 的小写字母。
#      p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

#  示例 1:

#  输入:
#  s = "aa"
#  p = "a"
#  输出: false
#  解释: "a" 无法匹配 "aa" 整个字符串。

#  示例 2:

#  输入:
#  s = "aa"
#  p = "*"
#  输出: true
#  解释: '*' 可以匹配任意字符串。

#  示例 3:

#  输入:
#  s = "cb"
#  p = "?a"
#  输出: false
#  解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

#  示例 4:

#  输入:
#  s = "adceb"
#  p = "*a*b"
#  输出: true
#  解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

#  示例 5:

#  输入:
#  s = "acdcb"
#  p = "a*c?b"
#  输入: false


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #  if p == '':
        #      return s == ''

        #  if p[0] == '*':
        #      for i in range(len(s), 0, -1):
        #          ok = self.isMatch(s[i:], p)
        #          if ok:
        #              return ok

        #      return self.isMatch(s, p[1:])

        #  else:
        #      if not s:
        #          return False

        #      if p[0] not in ['?', s[0]]:
        #          return False

        #      return self.isMatch(s[1:], p[1:])

        s_len = len(s)
        p_len = len(p)

        l = [[False for _ in range(p_len + 1)] for _ in range(s_len + 1)]
        l[0][0] = True

        for j in range(p_len):
            if p[j] == '*':
                l[0][j + 1] = l[0][j]

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):

                if p[j - 1] in [s[i - 1], '?']:
                    l[i][j] = l[i - 1][j - 1]
                elif p[j - 1] == '*':
                    l[i][j] = l[i][j - 1] or l[i - 1][j]

        return l[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    for s, p in [
        ("aa", "a"),
        ("aa", "*"),
        ("cb", "?a"),
        ("adceb", "*a*b"),
        ("acdcb", "a*c?b"),
        ("aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab", "*babbbb*aab**b*bb*aa*"),
        ("b", "?*?"),
    ]:
        result = solution.isMatch(s, p)
        print(result)

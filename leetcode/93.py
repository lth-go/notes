#!/usr/bin/env python
# encoding: utf-8

#  给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

#  示例:

#  输入: "25525511135"
#  输出: ["255.255.11.135", "255.255.111.35"]


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cheat = {
            4: {(1, 1, 1, 1)},
            5: {(1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (2, 1, 1, 1)},
            6: {(1, 1, 1, 3),
                (1, 1, 2, 2),
                (1, 1, 3, 1),
                (1, 2, 1, 2),
                (1, 2, 2, 1),
                (1, 3, 1, 1),
                (2, 1, 1, 2),
                (2, 1, 2, 1),
                (2, 2, 1, 1),
                (3, 1, 1, 1)},
            7: {(1, 1, 2, 3),
                (1, 1, 3, 2),
                (1, 2, 1, 3),
                (1, 2, 2, 2),
                (1, 2, 3, 1),
                (1, 3, 1, 2),
                (1, 3, 2, 1),
                (2, 1, 1, 3),
                (2, 1, 2, 2),
                (2, 1, 3, 1),
                (2, 2, 1, 2),
                (2, 2, 2, 1),
                (2, 3, 1, 1),
                (3, 1, 1, 2),
                (3, 1, 2, 1),
                (3, 2, 1, 1)},
            8: {(1, 1, 3, 3),
                (1, 2, 2, 3),
                (1, 2, 3, 2),
                (1, 3, 1, 3),
                (1, 3, 2, 2),
                (1, 3, 3, 1),
                (2, 1, 2, 3),
                (2, 1, 3, 2),
                (2, 2, 1, 3),
                (2, 2, 2, 2),
                (2, 2, 3, 1),
                (2, 3, 1, 2),
                (2, 3, 2, 1),
                (3, 1, 1, 3),
                (3, 1, 2, 2),
                (3, 1, 3, 1),
                (3, 2, 1, 2),
                (3, 2, 2, 1),
                (3, 3, 1, 1)},
            9: {(1, 2, 3, 3),
                (1, 3, 2, 3),
                (1, 3, 3, 2),
                (2, 1, 3, 3),
                (2, 2, 2, 3),
                (2, 2, 3, 2),
                (2, 3, 1, 3),
                (2, 3, 2, 2),
                (2, 3, 3, 1),
                (3, 1, 2, 3),
                (3, 1, 3, 2),
                (3, 2, 1, 3),
                (3, 2, 2, 2),
                (3, 2, 3, 1),
                (3, 3, 1, 2),
                (3, 3, 2, 1)},
            10: {(1, 3, 3, 3),
                 (2, 2, 3, 3),
                 (2, 3, 2, 3),
                 (2, 3, 3, 2),
                 (3, 1, 3, 3),
                 (3, 2, 2, 3),
                 (3, 2, 3, 2),
                 (3, 3, 1, 3),
                 (3, 3, 2, 2),
                 (3, 3, 3, 1)},
            11: {(2, 3, 3, 3), (3, 2, 3, 3), (3, 3, 2, 3), (3, 3, 3, 2)},
            12: {(3, 3, 3, 3)}}
        s_len = len(s)

        value = cheat.get(s_len)
        if not value:
            return []

        result = []
        for guess in value:
            foo = []
            ss = s
            for i in guess:
                num = ss[:i]
                ss = ss[i:]
                foo.append(num)

            for num in foo:
                if len(num) > 1 and num[0] == '0':
                    break
                if not (0 <= int(num) <= 255):
                    break
            else:
                result.append('.'.join(foo))

        return result


if __name__ == '__main__':
    s = Solution()

    result = s.restoreIpAddresses("010010")
    print(result)

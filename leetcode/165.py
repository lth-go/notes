#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        version1_list = map(int, version1.split('.'))
        version2_list = map(int, version2.split('.'))

        version1_len = len(version1_list)
        version2_len = len(version2_list)

        if version1_len > version2_len:
            minus = version1_len - version2_len

            while minus > 0:
                version2_list.append(0)
                minus -= 1

        elif version1_len < version2_len:
            minus = version2_len - version1_len
            while minus > 0:
                version1_list.append(0)
                minus -= 1

        for index in range(len(version1_list)):
            one = version1_list[index]
            two = version2_list[index]

            if one > two:
                return 1
            elif one < two:
                return -1

        return 0


if __name__ == '__main__':
    s = Solution()

    version1 = "7.5.2.4"
    version2 = "7.5.3"

    result = s.compareVersion(version1, version2)

    print(result)

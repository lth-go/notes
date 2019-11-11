#!/usr/bin/env python
# encoding: utf-8
#  给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

#  示例:

#  输入: n = 4, k = 2
#  输出:
#  [
#    [2,4],
#    [3,4],
#    [2,3],
#    [1,2],
#    [1,3],
#    [1,4],
#  ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def foo(num_list, k):
            if k == 1:
                return [[num] for num in num_list]

            result = []
            for index, num in enumerate(num_list):
                sub_num_list = num_list[index + 1:]
                sub_foo = foo(sub_num_list, k - 1)

                for bar in sub_foo:
                    result.append([num] + bar)

            return result

        return foo(range(1, n + 1), k)


if __name__ == "__main__":
    s = Solution()

    result = s.combine(
        4, 2
    )
    print(result)

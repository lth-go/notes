#!/usr/bin/env python
# encoding: utf-8

#  给出一个区间的集合，请合并所有重叠的区间。

#  示例 1:

#  输入: [[1,3],[2,6],[8,10],[15,18]]
#  输出: [[1,6],[8,10],[15,18]]
#  解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

#  示例 2:

#  输入: [[1,4],[4,5]]
#  输出: [[1,5]]
#  解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        num_list = []

        for interval in intervals:
            left, right = interval
            sub_num_list = range(left, right + 1)
            num_list.extend(sub_num_list)
            for num in sub_num_list[:-1]:
                num_list.append(num + 0.5)

        num_list = sorted(list(set(num_list)))

        num_len = len(num_list)

        start = 0
        end = 0
        while end < num_len:
            if end == num_len - 1:
                result.append([num_list[start], num_list[end]])
                break

            if num_list[end + 1] - num_list[end] == 0.5:
                end += 1

            else:
                result.append([num_list[start], num_list[end]])
                start = end + 1
                end = start

        return result


if __name__ == '__main__':
    s = Solution()
    intervals_list = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [5, 6]],
        [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]],
    ]

    for intervals in intervals_list:
        result = s.merge(intervals)
        print(result)

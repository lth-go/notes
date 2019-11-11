#!/usr/bin/env python
# encoding: utf-8

#  给出一个无重叠的 ，按照区间起始端点排序的区间列表。

#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

#  示例 1:

#  输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
#  输出: [[1,5],[6,9]]

#  示例 2:

#  输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#  输出: [[1,2],[3,10],[12,16]]
#  解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        if not newInterval:
            return intervals

        insert_start, insert_end = newInterval

        if insert_start < intervals[0][0]:
            if insert_end > intervals[-1][1]:
                return [newInterval]

            else:
                for index, interval in enumerate(intervals):
                    start, end = interval
                    if end < insert_end:
                        continue
                    else:
                        if insert_end >= start:
                            result = [[insert_start, end]] + intervals[index + 1:]
                            if [] in result:
                                result.remove([])
                            return result
                        else:
                            result = [newInterval] + intervals[index:]
                            if [] in result:
                                result.remove([])
                            return result

        elif insert_end > intervals[-1][-1]:
            for index, interval in enumerate(intervals):
                start, end = interval
                if end < insert_start:
                    continue
                else:
                    if insert_start >= start:
                        result = intervals[:index] + [[start, insert_end]]
                        if [] in result:
                            result.remove([])
                        return result
                    else:
                        result = intervals[:index] + [[insert_start, insert_end]]
                        if [] in result:
                            result.remove([])
                        return result

        start_ = None
        end_ = None

        for index, interval in enumerate(intervals):
            start, end = interval

            if start_ is None:
                if insert_start >= start and insert_start <= end:
                    start_ = index

                elif insert_start < start:
                    start_ = index - 0.5

            if end_ is None:
                if insert_end >= start and insert_end <= end:
                    end_ = index

                elif insert_end < start:
                    end_ = index - 0.5

        if start_ is None:
            return intervals + [newInterval]

        left = []
        right = []

        new_start = None
        new_end = None
        if isinstance(start_, float):
            left = intervals[:int(start_ + 0.5)]
            new_start = insert_start
        else:
            left = intervals[:start_]
            new_start = intervals[start_][0]

        if isinstance(end_, float):
            right = intervals[int(end_ + 0.5):]
            new_end = insert_end
        else:
            right = intervals[end_ + 1:]
            new_end = intervals[end_][1]

        return left + [[new_start, new_end]] + right


if __name__ == '__main__':
    s = Solution()

    intervals = [[3, 5], [12, 15]]
    newInterval = [6, 6]
    result = s.insert(intervals, newInterval)
    print(result)

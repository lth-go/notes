#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return range(numCourses)

        foo = {}
        bar = {}
        for o, i in prerequisites:
            foo.setdefault(i, [])
            foo[i].append(o)

            bar[o] = bar.get(o, 0) + 1

        q = []
        for i in range(numCourses):
            if i not in bar:
                q.append(i)

        result = []

        while q:
            i = q.pop()
            result.append(i)
            if i in foo:
                for o in foo[i]:
                    bar[o] -= 1
                    if bar[o] == 0:
                        q.append(o)

        if len(result) < numCourses:
            return []

        return result


if __name__ == '__main__':
    s = Solution()
    #  result = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    result = s.findOrder(3, [[1, 0]])
    print(result)

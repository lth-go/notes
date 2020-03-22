#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        foo = {}
        for o, i in prerequisites:
            foo.setdefault(i, [])
            foo[i].append(o)

        def dfs(count, foo):
            if not foo:
                return True

            o_set = set()
            for o_list in foo.values():
                o_set.update(o_list)

            i_set = set()
            for i in foo.keys():
                if i in o_set:
                    continue

                i_set.add(i)

            if not i_set:
                return False

            if count == 1:
                return True

            for i in i_set:
                del foo[i]

            return dfs(count - 1, foo)

        return dfs(numCourses - 1, foo)


if __name__ == '__main__':
    s = Solution()
    #  result = s.canFinish(2, [[1, 0], [1, 2], [0, 1]])
    result = s.canFinish(3, [[1, 0]])
    print(result)

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        result.add(tuple())

        for num in nums:
            new = set()

            one = (num,)
            new.add(one)

            for sub in result:
                new.add(tuple(sorted(sub + one)))

            result.update(new)

        bar = []
        for t in result:
            bar.append(list(t))

        return bar


if __name__ == '__main__':
    s = Solution()
    result = s.subsetsWithDup([1, 2, 2])
    print(result)

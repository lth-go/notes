#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = self.solve(candidates, target)
        return list(result)

    def solve(self, candidates, target):
        result = set()

        for num in candidates:
            sub = target - num

            if sub < 0:
                continue

            if sub == 0:
                result.add((num,))

            else:
                if sub < candidates[0]:
                    continue

                sub_result = self.solve(candidates, sub)

                for r in sub_result:
                    result.add(tuple(sorted(r + (num,))))

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.combinationSum([2, 3, 5], 8)
    print(result)

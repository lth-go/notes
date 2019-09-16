#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def combinationSum2(self, candidates, target):
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

                new_candidates = candidates[:]
                new_candidates.remove(num)
                sub_result = self.solve(new_candidates, sub)

                for r in sub_result:
                    result.add(tuple(sorted(r + (num,))))

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(result)

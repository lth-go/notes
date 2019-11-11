#!/usr/bin/env python
# encoding: utf-8

import functools


class Solution:
    @functools.lru_cache(None)
    def minCut(self, s):
        if s == s[::-1]:
            return 0
        ans = float("inf")
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(self.minCut(s[i:]) + 1, ans)
        return ans


if __name__ == '__main__':
    solution = Solution()

    s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"

    result = solution.minCut(s)
    print(result)

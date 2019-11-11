#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        stack = []
        max_area = 0

        heights = [0] + heights + [0]
        heights_len = len(heights)

        for index in range(heights_len):
            height = heights[index]

            while stack and height < heights[stack[-1]]:
                h = stack.pop()
                max_area = max(heights[h] * (index - stack[-1] - 1), max_area)

            stack.append(index)

        return max_area


if __name__ == "__main__":
    s = Solution()
    result = s.largestRectangleArea([0, 2, 1, 2, 0])
    print(result)

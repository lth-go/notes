#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        index1 = 0
        index2 = len(height) - 1

        while index1 != index2:
            h1 = height[index1]
            h2 = height[index2]

            area = (index2 - index1) * min(h1, h2)

            if area > max_area:
                max_area = area

            if h1 < h2:
                index1 += 1
            else:
                index2 -= 1

        return max_area

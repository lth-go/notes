#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        sub_area = sum(height)
        height_len = len(height)

        if height_len <= 2:
            return 0

        split_list = []

        index1 = 0
        index2 = 1
        max_index = None

        while True:
            num1 = height[index1]
            num2 = height[index2]

            if max_index is None or num2 > height[max_index]:
                max_index = index2

            if num2 >= num1:
                if not split_list:
                    split_list.append(index1)
                split_list.append(index2)
                index1 = index2
                index2 = index1 + 1

                max_index = None
            else:
                index2 += 1

            if index2 >= height_len:
                if max_index:
                    if not split_list:
                        split_list.append(index1)

                    split_list.append(max_index)
                    index1 = max_index
                    index2 = index1 + 1
                    max_index = None
                else:
                    index1 += 1
                    index2 = index1 + 1

            if index1 >= height_len - 1:
                break

        total_area = 0

        for i in split_list:
            total_area += height[i]

        if split_list[-1] != (height_len - 1):
            total_area += height[-1]

        for i in range(len(split_list) - 1):
            one = split_list[i]
            two = split_list[i + 1]

            num1 = height[one]
            num2 = height[two]

            area = (two - one - 1) * min(num1, num2)
            total_area += area

        return total_area - sub_area


if __name__ == '__main__':
    s = Solution()
    height_list = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [2, 0, 2],
        [5, 4, 1, 2],
    ]

    for height in height_list:
        result = s.trap(height)
        print(result)

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        nums_len = len(nums)

        zero_index = 0
        two_index = nums_len - 1
        index = 0

        while index <= two_index:
            num = nums[index]

            if num == 0:
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                zero_index += 1
                index += 1
            elif num == 2:
                nums[index], nums[two_index] = nums[two_index], nums[index]
                two_index -= 1
            else:
                index += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    result = s.sortColors([0, 0, 2, 1, 1, 2])
    print(result)

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length < 2:
            return 0

        the_min = float('inf')
        the_max = float('-inf')

        for num in nums:
            the_min = min(the_min, num)
            the_max = max(the_max, num)

        bucket_size = max(1, (the_max - the_min) / (length - 1))
        bucket_count = (the_max - the_min) / bucket_size + 1
        bucket = [{'use': False, 'min': float('inf'), 'max': float('-inf')} for _ in range(bucket_count)]

        for num in nums:
            bucket_id = (num - the_min) / bucket_size

            bucket[bucket_id]['min'] = min(bucket[bucket_id]['min'], num)
            bucket[bucket_id]['max'] = max(bucket[bucket_id]['max'], num)
            bucket[bucket_id]['use'] = True

        result = 0
        pre = the_min

        for b in bucket:
            if not b['use']:
                continue

            result = max(result, b['min'] - pre)
            pre = b['max']

        return result


if __name__ == '__main__':
    s = Solution()

    #  nums = [3, 6, 9, 1]
    nums = [1, 1, 1, 1]

    result = s.maximumGap(nums)

    print(result)

#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial_list = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        num_list = [str(i) for i in range(1, n + 1)]

        result = ''

        while True:
            if n == 1:
                result += ''.join(num_list)
                break

            if k == 0:
                result += ''.join(reversed(num_list))
                break

            div, mod = divmod(k, factorial_list[n - 1])

            if mod == 0:
                div -= 1

            num = num_list.pop(div)
            result += num

            n -= 1
            k = mod

        return result


if __name__ == '__main__':
    s = Solution()

    n_k_list = [
        (3, 3),
        (4, 9),
        (1, 1),
        (3, 2)
    ]

    for n, k in n_k_list:
        result = s.getPermutation(n, k)
        print(result)

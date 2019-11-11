#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        count_dict = {}
        for point in points:
            t = tuple(point)
            count_dict.setdefault(t, 0)
            count_dict[t] += 1

        func_dict = {}

        def xx(num1, num2):
            if num1 == 0:
                return (0, 1)

            m = max(num1, num2)
            n = min(num1, num2)

            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n
            return num1 / n, num2 / n

        def foo(a, b):
            if a == b:
                return None

            if a[0] == b[0]:
                return (a[0], None)

            k = xx(b[1] - a[1], b[0] - a[0])
            n = a[1] - a[0] * (k[0] / k[1])

            return (k, n)

        for index, point in enumerate(points):
            x1, y1 = point

            for x2, y2 in points[index + 1:]:
                bar = foo((x1, y1), (x2, y2))
                if bar:
                    func_dict.setdefault(bar, set())
                    func_dict[bar].add((x1, y1))
                    func_dict[bar].add((x2, y2))
        print(func_dict)

        if not func_dict.values():
            return max(count_dict.values())

        result = 0

        for todo in func_dict.values():
            r = 0
            for t in todo:
                r += count_dict[t]

            result = max(r, result)

        return result


if __name__ == '__main__':
    s = Solution()

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    #  points = [[0, 0], [0, 0]]
    #  points = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
    points = [[2, 3], [3, 3], [-5, 3]]

    result = s.maxPoints(points)
    print(result)

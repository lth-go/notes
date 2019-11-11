#!/usr/bin/env python
# encoding: utf-8

#  老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

#  你需要按照以下要求，帮助老师给这些孩子分发糖果：

#      每个孩子至少分配到 1 个糖果。
#      相邻的孩子中，评分高的孩子必须获得更多的糖果。

#  那么这样下来，老师至少需要准备多少颗糖果呢？

#  示例 1:

#  输入: [1,0,2]
#  输出: 5
#  解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

#  示例 2:

#  输入: [1,2,2]
#  输出: 4
#  解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#       第三个孩子只得到 1 颗糖果，这已满足上述两个条件。


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        def foo(ratings):

            cache = {}

            total = 0

            point = 0
            up = True

            minus = 0

            for index, current in enumerate(ratings):
                if index == len(ratings) - 1:
                    if up:
                        total += sum(range(1, index - point + 2))
                    else:
                        total += sum(range(1, index - point + 1))
                        cache[point] = max(cache.get(point, 0), index - point + 1)
                    continue

                right = ratings[index + 1]

                if up:
                    if right < current:
                        up = False
                        total += sum(range(1, index - point + 1))
                        cache[index] = index - point + 1
                        point = index
                    else:
                        continue
                else:
                    if right > current:
                        up = True
                        total += sum(range(1, index - point + 1))
                        cache[point] = max(cache.get(point, 0), index - point + 1)
                        point = index
                        minus += 1
                    else:
                        continue

            total += sum(cache.values())
            total -= minus

            return total

        start = 0
        total = 0
        for index, current in enumerate(ratings):
            if index == len(ratings) - 1:
                total += foo(ratings[start: index + 1])

            else:
                right = ratings[index + 1]

                if current == right:
                    total += foo(ratings[start: index + 1])
                    start = index + 1

        return total


if __name__ == '__main__':
    solution = Solution()
    #  ratings = [1, 2, 2]
    #  ratings = [1, 0, 2]
    #  ratings = [1, 3, 2, 2, 1]
    ratings = [1, 2, 87, 87, 87, 2, 1]
    print(solution.candy(ratings))

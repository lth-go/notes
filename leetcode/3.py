class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def index_of(array, value):
            for i, v in enumerate(array):
                if v == value:
                    return i
            return -1

        current = ''
        max_str = ''

        for i in s:
            index = index_of(current, i)
            if index < 0:
                current += i
                if len(current) > len(max_str):
                    max_str = current
            else:
                current = current[index + 1:]
                current += i

        return len(max_str)

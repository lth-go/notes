#!/usr/bin/env python
# encoding: utf-8

#  给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。

#  说明:

#      单词是指由非空格字符组成的字符序列。
#      每个单词的长度大于 0，小于等于 maxWidth。
#      输入单词数组 words 至少包含一个单词。

#  示例:

#  输入:
#  words = ["This", "is", "an", "example", "of", "text", "justification."]
#  maxWidth = 16
#  输出:
#  [
#     "This    is    an",
#     "example  of text",
#     "justification.  "
#  ]

#  示例 2:

#  输入:
#  words = ["What","must","be","acknowledgment","shall","be"]
#  maxWidth = 16
#  输出:
#  [
#    "What   must   be",
#    "acknowledgment  ",
#    "shall be        "
#  ]
#  解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#       因为最后一行应为左对齐，而不是左右两端对齐。
#       第二行同样为左对齐，这是因为这行只包含一个单词。

#  示例 3:

#  输入:
#  words = ["Science","is","what","we","understand","well","enough","to","explain",
#           "to","a","computer.","Art","is","everything","else","we","do"]
#  maxWidth = 20
#  输出:
#  [
#    "Science  is  what we",
#    "understand      well",
#    "enough to explain to",
#    "a  computer.  Art is",
#    "everything  else  we",
#    "do                  "
#  ]


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line_list = []
        current_len = 0
        current_index = 0
        for index, word in enumerate(words):
            word_len = len(word)
            add_len = word_len + current_len + 1
            if add_len > maxWidth + 1:
                line_list.append((current_index, index - 1))
                current_index = index
                current_len = word_len + 1
            else:
                current_len = add_len

        else:
            line_list.append((current_index, index))

        new_words = []
        for line in line_list:
            new_words.append(words[line[0]: line[1] + 1])

        result = []

        new_words_len = len(new_words)

        for word_list_index, word_list in enumerate(new_words):
            if word_list_index == new_words_len - 1:
                result.append(' '.join(word_list).ljust(maxWidth, ' '))
                continue

            total = 0
            for word in word_list:
                total += len(word)
            word_len = len(word_list)

            if word_len == 1:
                result.append(word_list[0].ljust(maxWidth, ' '))
                continue

            space_count = word_len - 1
            reset = maxWidth - total
            space_list = ['' for _ in range(space_count)]
            index = 0

            while reset:
                space_list[index] = space_list[index] + ' '
                index += 1
                if index == space_count:
                    index = 0

                reset -= 1

            new_word_list = []
            for i in range(space_count):
                new_word_list.append(word_list[i])
                new_word_list.append(space_list[i])

            new_word_list.append(word_list[-1])
            result.append(''.join(new_word_list))

        return result


if __name__ == '__main__':
    s = Solution()
    input_list = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What", "must", "be", "acknowledgment", "shall", "be"], 16),
        (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
    ]

    for input_ in input_list:
        result = s.fullJustify(*input_)
        print(result)

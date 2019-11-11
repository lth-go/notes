#!/usr/bin/env python
# encoding: utf-8
#  验证给定的字符串是否可以解释为十进制数字。

#  例如:

#  "0" => true
#  " 0.1 " => true
#  "abc" => false
#  "1 a" => false
#  "2e10" => true
#  " -90e3   " => true
#  " 1e" => false
#  "e3" => false
#  " 6e-1" => true
#  " 99e2.5 " => false
#  "53.5e93" => true
#  " --6 " => false
#  "-+3" => false
#  "95a54e53" => false

#  说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

#      数字 0-9
#      指数 - "e"
#      正/负号 - "+"/"-"
#      小数点 - "."

#  当然，在输入中，这些字符的上下文也很重要。


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = {
        }

if __name__ == "__main__":
    s = Solution()

    s_list = [
        "0",
        " 0.1 ",
        "abc",
        "1 a",
        "2e10",
        " -90e3   ",
        " 1e",
        "e3",
        " 6e-1",
        " 99e2.5 ",
        "53.5e93",
        " --6 ",
        "-+3",
        "95a54e53",
    ]
    for s_ in s_list:
        result = s.isNumber(s_)
        print(result)
    #  test(1, "123", true)
    #  test(2, " 123 ", true)
    #  test(3, "0", true)
    #  test(4, "0123", true)
    #  //Cannot agree test(5, "00", true)
    #  //Cannot agree test(6, "-10", true)
    #  test(7, "-0", true)
    #  test(8, "123.5", true)
    #  test(9, "123.000000", true)
    #  test(10, "-500.777", true)
    #  test(11, "0.0000001", true)
    #  test(12, "0.00000", true)
    #  test(13, "0.", true)
    #  //Cannot be more disagree!!! test(14, "00.5", true)
    #  //Strongly cannot agree test(15, "123e1", true)
    #  test(16, "1.23e10", true)
    #  test(17, "0.5e-10", true)
    #  test(18, "1.0e4.5", false)
    #  test(19, "0.5e04", true)
    #  test(20, "12 3", false)
    #  test(21, "1a3", false)
    #  test(22, "", false)
    #  test(23, "     ", false)
    #  test(24, null, false)
    #  test(25, ".1", true)
    #  //Ok, if you say so test(26, ".", false)
    #  test(27, "2e0", true)
    #  //Really?! test(28, "+.8", true)
    #  test(29, " 005047e+6", true)
    #  //Damn = = | ||

# 题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
#       例如，字符串“+100”、“5e2”、“-123”、“3.1416”及“-1E-16”都表示数值。但“12e”、“1a3.14”、“1.2.3”、 “+-5”及“12e+5.4”都不是。


class Solution(object):
    def isNumeric(self, s):
        if s is None:
            return False

        # 先判断是否为有符号整数
        flag, s = self.isInterger(s)

        # 判断是否是小数(小数点前面没有数字的小数）

        if s is not None and s[0] == '.':
            if len(s) > 1:
                s = s[1:]
            else:
                s = None
            flag1, s = self.isUnsignedInterger(s)
            flag = flag or flag1

        # 判断指数
        if s is not None and (s[0] == 'e' or s[0] == 'E'):
            if len(s) > 1:
                s = s[1:]
            else:
                s = None
            flag2, s = self.isInterger(s)
            flag = flag and flag2

        return flag and s is None

    def isUnsignedInterger(self, s):
        flag = False
        while s is not None and '0' <= s[0] <= '9':
            if len(s) > 1:
                s = s[1:]
            else:
                s = None
            flag = True
        return flag, s

    def isInterger(self, s):
        if s is not None and (s[0] == '+' or s[0] == '-'):
            if len(s) > 1:
                s = s[1:]
            else:
                s = None
        return self.isUnsignedInterger(s)


print(Solution().isNumeric("12."))
print(Solution().isNumeric("12.e"))
print(Solution().isNumeric("12.1e-10"))
# 题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
#       数值为0或者字符串不是一个合法的数值则返回0


class Solution(object):
    def StrToInt(self, s):
        if len(s) == 0:
            return 0

        dic = {str(i): i for i in range(10)}

        if s[0] != '+' and s[0] != '-' and s[0] not in dic:
            return 0

        for val in s[1:]:
            if val not in dic:
                return 0

        if s[0] == '+':
            sign = 1
            res = sign * self.str_to_int(s[1:])

        elif s[0] == '-':
            sign = -1
            res = sign * self.str_to_int(s[1:])

        else:
            sign = 1
            res = sign * self.str_to_int(s)

        if res < -2 ** 31:
            return 0
        if res > 2 ** 31 - 1:
            return 0

        return res

    def str_to_int(self, s):
        res = 0
        for val in s:
            res = res * 10 + int(val)
        return res


test = '-2147483649'
s = Solution()
print(s.StrToInt(test))

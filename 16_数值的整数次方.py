# 题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#      保证base和exponent不同时为0


class Solution(object):
    def power(self, base, exponent):
        flag = 0
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1

        result = 1

        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result


s = Solution()
print(s.power(2, -3))


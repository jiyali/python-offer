# 题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#      保证base和exponent不同时为0
# 普通做法：

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


# 高效的做法，可以使用递归，同时用右移来代替/2
class Solution1(object):
    def power(self, base, exponent):

        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1 / base

        result = self.power(base, exponent >> 1)  # 求余运算
        result *= result
        if (exponent & 0x1) == 1:  # 判断奇数还是偶数
            result *= base
        return result


s1 = Solution1()
print(s1.power(2, -3))

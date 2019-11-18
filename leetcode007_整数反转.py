# 题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


# 直接反转
class Solution(object):
    def reverse(self, x):
        num = int(str(abs(x))[::-1])
        if -2 ** 31 <= num <= 2 **31 - 1:
            if x < 0:
                return -num
            else:
                return num
        else:
            return 0

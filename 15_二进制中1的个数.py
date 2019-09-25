# 题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 思路：补码的表示方法是：正数的补码是本身，负数的补码在其原码的基础上a符号位不变，其余各位取反（求反码）最后加一


class Solution(object):
    def NumberOf1(self, n):

        count = 0

        if n < 0:
            n = n & 0xffffffff  # 把整数转成补码形式
        while n:
            count += 1
            n = (n - 1) & n  # 用于消去最后一位的1
        return count


S = Solution()
print(S.NumberOf1(-1))

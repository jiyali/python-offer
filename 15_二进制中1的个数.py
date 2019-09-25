# 题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 思路：补码的表示方法是：正数的补码是本身，负数的补码在其原码的基础上a符号位不变，其余各位取反（求反码）最后加一
#       把一个整数减去1，再和原来整数做与运算，会把该整数最右边的1变成0，那么一个整数有多少个1，就能做多少次这种运算


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


# 思路二：将输入的整数用二进制表示出来，数1的个数即可

class Solution1(object):

    def NumberOf2(self, n):

        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')


s1 = Solution1()
print(s1.NumberOf2(-1))

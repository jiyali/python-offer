# 题目：数字以0123456789101112131415…的格式序列化到一个字符序列中。
#      在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。 请写一个函数，求任意第n位对应的数字。


# （不推荐）常规解法，从0开始枚举数字，并把该数字长度加进来，那么第n位对应的数字就在这个数的某一位。
class Solution(object):
    def findNthDigit(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        i = 0
        total_len = 0
        while total_len < n:
            i += 1
            total_len += len(str(i))
        return int(str(i)[-1 - (total_len - n)])


# 数字规律： 1~9有9个数，10~99有2*10*9个数，100~999有3*100*9个数，1000-9999有4*1000*9个数字
class Solution1(object):
    def findNthDigit(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0

        i = 0
        total_len = 0

        # 确定结果所在的数字位数
        while total_len < n:
            i += 1
            total_len += i * (9 * 10 ** (i-1))

        # 确定n所在的是第i位的第几个位置
        state = n - total_len + i * (9 * 10 ** (i-1))

        k_num = (state - 1) / i  # 属于i位数的哪个数
        k_end = (state - 1) % i  # 属于i位数的第几位

        num = 10 ** (i - 1) + k_num

        return int(str(num)[k_end])


s = Solution()
print(s.findNthDigit(0))
print(s.findNthDigit(5))
print(s.findNthDigit(10))
print(s.findNthDigit(13))
print(s.findNthDigit(19))

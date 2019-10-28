# 题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷ 四则运算符号。


# 思路：举个例子比如说5+17，如果不能使用加减乘除运算符，那就只能使用位运算。
#  5:00101
#  17:10001
#  如果不考虑进位的话，两数相加为10100，与位运算的异或相同
#        考虑进位：进位是与<<1
#        python没有无符号右移操作，所以需要越界检查一波
class Solution(object):
    def Add(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 <= 0x7fffffff else ~(num1 ^ 0xffffffff)


class Solution1(object):
    def Add(self, num1, num2):
        list = [num1, num2]
        return sum(list)


s = Solution1()
print(s.Add(5, -17))

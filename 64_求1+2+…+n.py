# 题目：求 1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case 等关键字及条件判断语句（A?B:C）。


# 思路：等差求和
class Solution(object):
    def Sum_Solution(self, n):
        return (n**2 + n) >> 1


class Solution1(object):
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        self.getsum(n)
        return self.sum

    def getsum(self, n):
        self.sum += n
        n -= 1
        return n > 0 and self.getsum(n)


s = Solution1()
print(s.Sum_Solution(5))

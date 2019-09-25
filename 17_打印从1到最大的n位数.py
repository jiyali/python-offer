# 题目：输入数字n，按顺序打印出从1到最大的n位十进制数。


class Solution(object):
    def print1ToMax(self, n):
        if n <= 0:
            return
        number = ['0'] * n
        while not self.Increment(number):
            self.PrintNumber(number)

    def Increment(self, number):
        isOverflow = False
        nLength = len(number)

        for i in range(nLength - 1, -1, -1):



    def PrintNumber(self,number):



s = Solution()
s.print1ToMax(3)

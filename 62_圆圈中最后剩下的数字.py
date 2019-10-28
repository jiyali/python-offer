# 题目：0,1,...,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
#      求出这个圆圈里剩下的最后一个数字。
#      约瑟夫环问题


# 模拟环形链表
class Solution(object):
    def LastRemaining_Solution(self, n, m):
        if n <= 0 or m <= 0:
            return -1

        idList = [i for i in range(n)]  # 编号

        j = 0
        while len(idList) > 1:
            for i in range(m):
                j += 1
                if j == len(idList):
                    j = 0
            if j > 0:
                j -= 1  # 因为当报到第m个数时，j继续自加了一次
                idList.pop(j)
            elif j == 0:
                idList.pop()  # 最后一个

        return idList[0]


# 约瑟夫环问题的通解公式是
# f[1] = 0
# f[i] = (f[i-1] + m) % i (i>1)

class Solutuon1(object):
    def LastRemaining_Solution(self, n, m):
        if n <= 0 or m <= 0:
            return -1

        last = 0
        for i in range(1, n + 1):
            last = (last + m) % i
        return last

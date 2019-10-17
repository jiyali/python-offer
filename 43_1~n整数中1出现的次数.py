# 题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
#       为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
#      ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
#      输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数


# (不推荐)效率很低，对每一位都对10求余，求出1的个数累加，时间复杂度O(nlogn)
class Solution(object):
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0

        for i in range(n + 1):
            number = 0
            while i:
                if i % 10 == 1:
                    number += 1
                i = i / 10
            count += number

        return count


# 思路二：找规律，
#     如果十位上的数是0，比如101，则十位上可能出现1的情况为10~19.
#                       最后结果为 高位数*位数  这个规律可以用n//(i*10)*i公式来表示。
#     如果十位上的数是1，那么最后1的数量要加上x+1，其中x是个位上的数值。比如说112，十位上数字是1，则最后1的数量加上3，即满足条件的有10、11、12三个数，
#                       最后结果为 高位数*位数+低位数+1
#     如果十位上的数大于1，那么十位上为1的所有的数都是符合要求的，这时候最后1的数量要加10，比如120，除了满足110的条件之外，还有11~19共十个数也满足条件。
#                       最后结果为 高位数*位数+位数
class Solution1(object):
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        s = str(n)
        length = len(s)
        for idx, i in enumerate(s):
            place = length - idx  # 当前位数（个位是1，十位是2……）
            pre = n // (10 ** place)  # 当前位数的高位数字
            aft = n % (10 ** (place - 1))  # 当前位数的低位数字
            if i == '0':
                count += pre * 10 ** (place - 1)
            elif i == '1':
                count += pre * 10 ** (place - 1) + aft + 1
            else:
                count += pre * 10 ** (place - 1) + 10 ** (place - 1)
        return count


# 上述思想简化之后：
class Solution2(object):
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        i = 1  # 计算第i位，i=1时为个位

        while i <= n:
            count += n // (i * 10) * i + min(max(n % (i * 10) - i + 1, 0), i)
            i *= 10
        return count


s = Solution2()
print(s.NumberOf1Between1AndN_Solution(10))

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


class Solution1(object):
    def NumberOf1Between1AndN_Solution(self, n):
        if n <= 0:
            return 0
        s = str(n)
        res = 0
        for i in range(len(s)):
            leftbit = s[:i]
            curbit = s[i]
            rightbit = s[i+1:]
            leftnum = int(leftbit) if len(leftbit) != 0 else 0
            rightnum = int(rightbit) if len(rightbit) != 0 else 0
            curnum = int(curbit)
            if curnum == 1:
                res += leftnum * (10 ** len(rightbit)) + rightnum+1
            elif curnum == 0:
                res += leftnum * (10 ** len(rightbit))
            else:
                res += (leftnum+1) * (10 ** len(rightbit))
        return res


# 思路二：找规律，
#        高位上1的个数：每10个数，个位上的1就会出现一次。每100个数，十位上的1就会出现一次。这个规律可以用n//(i*10)*i公式来表示。
#        低位上1的个数：如果十位上的数是1，那么最后1的数量要加上x+1，其中x是个位上的数值。
#                      如果十位上的数大于1，那么十位上为1的所有的数都是符合要求的，这时候最后1的数量要加10。

class Solution2(object):
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        i = 1  # 计算第i位，i=1时为个位

        while i <= n:
            count += n // (i * 10) * i + min(max(n % (i * 10) - i + 1, 0), i)
            i *= 10
        return count


s = Solution1()
print(s.NumberOf1Between1AndN_Solution(10))
print(1//10)

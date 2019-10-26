# 题目：输入一个正数s，打印所有和为s的连续正数序列(至少含有两个数)。
#      例如，输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以打印出3个连续序列1~5、4~6和7~8


class Solution(object):
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []

        small = 1
        big = 2
        middle = (tsum + 1) // 2

        curSum = small + big

        output = []

        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output


s = Solution()
print(s.FindContinuousSequence(15))

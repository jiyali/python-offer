# 题目：从扑克牌中随机抽五张牌，判断是不是一个顺子，即这五张牌是不是连续的。
#      2~10为数字本身，A为1，J为11，Q为12，K为13，而大小王可以看成任意数字。


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return False

        transDic = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in transDic:
                numbers[i] = transDic[numbers[i]]

        numbers = sorted(numbers)
        numberOfzero = 0
        numberOfGap = 0

        i = 0
        while i < len(numbers) and numbers[i] == 0:
            numberOfzero += 1
            i += 1

        small = numberOfzero
        big = numberOfzero + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False

            numberOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numberOfzero < numberOfGap else True


s = Solution()
test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
print(s.IsContinuous(test))






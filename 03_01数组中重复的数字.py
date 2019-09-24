# 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
#       数组中某些数字是重复的，但不知道有几个数字是重复的。
#       也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
#       例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
# 思路：从下标0开始，对每个元素，若numbers[i]不等于i，则交换numbers[i]和numbers[numbers[i]]，
#      直至i和numbers[i]相等继续循环，或numbers[i]和numbers[numbers[i]]相等即遇到重复元素返回True
# 时间复杂度O(n），空间复杂度O(n)


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers):
                return False
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = (numbers[i])
                    return True
                else:
                    tmp = numbers[numbers[i]]
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = tmp
        return False


# -*- coding:utf-8 -*-
class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic = {}
        flag = False
        for num in numbers:
            dic[num] = dic.get(num, 0) + 1
        for num in numbers:
            if dic[num] > 1:
                duplication[0] = num
                flag = True
                break
        return flag


s = Solution2()
s1 = Solution()
test = [2, 3, 1, 0, 2, 5, 3]
dupulication = [0]
print(s.duplicate(test, dupulication))
print(s1.duplicate(test, dupulication))

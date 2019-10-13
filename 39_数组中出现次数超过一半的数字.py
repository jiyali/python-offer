# 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
#       由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 思路一：排序数组，比较中间数的个数是否大于数组长度的一半，时间复杂度为O(nlogn)


class Solution(object):
    def MoreThanHalfNum_Solution(self, numbers):
        numbers.sort()

        tmp = numbers[len(numbers)//2]

        if numbers.count(tmp) > len(numbers)/2:
            return tmp
        else:
            return 0

# 思路二:根据数组特点。时间复杂度O(n)


class Solution1(object):
    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) == 0:
            return 0

        value = 0
        flag = 0
        for i in numbers:
            if flag == 0:
                value = i
                flag = 1
            elif i == value:
                flag += 1
            else:
                flag -= 1
        if flag > 0 and self.check_more_than_half(numbers, value):
            return value
        else:
            return 0

    def check_more_than_half(self, numbers, value):
        times = 0

        for i in numbers:
            if i == value:
                times += 1
        if times > len(numbers)/2:
            return times
        else:
            return False


S = Solution1()
print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum_Solution([1, 2]))

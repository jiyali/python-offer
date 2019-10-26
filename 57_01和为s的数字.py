# 题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
#      如果有多对数字的和等于S，输出任意一对即可。


class Solution(object):
    def FindNumbersWithSum(self, array, tsum):
        if array is None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []

        left = 0
        right = len(array) - 1

        while left < right:
            sum = array[left] + array[right]

            if sum < tsum:
                left += 1
            elif sum > tsum:
                right -= 1
            else:
                return [array[left], array[right]]
        return []


test = [1, 2, 4, 7, 11, 15]
s = Solution()
print(s.FindNumbersWithSum(test, 15))

# 题目：统计一个数字在排序数组中出现的次数。
#       例如，输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4.


# 常规思路：二分法查找大于等于k的第一个数字的下标和大于等于k+1的第一个数字的下标，相减
class Solution(object):
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0

        return self.GetFistK(data, k+1) - self.GetFistK(data, k)

    def GetFistK(self, data, k):
        if data[0] == k:
            return 0

        left = 0
        right = len(data)-1

        while left < right:
            mid = left + (right - left) // 2
            if data[mid] >= k:
                right = mid
            else:
                left = mid + 1

        # 因为 k 有可能不存在，所以不一定符合要求，所以一定要单独判断一下
        if data[left] != k:
            if data[len(data) - 1] < k:
                return len(data)
            elif data[0] > k:
                return 0

        return left


alist = [1, 2, 3, 3, 3, 3, 4, 5]
s = Solution()
print(s.GetFistK(alist, 3))

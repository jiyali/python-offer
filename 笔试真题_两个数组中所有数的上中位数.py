# 给定两个有序数组arr1和arr2，两个数组长度都为N(N>0)，求两个数组中所有数的上中位数，要求：时间复杂度为O(logN)
# 比如：a1 = {1, 2, 3, 4}; a2 = {5, 6, 7, 8}。返回值为4
# 输入描述：输入包括3行，第一行为数组长度N，第二行和第三行分别为一个长度为N的数组
# 输出描述：输出结果为一个整数


class Solution(object):
    def getMidnum(self, a, b):
        if a is None or b is None or len(a) != len(b):
            return None
        start1, end1 = 0, len(a) - 1
        start2, end2 = 0, len(a) - 1
        while start1 < start2:
            mid1 = (start1 + end1) // 2
            mid2 = (start2 + end2) // 2
            offset = (end1 - start1 + 1) & 1 ^ 1
            if a[mid1] == b[mid2]:
                return a[mid1]
            elif a[mid1] > b[mid2]:
                start2 = mid2 + offset
            else:
                start1 = mid1 + offset
                end2 = mid2
        return min(a[end1], b[end2])


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = Solution()
print(s.getMidnum(a, b))

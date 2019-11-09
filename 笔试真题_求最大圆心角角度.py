# 一个圆上有N个点(用圆心正上方的点，顺时针旋转到该点的角度来表达，N可能很大)，求其中任意2点与圆心缩成圆心角的最大值。
# 输入为N个N个[0, 360)的有序float值，输出精确到小数点后一位
# 输入描述：输入为N个N个[0, 360)的有序float值
# 输出描述：输出最大圆心角的角度

class Solution(object):
    import sys
    def find_key(self, arr, l, r):
        mid = l + (r - l) // 2
        if arr[mid] == 180.0:
            return mid
        if mid < len(arr) - 1 and arr[mid] < 180 and arr[mid + 1] > 180:
            return mid + 1
        if mid != len(arr) - 1 and arr[mid] < 180:
            return self.find_key(arr, mid + 1, r)
        if mid != 0 and arr[mid] > 180:
            return self.find_key(arr, l, mid - 1)
        return mid

    def max_angle(self, arr, n):
        key = self.find_key(arr, 0, n - 1)
        if key == 0 or key == n - 1:
            return arr[n - 1] - arr[0]
        res = 0.0
        if 180 >= arr[key] - arr[0] > res:
            res = arr[key] - arr[0]
        elif arr[key - 1] - arr[0] > res:
            res = arr[key - 1] - arr[0]
        if 180 >= arr[n - 1] - arr[key - 1] > res:
            res = arr[n - 1] - arr[key - 1]
        elif arr[n - 1] - arr[key] > res:
            res = arr[n - 1] - arr[key]
        return res

s = Solution()

line = raw_input().split()
n = int(line[0])
arr1 = [float(i) for i in line[1:]]
print(max_angle(arr1, n))
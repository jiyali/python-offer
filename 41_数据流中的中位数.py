# 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
#      如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
#      我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。


# 思路一，将数据流中的数据存入数组中，查找时先排序，然后直接判断中位数，插入时间复杂度为O(1)，输出时间复杂度为O(n)
class Solution(object):
    def __init__(self):
        self.data = []

    def Insert(self, num):
        self.data.append(num)

    def GetMedian(self, data):
        self.data.sort()
        length = len(self.data)
        if length == 0:
            return None
        elif length == 1:
            return self.data[0]
        if length % 2 == 0:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0
        else:
            return self.data[int(length // 2)]


# 思路二：将数据流中的数据存入数组中，按照Partition的思想排序
class Solution1(object):
    def __init__(self):
        self.arr = []

    def Insert(self, num):
        self.arr.append(num)

    def GetMedian(self):  # 牛客上需要加一个变量 def GetMedian(self,arr)这样，我也不知道为啥
        length = len(self.arr)
        if length == 0:
            return []
        if length == 1:
            return self.arr[0]
        if length % 2 == 0:
            return (self.find_kth(self.arr, 0, length - 1, (length - 1) // 2) + \
                    self.find_kth(self.arr, 0, length - 1, length // 2)) / 2.0
        if length % 2 == 1:
            return self.find_kth(self.arr, 0, length - 1, length // 2)

    def find_kth(self, num, left, right, k):
        index = self.Partition(num, left, right)
        if index == k:
            return num[index]
        if index < k:
            return self.find_kth(num, index + 1, right, k)
        if index > k:
            return self.find_kth(num, left, index - 1, k)

    def Partition(self, numbers, left, right):

        pivot = numbers[left]

        while left < right:
            while left < right and numbers[right] >= pivot:
                right -= 1
            numbers[left], numbers[right] = numbers[right], numbers[left]
            while left < right and numbers[left] <= pivot:
                left += 1
            numbers[left], numbers[right] = numbers[right], numbers[left]

        return left


s = Solution1()
s.Insert(5)
print(s.GetMedian())
s.Insert(2)
print(s.GetMedian())
s.Insert(3)
print(s.GetMedian())
s.Insert(4)
print(s.GetMedian())
s.Insert(1)
print(s.GetMedian())
s.Insert(6)
print(s.GetMedian())
s.Insert(7)
print(s.GetMedian())

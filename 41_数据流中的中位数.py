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


# 思路二：将数据流中的数据存入数组中，按照Partition的思想排序，插入的时间复杂度为O(1)，输出时间复杂度为O(n)，
#         这里如果使用快排的话，时间复杂度是O(nlogn)
class Solution1(object):
    def __init__(self):
        self.arr = []

    def Insert(self, num):
        self.arr.append(num)

    def GetMedian(self):  # 牛客上需要加一个变量 def GetMedian(self,n = None)这样，我也不知道为啥
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


# 思路三：最炫酷的就是堆
class Solution2(object):

    def __init__(self):
        self.minNums = []
        self.maxNums = []

    def maxHeapInsert(self, num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[int(i)] > self.maxNums[int((i - 1) / 2)]:
                t = self.maxNums[int((i - 1) / 2)]
                self.maxNums[int((i - 1) / 2)] = self.maxNums[int(i)]
                self.maxNums[i] = t
                i = (i - 1) / 2
            else:
                break

    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def minHeapInsert(self, num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[int(i)] < self.minNums[int((i - 1) / 2)]:
                t = self.minNums[int((i - 1) / 2)]
                self.minNums[int((i - 1) / 2)] = self.minNums[int(i)]
                self.minNums[i] = t
                i = (i - 1) / 2
            else:
                break

    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def Insert(self, num):
        if (len(self.minNums) + len(self.maxNums)) & 1 == 0:
            if len(self.maxNums) > 0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums) > 0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)

    def GetMedian(self):  # 牛客上需要加一个变量 def GetMedian(self,n = None)这样，我也不知道为啥
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen == 0:
            return -1
        if allLen & 1 == 1:
            return self.minNums[0]
        else:
            return (self.maxNums[0] + self.minNums[0] + 0.0) / 2


s = Solution2()
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

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


# 思路三：最炫酷的就是堆，具体参考：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/you-xian-dui-lie-python-dai-ma-java-dai-ma-by-liwe/
# 要找出中位数，即当数据流读出的个数为奇数时，中位数是中位数之前的有序树组的最大值，
#                当数据流读出的个数为偶数时，中位数是中位数之前的有序树组的最大值与中位数之后的有序树组的最小值的平均数
#                所以我们可以将前半部分的有序树组动态的放置在一个“大顶堆”中，后半部分放置在“小顶堆”中
#                当数据流中读出的个数为偶数时，让这两部分数组的个数相等，两个顶堆元素的平均值就是中位数
#                                   为奇数时，只要保证大顶堆的元素永远比小顶堆的元素个数多1，则大顶堆的堆顶元素就是中位数
#    时间复杂度O(n),空间复杂度O(n):两个堆的空间复杂度为O(n/2),计数器占用空间O(1)


#  1.python使用heapq包的办法(heapq只能实现小顶堆，所以在实现大顶堆时需要绕个圈圈)
import heapq


class Solution2(object):
    def __init__(self):
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def Insert(self, num):
        self.count += 1
        # print('self.count:', self.count)
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        # 先往大顶堆中存入数字，弹出最大值之后，放入小顶堆，如果count为奇数，则再从小顶堆中弹出放入大顶堆，
        # 这样保证如果是奇数的话，大顶堆中的数据比小顶堆中的多一个，如果是偶数的话，则两个堆中的数据相同
        heapq.heappush(self.max_heap, -num)  # heapq.heappush() 将值推入堆，保持堆不变
        # print('1111111')
        # print('self.min_heap:', self.min_heap)
        # print('self.max_heap:', self.max_heap)
        max_heap_top = heapq.heappop(self.max_heap)  # heapq.heappop() 弹出并从堆中返回最小的项，从而保持堆不变。
        # print('22222222')
        # print('self.min_heap:', self.min_heap)
        # print('self.max_heap:', self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)
        # print('33333333')
        # print('self.min_heap:', self.min_heap)
        # print('self.max_heap:', self.max_heap)
        if self.count & 1:  # &1 代替%2
            min_heap_top = heapq.heappop(self.min_heap)
            # print('min_heap_top:', min_heap_top)
            heapq.heappush(self.max_heap, -min_heap_top)
            # print('44444444')
            # print('self.min_heap:', self.min_heap)
            # print('self.max_heap:', self.max_heap)

    def GetMedian(self):  # 牛客上依旧需要添加一个参数：def GetMedian(self , n = None):
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return -self.max_heap[0]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# 2.纯手写实现：(暂时没整明白)
class Solution3(object):
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def Insert(self, num):
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def GetMedian(self):
        if self.count == 1:
            return self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        length = len(alist)
        if alist is None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] < alist[index + 1]: index += 1
                if temp >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist is None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp


s = Solution3()
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

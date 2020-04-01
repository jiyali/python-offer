class Solution:
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 交换

            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

            # 一个个交换元素
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # 交换
            self.heapify(arr, i, 0)
        return arr


s = Solution()
print(s.heapSort([12, 11, 13, 5, 6, 7]))

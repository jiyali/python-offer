import random
import operator


class Solution:
    def BubbleSort(self, arr):
        if not arr or len(arr) <2:
            return arr

        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def GenerateRandomArr(self, size, value):
        arr = []
        for i in range(size):
            arr.append(random.random() * (value + 1) - random.random() * value)
        return arr

    def rightMathod(self, arr):
        arr.sort()
        return arr

    def isTure(self, times, value, size, func):
        success = True
        for j in range(times):
            arr1 = self.GenerateRandomArr(size, value)
            arr2 = arr1.copy()
            arr3 = arr1.copy()
            func(arr2)
            self.rightMathod(arr3)
            if not operator.eq(arr2, arr3):
                success = False
                print(arr1)
                break
        print("NICE" if success is True else "FUCK!")


s = Solution()
print(s.isTure(5000, 10, 100, s.BubbleSort))

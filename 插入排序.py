# 插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。


class Solution():
    def insertSort(self, arr):
        if not arr or len(arr) < 2:
            return arr

        n = len(arr)
        for j in range(1, n):
            # 控制将拿到的元素放到前面有序序列中正确位置的过程
            for i in range(j, 0, -1):
                # 如果比前面的元素小，则往前移动
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                # 否则代表比前面的所有元素都小，不需要再移动
                else:
                    break
        return arr


s = Solution()
print(s.insertSort([12, 11, 13, 5, 6]))

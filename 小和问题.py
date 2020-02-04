# 在一个数组中，当前一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。
# 小和问题
# 在一个数组中， 每一个数左边比当前数小的数累加起来， 叫做这个数组的小和。 求一个数组
# 的小和。
# 例子：
# [1,3,4,2,5]
# 1左边比1小的数， 没有；
# 3左边比3小的数， 1；
# 4左边比4小的数， 1、 3；
# 2左边比2小的数， 1；
# 5左边比5小的数， 1、 3、 4、 2；
# 所以小和为1+1+3+1+1+3+4+2=16


class Solution:
    def small_sum(self, arr):
        if not arr or len(arr) < 1:
            return 0
        return self.merge_sort(arr, 0, len(arr) - 1)

    def merge_sort(self, arr, left, right):
        if left == right:
            return 0
        mid = (right + left) // 2
        return self.merge_sort(arr, left, mid) + self.merge_sort(arr, mid + 1, right) + self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        help = []
        # p1是左边数组的第一个索引位
        p1 = left
        # p2是右边数组的第一个索引位
        p2 = mid + 1
        res = 0
        while p1 <= mid and p2 <= right:
            res += (right - p2 + 1) * arr[p1] if arr[p1] < arr[p2] else 0
            if arr[p1] < arr[p2]:
                help.append(arr[p1])
                p1 += 1
            else:
                help.append(arr[p2])
                p2 += 1
        while p1 <= mid:
            help.append(arr[p1])
            p1 += 1
        while p2 <= right:
            help.append(arr[p2])
            p2 += 1
        arr[left:right + 1] = help
        return res


s = Solution()
print(s.small_sum([7, 2, 14, 6, 14]))

# 在未排序的数组中找到第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        # return heapq.nlargest(k, nums)[-1]
        if not nums:
            return None
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))

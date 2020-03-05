# 1.判断两个实数区间是否相交
class Solution:
    def OverLap(self, a1, a2, b1, b2):
        if a1 < a2 and b1 < b2:
            if a2 < b1 or a1 > b2:
                return 'No'
            else:
                return 'Yes'


s = Solution()
print(s.OverLap(2, 5, 3, 7))


# 2.假设每包小浣熊干脆面中包含有随机的N张英雄卡之一，
# 集齐一整套N张卡片，预期需要吃掉多少包小浣熊干脆面？请编写一个运行10万次的仿真程序求解
# 3.找出两个数组中所有的相同元素，并存入output数组中
class Solution3:
    def theSameElements(self, nums1, nums2):
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        same = nums1 & nums2
        for i in same:
            res.append(i)
        return res


s = Solution3()
print(s.theSameElements([1, 3, 6, 3, 9, 0], [3, 5, 10, 7, 6]))


# 4. 将16进制的字符串转化为10进制的字符串，例如："40A"=>"1034"
class Solution4:
    def hex2dec(self, s):
        return str(int(s.upper(), 16))


s = Solution4()
print(s.hex2dec('40A'))


# 5.一个长度为N，先升序后降序排列的整数数组，找到其中的最大值，要求时间复杂度不超过O(logN)
class Solution5:
    def findMax(self, nums):
        if not nums:
            return None

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            elif nums[mid] < nums[mid - 1]:
                left = mid + 1
            else:
                right = mid


s = Solution5()
print(s.findMax([2, 4, 6, 8, 10, 9, 5, 3, 1]))


# 6.输入一个长度为5的整型数组，求这5个数的中间值（第三大）
class Solution6:
    def theKthMax(self, nums):
        import heapq

        k = len(nums) // 2 + 1

        heap = [0 for i in range(k)]
        for i in nums:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        return heap[0]


s = Solution6()
print(s.theKthMax([1, 8, 6, 4, 9]))

# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。


class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n <= 1:
            return n

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# 时间复杂度为o(nlogn)的做法:如果后续的元素大于数组末尾的元素，则接在末尾；否则找到第一个大于等于元素的值，然后替换
class Solution1:
    def lengthOfLIS(self, nums):
        if len(nums) < 2:
            return len(nums)
        tail = [nums[0]]
        for i in range(1, len(nums)):
            # 如果后续的元素大于数组末尾的元素，则接在末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            # 找到第一个大于等于元素的值，然后替换
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)


s1 = Solution1()
s2 = Solution()
print(s1.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s2.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

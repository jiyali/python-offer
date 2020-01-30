# 题目： 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#        请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#        你可以假设 nums1 和 nums2 不会同时为空
# 解题分析：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/dong-yong-er-fen-cha-zhao-mo-ban-lai-qiao-miao-jie/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)

        mid = (m + n + 1) // 2

        left = 0
        right = m
        mid1 = (left + right) // 2
        mid2 = mid - mid1

        while left < right:
            if mid1 < m and nums2[mid2 - 1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = mid - mid1

        if mid1 == 0:
            max_of_left = nums2[mid2 - 1]
        elif mid2 == 0:
            max_of_left = nums1[mid1 - 1]
        else:
            max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

        if (m + n) % 2 == 1:
            return max_of_left

        if mid1 == m:
            min_of_right = nums2[mid2]
        elif mid2 == n:
            min_of_right = nums1[mid1]
        else:
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))

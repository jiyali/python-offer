# 题目： 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#        请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#        你可以假设 nums1 和 nums2 不会同时为空


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)

        left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
        mid1 = (left + right) // 2
        mid2 = half_len - mid1

        while left < right:
            if mid1 < len1 and nums2[mid2 - 1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

        if mid1 == 0:
            max_of_left = nums2[mid2 - 1]
        elif mid2 == 0:
            max_of_left = nums1[mid1 - 1]
        else:
            max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

        if (len1 + len2) % 2 == 1:
            return max_of_left

        if mid1 == len1:
            min_of_right = nums2[mid2]
        elif mid2 == len2:
            min_of_right = nums1[mid1]
        else:
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))

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

        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

            # 如果两个都为空的异常处理
        if n2 == 0:
            raise ValueError

        # nums1中index在imid左边的都被分到左堆，nums2中jmid左边的都被分到左堆
        left, right = 0, n1

        # 二分答案
        while left <= right:
            imid = left + (right - left) // 2
            # 左堆最大的只有可能是nums1[imid-1],nums2[jmid-1]
            # 右堆最小只有可能是nums1[imid],nums2[jmid]
            # 让左右堆大致相等需要满足的条件是imid+jmid = m-imid+n-jmid 即 jmid = (m+n-2imid)//2
            # 为什么是大致呢？因为有总数为奇数的情况，这里用向下取整数操作，所以如果是奇数，右堆会多1
            jmid = (n1 + n2 - 2 * imid) // 2

            # 前面的判断条件只是为了保证不会index out of range
            if imid > 0 and nums1[imid - 1] > nums2[jmid]:
                # imid太大了，这是里精确查找，不是左闭右开，而是双闭区间，所以直接移动一位
                right = imid - 1
            elif imid < n1 and nums2[jmid - 1] > nums1[imid]:
                left = imid + 1
            # 满足条件
            else:
                # 边界情况处理，都是为了不out of index
                # 依次得到左堆最大和右堆最小
                if imid == n1:
                    minright = nums2[jmid]
                elif jmid == n2:
                    minright = nums1[imid]
                else:
                    minright = min(nums1[imid], nums2[jmid])

                if imid == 0:
                    maxleft = nums2[jmid - 1]
                elif jmid == 0:
                    maxleft = nums1[imid - 1]
                else:
                    maxleft = max(nums1[imid - 1], nums2[jmid - 1])

                # 前面也提过，因为取中间的时候用的是向下取整，所以如果总数是奇数的话，
                # 应该是右边个数多一些，边界的minright就是中位数
                if ((n1 + n2) % 2) == 1:
                    return float(minright)

                    # 否则我们在两个值中间做个平均
                return (maxleft + minright) / 2.0


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))

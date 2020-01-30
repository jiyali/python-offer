# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


class Solution(object):
    def removeElements(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        思路： 当 nums[j]与给定的值相等时，递增j以跳过该元素。只要 nums[j] != val，我们就复制 nums[j]到 nums[i]并同时递增两个索引。
        重复这一过程，直到 j到达数组的末尾，该数组的新长度为 i。

        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
        return i


s = Solution()
print(s.removeElements([1, 1, 1, 2, 2, 3], 1))

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))

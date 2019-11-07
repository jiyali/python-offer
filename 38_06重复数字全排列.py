class Solution(object):
    def Permutation(self, nums):
        if len(nums) == 0:
            return []

        res = []
        nums.sort()

        def backtrack(nums, tmp):
            if len(nums) == 0:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


nums = [0, 1, 2, 2, 3, 3]
s = Solution()
print(s.Permutation(nums))

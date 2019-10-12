class Solution:
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


class Solution1(object):
    def Permutation(self, nums):
        perms = [[]]

        nums.sort()
        print(nums)

        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return sorted(perms)


nums = [2, 3, 9, 7, 0, 11, 6]
s = Solution()
print(s.Permutation(nums))

class Solution(object):
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

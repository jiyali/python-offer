class Solution:
    def getPermutation(self, n, k):
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        nums = list(range(1, n + 1))

        backtrack(nums, [])
        res.sort()
        return ''.join(list(map(str, res[k - 1])))


s = Solution()
print(s.getPermutation(n=3, k=3))

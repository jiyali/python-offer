# 题目：输入一个含有八个数字的数组, 判断有没有可能把这把个数字分别放到正方体的八个顶点上，
#      使得正方体上三组相对的面上四个顶点的和都相等

# 思路：将八个数全排列，放到正方体的顶点上，判断


class Solution(object):
    def Permutation(self, nums):
        if len(nums) == 0:
            return []

        nums.sort()
        res = []

        def backtrack(nums, tmp):
            if len(nums) == 0:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res

    def compare(self, aList):

        resList = self.Permutation(aList)

        for reslist in resList:
            sum1 = reslist[0] + reslist[1] + reslist[2] + reslist[3]
            sum2 = reslist[4] + reslist[5] + reslist[6] + reslist[7]
            sum3 = reslist[0] + reslist[2] + reslist[4] + reslist[6]
            sum4 = reslist[1] + reslist[3] + reslist[5] + reslist[7]
            sum5 = reslist[0] + reslist[1] + reslist[4] + reslist[5]
            sum6 = reslist[2] + reslist[3] + reslist[6] + reslist[7]

            if sum1 == sum2 and sum3 == sum4 and sum5 == sum6:
                return True
        return False


ss = [2, 3, 9, 7, 0, 11, 2, 6]
ss2 = [1, 1, 1, 1, 1, 1, 1, 1]
s = Solution()
print(s.Permutation(ss))
print(s.compare(ss))

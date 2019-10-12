# 题目：在8*8的国际象棋上摆放八个皇后, 使其不能相互攻击, 即任意两个皇后不得处在同一行, 同一列或者同一对角线上

# 思路：根据题意可知，每一个皇后占据一行，定义一个数组columnIndex表示第i行的皇后所在的列号
#      对数组columnIndex进行全排列，判断每个皇后是否在同一列或者是在对角线上
#      如果在同一列上，则i=j,如果在对角线上，则abs(i-j) = columnIndex(i) - columnIndex(j)


class Solution(object):
    def Permutation(self, nums):

        output = [[]]
        nums.sort()

        for n in nums:
            new_res = []
            for res in output:
                for i in range(len(res)+1):
                    new_res.append(res[:i] + [n] + res[i:])
            output = new_res

            output.sort()

        return output

    def judge(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if i - j == nums[i] - nums[j] or j - i == nums[i] - nums[j]:
                    return False
        return True

    def queen(self, nums):
        aList = self.Permutation(nums)
        for n in aList:
            isQueen = self.judge(n)
            if isQueen is True:
                print(n)


nums = [0, 1, 2, 3, 4, 5, 6, 7]
s = Solution()
print(s.Permutation(nums))
print(s.queen(nums))

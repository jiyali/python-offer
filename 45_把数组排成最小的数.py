# 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#      例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。


# 常规做法就是先对输入数组排列组合，把每组数字拼起来，再比较大小，输出比较小的那个数字
class Solution(object):
    def PrintMinNumber(self, numbers):
        if numbers is None or len(numbers) == 0:
            return ''

        alist = self.Permutation(numbers)
        tmp = []

        for i in range(len(alist)):
            s = ''
            for j in range(len(alist[0])):
                s += str(alist[i][j])
                # s = ''.join(str(n) for n in alist[i])
            tmp.append(s)

        return min(tmp)

    # 对数组进行全排列
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
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res




s = Solution()
print(s.PrintMinNumber([3, 32, 321]))

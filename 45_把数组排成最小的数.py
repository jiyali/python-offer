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


# 第二种方法：将数组中的每一个数字转换成字符串，将他们拼起来，如果字符串a+字符串b组成的数字大于字符串b+字符串a的数字的话，选择较小的拼接方式
from functools import cmp_to_key


class Solution1(object):
    def PrintMinNumber(self, numbers):
        if numbers is None or len(numbers) == 0:
            return ''
        # 直接拼接数字，可能导致数值溢出，这是一个隐形的大数问题，需要把数字转换成字符串
        strList = []
        for i in numbers:
            strList.append(str(i))

        # 比较 x+y 和 x-y 的大小, 因为为str型, 需要先转换成int型
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        strList.sort(key=key)

        return ''.join(strList)


# 如果不借助包的话
class Solution2(object):
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return ''

        strlist = []
        for i in numbers:
            strlist.append(str(i))

        res = self.sort(strlist)

        return ''.join(res)

    def sort(self, numbers):
        if len(numbers) == 0 or len(numbers) == 1:
            return numbers

        temp = numbers[0]
        a = []
        b = []

        for i in range(1, len(numbers)):
            if temp + numbers[i] > numbers[i] + temp:
                a.append(numbers[i])
            else:
                b.append(numbers[i])
        return self.sort(a) + [temp] + self.sort(b)


s = Solution2()
print(s.PrintMinNumber([3, 32, 321]))

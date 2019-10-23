# 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。
#      请写程序找出这两个只出现一次的数字。


class Solution(object):
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp


s = Solution()
print(s.FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5]))





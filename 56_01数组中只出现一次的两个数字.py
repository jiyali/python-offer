# 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。
#      请写程序找出这两个只出现一次的数字。


# 思路一：列表操作，定义一个数组，遍历列表。如果数组中存在该元素就remove，否则append。最后输出数组
#         时间复杂度：O(n^2)。遍历array花费O(n)的时间。
#                            还要在列表中遍历判断是否存在这个数字，花费O(n)的时间，所以总循环时间为O(n^2)
#         空间复杂度：O(n)。需要一个大小为n的列表保存所有的array中元素

class Solution(object):
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array or len(array) == 0:
            return None

        tmp = []

        for i in array:
            if i in tmp:
                tmp.remove(i)
            else:
                tmp.append(i)
        return tmp


# 思路二：哈希表
#        定义一个字典，遍历列表，将列表元素作为key,如果元素存在于字典中就加一，否则键值等于1。
#        对字典遍历，输出键值为1的key。
class Solution1(object):
    def FindNumsAppearOnce(self, array):
        if not array or len(array) == 0:
            return None

        dic = {}

        for i in array:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        tmp = []

        for key in dic:
            if dic[key] == 1:
                tmp.append(key)

        return tmp


# 异或: 相同元素的位运算为0；0与任意整数的异或为该整数。(a xor a) xor b = a xor b xor a = b xor 0 = b
# 分治。遍历列表，对所有元素进行异或，得到两个只出现一次的元素x,y的异或值a。
# 将a进行取反加一，并与a本身相与得到一个mask值，该值与列表中的每一个元素相与的结果可以作为划分数组的判别条件。
# 因为该mask表示了x,y二进制中不同的某一位，并且mask的其他位为0，所以列表中的元素与该值相与为0或者为1就可以将列表划分为两部分。
# 再对每一部分异或就可以得到最终的结果。
class Solution2(object):
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array) == 0:
            return None

        res = 0
        for nu in array:
            res ^= nu

        ans = [0, 0]

        res &= -res

        for nu in array:
            if nu & res == 0:
                ans[0] ^= nu
            else:
                ans[1] ^= nu
        return ans


s = Solution2()
print(s.FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5]))

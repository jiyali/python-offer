#
class Solution:

    def findDuplicate(self, arr):
        # 。这样通过判断元素是否大于等于n就能决定这个元素是未访问过的数据还是已访问过的数据
        if arr is None:
            return []
        n = len(arr)
        flag = False
        res = []

        for i in range(n):
            if arr[i] < n:  # 如果值小于n，则说明第一次访问，查找他相对的那个元素，如果相对元素大于n,则说明找到重复元素，如果不是，则+n
                index = arr[i]
            else:  # 如果值大于n，则继续查找相对元素
                index = arr[i] - n
            if arr[index] >= n:
                flag = True
                res.append(index)
            else:
                arr[index] += n
        if flag is False:
            return []
        return res


s = Solution()
print(s.findDuplicate([4, 1, 3, 5, 5, 2, 0, 0]))

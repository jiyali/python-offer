#
class Solution:

    def findDuplicate(self, arr):
        if arr is None:
            return []
        index = []
        n = len(arr)
        flag = False
        res = []

        for i in range(n):
            if arr[i] >= n:
                index = arr[i] - n
            else:
                index = arr[i]
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

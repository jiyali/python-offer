class Solution:
    def countSort(self, arr):
        # 获取arr中的最大值和最小值
        maxNum = max(arr)
        minNum = min(arr)
        # 以最大值和最小值的差作为中间数组的长度,并构建中间数组，初始化为0
        length = maxNum - minNum + 1
        tempArr = [0 for i in range(length)]
        # 创建结果List，存放排序完成的结果
        resArr = list(range(len(arr)))
        # 第一次循环遍历
        for num in arr:
            tempArr[num - minNum] += 1
        # 第二次循环遍历
        for j in range(1, length):
            tempArr[j] = tempArr[j] + tempArr[j - 1]
        # 第三次循环遍历
        for i in range(len(arr) - 1, -1, -1):
            resArr[tempArr[arr[i] - minNum] - 1] = arr[i]
            tempArr[arr[i] - minNum] -= 1
        return resArr


s = Solution()
print(s.countSort([1, 0, 8, 5, 4, 7, 3, 6, 2, 0]))

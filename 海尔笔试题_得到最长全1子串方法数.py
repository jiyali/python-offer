# 题目：给定一个二进制字符串和整数 K。求得到由 1 组成的最长连续子段的不同方法数目。
#


class Solution:
    # 返回仅包含 1 的最长（连续）子数组的长度
    def getMaxOnes(self, size, allowedChanges, str):
        n = size
        k = allowedChanges
        num = list(map(int, str.split()))

        zeros = res = l = 0
        for r in range(n):
            zeros += 1 - num[r]
            if zeros > k:
                zeros -= 1 - num[l]
                l += 1
            res = r - l + 1
        return res

    # 依次得到最长长度的子串以及是否满足条件可以变成全1子串，返回整个字符串
    def Ways(self, size, allowedChanges, str):
        n = size
        k = allowedChanges
        num = list(map(int, str.split()))

        res = self.getMaxOnes(size, allowedChanges, str)

        left = 0
        right = left + res


        a = []
        count = 0

        while right <= n:
            outputleft=num[0:left]
            #print('111')
            #print(outputleft)
            output=num[left:right]
            #print('222')
            #print(output)

            for i in output:
                #print(i)
                if i == 1:
                    #print('我执行了吗')
                    continue
                else:
                    #print('else执行了吗')
                    count += 1
                    #print(count)
                    if count <= k:
                        output = [1] * res
                        #print('全1执行了吗')
                    else:
                        count = 0
                        #print('else执行了吗')
                        output = num[left:right]


            outputright=num[right:n]
            #print('333')
            #print(outputright)

            #print('44444')
            a.append(outputleft + output + outputright)



            left += 1
            right += 1
        return a

    # 判断是否重复
    def CountWanys(self, size, allowedChanges, str1):
        n = size
        k = allowedChanges
        num = list(map(int, str1.split()))
        if n <= 0:
            return 0
        if n == 1:
            return 1

        alist = self.Ways(size, allowedChanges, str1)

        b = set()

        for i in range(len(alist)):
            s = ''
            for j in range(len(alist[0])):
                s += str(alist[i][j])
            b.add(s)

        return len(b)


s = Solution()
print(s.CountWanys(5, 3, '0 1 0 1 0'))

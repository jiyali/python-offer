# 题目：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
#      其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。


class Solution(object):
    def multiply(self, A):
        if not A:
            return []

        length = len(A)

        B = [1] * length
        for i in range(1, length):
            B[i] = B[i - 1] * A[i - 1]
        tmp = 1
        for i in range(length - 2, -1, -1):
            tmp *= A[i + 1]
            B[i] *= tmp
        return B


test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))


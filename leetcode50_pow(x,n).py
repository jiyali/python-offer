class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickmul(n):
            if n == 0:
                return 1
            y = quickmul(n//2)
            if n % 2== 0:
                return y * y
            else:
                return y*y*x
        if n>=0:
            return quickmul(n)
        else:
            return 1/quickmul(-n)
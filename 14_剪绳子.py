# 题目：给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
#       请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，
#       此时得到的最大乘积是18
# 思路一：动态规划 ，定义函数f(n)为乘积的最大值，在剪第1刀的时候，有n-1种选择，也就是第1刀的长度可能是1,2,……,n-1.
#       第i刀时，有n-i种选择。则f(n)=max(f(i)*f(n-i))


class Solution(object):
    def cutRope(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        max_ls = [0, 1, 2, 3]

        for i in range(4, number + 1):
            max_tmp = 0
            for j in range(1, i):
                max_tmp = max(max_tmp, max_ls[j] * max_ls[i - j])
            max_ls.append(max_tmp)

        return max_ls.pop()


s = Solution()
print(s.cutRope(8))


# 思路二：贪婪算法，

class Solution1(object):
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        if number == 3:
            return 2
        if number == 4:
            return 4
        if number >= 5:
            a = number % 3
            b = number // 3
            if a == 0:
                return 3 ** b
            if a == 1:
                return 3 ** (b - 1)
            else:
                return 3 ** b * 2


s1 = Solution1()
print(s1.cutRope(8))

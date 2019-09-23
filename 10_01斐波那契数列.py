# 使用生成器:输出的是所有的数据，暂时不知道怎么输出指定的某一次迭代的数据
class Solution(object):

    def fib(self, num):
        a, b = 0, 1
        for i in range(num):
            yield a
            a, b = b, a + b


s = Solution()
for n in s.fib(10):
    print(n)


# 使用迭代：输出的是最后一次的数据


class Solution2(object):

    def fib2(self, num1):
        a, b = 0, 1
        for i in range(num1):
            a, b = b, a + b
        return a


print('here')
s1 = Solution2()
print(s1.fib2(10))


# ※推荐！！ 使用迭代 避免重复，时间复杂度O(n)
class Solution3(object):

    def fib3(self, num2):
        a, b = 0, 1
        if num2 == 0:
            return 0
        if num2 == 1:
            return 1
        if num2 >= 2:
            for i in range(num2):
                a, b = b, a + b
        return a


print('here')
s1 = Solution3()
print(s1.fib3(3))

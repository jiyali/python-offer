class Solution(object):

    def jump(self, num):
        a, b = 1, 2
        if num == 1:
            return 1
        if num == 2:
            return 2
        if num >= 3:
            for i in range(3, num + 1):
                a, b = b, a + b
        return b


s = Solution()
print(s.jump(3))
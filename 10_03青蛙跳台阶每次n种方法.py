class Solution(object):

    def jump(self, num):
        if num < 0:
            return 0
        else:
            return pow(2, num - 1)


s = Solution()
print(s.jump(3))

class Solution:
    def seq(self, x):
        if x < 1:
            return x
        cur = x
        while cur > x/cur:
            cur = (cur + x/cur) // 2
        return int(cur)


s = Solution()
print(s.seq(8))

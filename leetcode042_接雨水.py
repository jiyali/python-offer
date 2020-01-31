# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水


class Solution:
    def trap(self, height) -> int:
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]
        total = 0

        while left < right:
            if left_max < right_max:
                left += 1
                cur = height[left]
                if cur > left_max:
                    left_max = cur
                else:
                    total += left_max - cur
            else:
                right -= 1
                cur = height[right]
                if cur > right_max:
                    right_max = cur
                else:
                    total += right_max - cur
        return total


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

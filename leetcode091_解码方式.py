# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 顺序遍历，计算字符串从开始位到当前位的解码方式总数，按照与字符串索引对应的位置存入dp数组
#
# 如果第一个元素等于'0'，直接返回0
# 如果元素长度等于1，直接返回1
# 定义dp数组为[1]，然后从字符串s的第二个字母开始遍历
# 如果第i个元素是‘0’，检查第i-1个元素是不是‘1’或‘2’，如果不是，返回0；如果是，判断一下i是否等于1，来决定dp.append(dp[i-2])或者是dp.append(1) (防止数组越界)
# 如果第i-1个元素是‘1’，或者第i-1个元素是‘2’且第i个原始大于‘0’且小于‘7’：dp.append(dp[i-2]+dp[i-1])
# 其余情况dp.append(dp[i-1])
# 返回s最后一个元素对应的dp值


class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if s[i - 1] == '1' or (s[i - 1] == '2' and '1' <= s[i] <= '6'):
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[-1]


s = Solution()
print(s.numDecodings("226"))


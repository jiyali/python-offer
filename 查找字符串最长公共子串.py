# 请编码实现一个命令行工具，找出指定的2个字符串的最长公共子串。
#
# 输入描述:
# 命令行工具接收两个字符串参数。输入字符串的合法字符集为[a-zA-Z0-9]，大小写敏感，无需考虑异常输入场景。
#
# 输出描述:
# 所找到的公共子串；如果存在多个等长的公共子串，则请按字母序排序，依次打印出所有公共子串，每行一个。
#
# 输入例子1:
# 1234567 12893457


s1, s2 = input().split()
m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]
res = []
max_len = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        if dp[i][j] >= max_len:
            max_len = dp[i][j]
            res.append(s1[i - max_len: i])
res = sorted([x for x in res if len(x) == max_len])
for x in res:
    print(x)


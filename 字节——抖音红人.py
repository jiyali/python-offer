# 题目描述
# 需要找到所有的抖音红人，用户数为N，关注关系有M对。(A,B)代表A关注了B。关注关系具有传递关系，比如有(A,B)(B,C)，那么认为A间接关注了C。如果一个用户被所有N个用户直接或间接关注，那么我们认为这个用户就是抖音红人。求抖音红人的总数。
# 输入：**
# 第一行，整数N
# 第二行，整数M
# 第三行，M*2个整数，代表M个关注关系
# 输出：
# 整数
# 样例输入：
# 3
# 3
# 1 2 2 1 2 3
# 样例输出：
# 1
# 提示：
# 只有3用户，有直接粉丝2，间接粉丝1，所以3用户是唯一的抖音红人。


from collections import defaultdict

# 提交代码时，取消以下注释
##n = eval(input())
##m = eval(input())
##li = list( map(int,input().split()))

# 提交代码时，删除以下代码
n = 3
m = 3
li = [1, 2, 2, 1, 2, 3]

# 测试用例里，用户索引从1开始，本文从0开始
son = defaultdict(list)
fans = [1] * n  # 存直接或间接粉丝，自己也算自己的粉丝，所以初始为1
visited = [False] * n


def findson(origi, i):  # origi代表起点
    for j in son[i]:
        if visited[j] != True:
            fans[origi] += 1
            visited[j] = True
            # print(i,j,visited)
            findson(origi, j)


for i in range(m):
    a = i * 2
    b = i * 2 + 1
    # a关注b
    son[li[b] - 1].append(li[a] - 1)
    # 原输入是123，那么程序里就是012
# 建立好了有向图

for i in range(n):
    visited = [False] * n
    visited[i] = True
    findson(i, i)

count = 0
for i in fans:
    if (i == n):  # 如果粉丝为n
        count += 1
print(count)

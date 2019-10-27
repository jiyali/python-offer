# 给定大小为n的数组A，A中的元素有正有负。请给出方法，对其进行排序
# 排序后的数组保证：
#    1.负数在前面，正数在后面
#    2.正数之间的相对位置不变
#    3.负数之间的相对位置不变
# 输入描述：
#    输入n+1行：第1行为一个整数n，表示数组的长度；第1行到第n+1行每行一个整数，为按序输入的数组元素
# 输入：
#     4
#     -4
#     1
#     -5
#     2
# 输出：
#     -4 -5 1 2


import sys
n = int(sys.stdin.readline().strip())  # 代表长度
array = []  # 表示数组
for i in range(n):
    line = sys.stdin.readline().strip()
    array.append(int(line))
# print(n)
# print(array)

minus_list = []  # 负数
plus_list = []  # 正数

for value in array:
    if value < 1:
        minus_list.append(value)
    else:
        plus_list.append(value)

print(minus_list + plus_list)




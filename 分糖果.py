# n 个小朋友坐在一排，每个小朋友拥有 ai 个糖果，现在你要在他们之间转移糖果，使得最后所有小朋友拥有的糖果数都相同，每一次，你只能从一个小朋友身上拿走恰好两个糖果到另一个小朋友上，问最少需要移动多少次可以平分糖果，如果方案不存在输出 -1。
#
#
# 输入描述:
# 每个输入包含一个测试用例。每个测试用例的第一行包含一个整数n（1 <= n <= 100），接下来的一行包含n个整数ai（1 <= ai <= 100）。
#
# 输出描述:
# 输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出-1。
#
# 输入例子1:
# 4
# 7 15 9 5
#
# 输出例子1:
# 3


def main():
    n = input()
    n = int(n)

    s = input().split()
    nums = []
    for i in s:
        nums.append(int(i))

    sum_ = sum(nums)
    average = int(sum_ / n)
    # print(average)
    count = 0

    if sum_ % n != 0:
        return -1
    for i in range(n):
        d = abs(nums[i] - average)
        if d % 2 != 0:
            return -1
        count += (d / 2)
    return int(count / 2)


print(main())

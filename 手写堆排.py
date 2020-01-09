def heap_sort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆  例子中对应 6—10对
    n = len(arr)
    # 最后一个非叶子节点
    first = int(n / 2 - 1)  # 例子中对应01234 第五个数 角标为4
    # 构造大根堆
    for start in range(first, -1, -1):  # 循环到第4,3,2,1,0个
        max_heapify(arr, start, n - 1)  # 排序一次的结果

    # 堆排，将大根堆转换成有序数组 # 将最大的放到堆的最后一个, 堆大小-1, 继续调整排序
    for end in range(n - 1, 0, -1):  # 剩下9次 循环987654321
        arr[end], arr[0] = arr[0], arr[end]
        max_heapify(arr, 0, end - 1)  # 注意start=0
    return arr


# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(arr, start, end):
    root = start  # 例子中我们看到第一次root是6这个数
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1  # 例子中child对应10这个数
        if child > end:  # 后面可以看出堆的大小在减小
            break

        # 找出两个child中较大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if arr[root] < arr[child]:
            # 最大堆root小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]

            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候, 退出
            break


def main():
    # [7, 95, 73, 65, 60, 77, 28, 62, 43]
    # [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(l)
    heap_sort(l)  # 调用
    print(l)


if __name__ == "__main__":
    main()

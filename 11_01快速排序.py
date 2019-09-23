# 方法一：先选择第一个元素作为基准值，分为小于基准值的部分和大于基准值的部分，然后对这两部分分别以第一个元素为基准值递归
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([30, 24, 5, 58, 18, 36, 12, 42, 39]))

# 方法二：选择任意一个数作为基准
from random import *


def quicksort1(array):
    if len(array) < 2:
        return array
    else:
        pivot = choice(array)

        less = [i for i in array if i < pivot]

        greater = [i for i in array if i > pivot]

        return quicksort1(less) + [pivot] * array.count(pivot) + quicksort1(greater)


print(quicksort1([30, 24, 5, 58, 18, 36, 12, 42, 39]))
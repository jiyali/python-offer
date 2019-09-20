# 不修改数组，找出数组中重复的元素
def duplicate(numbers):
    if numbers is None or len(numbers) == 0:
        return False
    left = 0
    right = len(numbers)
    while left < right:
        mid = left + (right + 1 - left) // 2
        count = countNum(numbers,right,left,mid)
        if left == right:
            if count > 1:
                print(True)
                return True
            else:
                break
        if (mid - left + 1) < count:
            left = mid
        else:
            right = mid - 1
    return False


def countNum(numbers,right,left,mid):
    count = 0
    for i in range(right):
        print(numbers[i])
        if numbers[i] < 1 or numbers[i] > right:
            return False
        if left <= numbers[i] <= right:
            count += 1
    return count

print(duplicate(numbers = [4,2,3,1,2,5]))

# # 第二种方式哈希表 需要额外的空间，空间消耗为O(n)
# import numpy as np
#
#
# def HashFind(a):                        #哈希表 需要额外的空间，空间消耗为O(n)
#     num_array = np.zeros(len(a))
#     for i in range(len(a)):
#         if num_array[a[i]] == 0:
#             num_array[a[i]] += 1
#         else:
#             return a[i]
#
# #二分法查找统计思想
# #数值范围1-n，一共n-1个数字
# #循环实现,循环改变索引值进行二分：
# def getDuplication(a):
#     m = len(a)
#     startN = 1      #列表数值范围最小值
#     endN = m      #列表数值范围最大值
#
#     while startN <= endN:
#         midN = (startN+endN)>>1     #二分法中间值
#         numbers = 0
#         for i in range(m):
#             if (a[i]<= midN) & (a[i]>= startN):
#                 numbers += 1
#         if numbers > (midN - startN+1):     #关键(midN - startN+1)，如果没有重复元素，startN与midN范围间相差的数字个数
#             startN, endN = startN, midN
#         else:
#             startN, endN = midN+1, endN
#         if startN == endN:                  #最后判断数组出现的次数
#             number = 0
#             for j in a:
#                 if j ==startN:
#                     number += 1
#             if number > 1:
#                 return startN
#             else:
#                 break
#     return False
#
# if __name__ == "__main__":
#     Lst2 = [2,2,3,4,6,6]
#     Lst3 = [1,2,3,4,6,4,6]
#     Lst4 = [2,5,4,2,5,3]
#     Lst5 = [1, 0]
#     print(Lst2)
#     print("----------------------------------------")
#     #print(HashFind(Lst2))
#     print(getDuplication(Lst2))

# 题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
#      输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
#      例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
#      NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# 思路：使用二分法，但是考虑到[1, 0, 0, 1]这种数据，只能顺序查找
#       旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。
#       如果中间点大于首元素，说明最小数字在后面一半，如果中间点小于尾元素，说明最小数字在前一半。依次循环。
#       同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。


class Solution:
    def minNumberInRotateArray(self, numbers) :
        if not numbers:
            return None

        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = left + (right - left) // 2
            if numbers[right] > numbers[mid]:
                right = mid
            elif numbers[right] < numbers[mid]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]


Test = Solution()
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))

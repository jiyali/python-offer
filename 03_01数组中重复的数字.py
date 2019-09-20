# 找出数组中重复的数字
# 思路：从下标0开始，对每个元素，若numbers[i]不等于i，则交换numbers[i]和numbers[numbers[i]]，
#      直至i和numbers[i]相等继续循环，或numbers[i]和numbers[numbers[i]]相等即遇到重复元素返回True
# 时间复杂度O(n），空间复杂度O(n)
def duplicate(numbers,duplication):
    if numbers is None or len(numbers) == 0:
        return False
    for i in numbers:
        if i < 0 or i >= len(numbers):
            return False

    for i in range(len(numbers)):
        while i != numbers[i]:
            if numbers[i] == numbers[numbers[i]]:
                duplication.append(numbers[i])
                break
            else:
                tmp = numbers[numbers[i]]
                numbers[numbers[i]] = numbers[i]
                numbers[i] = tmp
    return duplication

print(duplicate(numbers=[2, 3, 1, 0, 2, 5, 3, 7, 9, 10, 7],duplication=[]))
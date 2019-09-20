# 二维数组查找指定数字
def Find(array,target):
    if array is None or len(array) == 0:
        return False
    row = 0
    col = len(array[0]) - 1
    while row <= len(array) or col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

print(Find(array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],target = 2))
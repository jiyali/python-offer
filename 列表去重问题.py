# 内置函数set去重,不保证顺序
list1 = [2, 1, 3, 4, 1]
print(list(set(list1)))

# 使用字典的fromkeys()去重
list2 = [2, 1, 3, 4, 1]
print({}.fromkeys(list2).keys())

# 使用常规的方法去重
list3 = [2, 1, 3, 4, 1]
tmp = []
for i in list3:
    if i not in tmp:
        tmp.append(i)
print(tmp)

# 使用排序去重
list4 = [2, 1, 3, 4, 1]
print(sorted(set(list4), key=list4.index))

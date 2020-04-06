class Solution:
    def dicSort(self, dic):
        dic = sorted(dic.items(), key=lambda x: x[1])
        return dic

# 第一个参数是需要排序的列表，第二个参数是指定key（列表中每一项的第几个元素）来进行排序。
# d.items()返回的是一个列表 [('a', 56), ('b', 23), ('c', 90), ('d', 12), ('e', 64), ('f', 41), ('g', 88)]
# sorted会对d.items()这个list进行遍历，把list中的每一个元素，也就是每一个tuple()当做x传入匿名函数lambda x：x[1],函数返回值为x[1],
# 也就是key=x[1]=tuple()[1]=('a', 74)[1]也就是说按照里表中每个项的第二个元素进行排序（第一个是想x[0]）


s = Solution()
print(s.dicSort({"a": 56, "b": 23, "f": 41, "c": 90, "d": 12, "e": 64, "g": 88}))

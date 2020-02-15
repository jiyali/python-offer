# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 列表中的每一项或者为一个整数，或者是另一个列表


class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self.recursion(nestedList)

    def recursion(self, nestList):
        for i in range(len(nestList) - 1, -1, -1):
            if nestList[i].isInteger():
                self.stack.append(nestList[i].getInteger())
            else:
                self.recursion(nestList[i].getList())

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数(时间复杂度应为O(1))。
# 思路：引入两个栈，一个栈每次push实际的数字，另一个minStack栈每次push最小值，
#       如果push的数字小于minStack栈顶的数字，minStack栈中push新的数字，
#       反之，把栈顶的数字再压入一遍。


class Solution(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        # write code here
        if self.stack == [] or self.minStack == []:
            return None

        self.minStack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]


S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
S.push(0)

print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())

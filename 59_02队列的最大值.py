# 题目：请定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back和pop_front的时间复杂度都是O(1)


class Solution:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push_back(self, num):
        self.stack.append(num)

        while self.maxStack and num > self.maxStack[-1]:
            self.maxStack.pop()

        self.maxStack.append(num)

    def pop_front(self):
        if self.stack is None:
            return None
        if self.stack[0] == self.maxStack[0]:
            self.maxStack.pop(0)
        self.stack.pop(0)

    def max(self):
        return self.maxStack[0]


# 网上的另一个做法

from collections import deque


class Solution1(object):
    def __init__(self):
        self.data = deque()
        self.max_queue = deque()
        self.current_index = 0

    def push_back(self, num):
        while len(self.max_queue) != 0 and num >= self.max_queue[-1][1]:
            self.max_queue.pop()
        self.max_queue.append((self.current_index, num))
        self.data.append((self.current_index, num))
        self.current_index += 1

    def pop_front(self):
        assert len(self.data) != 0
        index, num = self.data.popleft()
        if index == self.max_queue[0][0]:
            self.max_queue.popleft()

    def max(self):
        assert len(self.data) != 0
        return self.max_queue[0][1]


s = Solution()
s.push_back(3)
print(s.max())
s.push_back(3)
print(s.max())
s.push_back(1)
print(s.max())
s.push_back(2)
print(s.max())
s.pop_front()
print(s.max())
s.pop_front()
print(s.max())
s.push_back(4)
print(s.max())

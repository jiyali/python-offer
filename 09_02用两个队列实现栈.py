# 思路： 两个先进先出的队列实现后进先出的栈，
#        如果第一个队列为空的话，添加元素，输出第n个元素时，将第n-1个元素压入第二个队列，然后输出第一个队列中剩下的元素
#        反之亦然


class Solution(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        if not self.queue2:
            self.queue1.append(data)
        else:
            self.queue2.append(data)

    def pop(self):
        if not self.queue1 and not self.queue2:
            return None
        if self.queue1:
            length = len(self.queue1)
            for i in range(length - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            length = len(self.queue2)
            for i in range(length - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()


P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())
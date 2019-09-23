# 思路： 用两个先入后出的栈实现先入先出的队列，一个栈负责入栈，一个栈负责出栈
#        入栈时在stack1中插入元素，出栈时，如果stack2为空，则将stack1中的元素压入Stack2，然后弹出stack2中的元素

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        self.stack1.append(data)

    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return False
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


P = MyQueue()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
print('here1')
P.push(13)
print(P.pop())
print('here2')
print(P.pop())
print('here3')
print(P.pop())
print('here4')
print(P.pop())
print('here5')

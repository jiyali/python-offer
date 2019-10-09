# 题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
#       返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
# 思路：第一步：在每个原始节点后面复制这个节点，并用next将这2n个节点串起来
#       第二步：复制random指针，指向原始random指针所指向的后一个节点
#       第三步：拆分原始链表和复制链表


class RandomListNode(object):
    def __init__(self, data):
        self.label = data
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None

        self.CloneNodes(pHead)
        self.CloneRandomNodes(pHead)
        return self.ReconnextedNodes(pHead)

    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pClone = RandomListNode(0)
            pClone.label = pNode.label
            pClone.next = pNode.next
            pClone.random = pNode.random
            pNode.next = pClone
            pNode = pClone.next

    def CloneRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random is not None:
                pClone.random = pNode.random.next
            pNode = pClone.next

    def ReconnextedNodes(self, pHead):
        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)

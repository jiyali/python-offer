# 题目：输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
# 思路一：可以借助列表insert方法，每次在位置0处插入数据
#         先入后出类似于栈，从头到尾遍历链表，用栈存储每个节点的值，之后出栈输出值即可


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def printList(self, listnode):
        if listnode.data is None:
            return False
        l = []
        head = listnode

        while head:
            l.insert(0, head.data)
            head = head.next
        return l


node1 = Node(11)
node2 = Node(13)
node3 = Node(15)
node1.next = node2
node2.next = node3

s = Solution()
print(s.printList(node1))

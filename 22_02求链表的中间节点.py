# 题目：求链表的中间节点，如果总结点数为奇数就是中间那个，如果是偶数就返回中间两个节点的任意一个。


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def FindMidNode(self, head):
        if head is None:
            return None

        node1 = head
        node2 = head

        while node1 is not None and node1.next is not None:
            node1 = node1.next.next
            node2 = node2.next
        return node2


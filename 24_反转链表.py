# 题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def ReverseList(self, pHead):
        if pHead is None:
            return None

        node_prior = None
        node = pHead

        while node is not None:
            node_next = node.next
            node.next = node_prior
            node_prior = node
            node = node_next
        return node_prior


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
print(S.ReverseList(node1).val)

# 题目：将两个有序链表合并为一个新的有序链表并返回。
#      新链表是通过拼接给定的两个链表的所有节点组成的


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(1)
node5 = ListNode(2)
node6 = ListNode(4)
node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6

s = Solution()
print(s.mergeTwoLists(node1, node4).val)

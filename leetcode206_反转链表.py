# 题目：反转一个单链表。


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.nexT = None


class Solution(object):
    # 迭代
    def reverseList(self, head):
        if head is None:
            return None

        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    # 递归
    def reverseList1(self, head):
        if not head:
            return None
        if not head.next:
            return head

        cur = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return cur

        


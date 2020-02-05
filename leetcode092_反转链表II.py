# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。


class ListNode():
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def reverseBetween(self, head, m, n):
        pre = pre_head = ListNode(0)
        pre.next = head

        for i in range(m - 1):
            head = head.next
            pre = pre.next

        for j in range(n - m):
            tmp = head.next
            head.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return pre_head.next

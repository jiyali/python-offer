# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。


class ListNode():
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution():
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy  # 反转点前一个

        for i in range(m - 1):
            head = head.next
            pre = pre.next
        # pre是反转点前一个, head是反转点
        for i in range(n - m):
            nxt = head.next  # 记录反转点后一个
            head.next = nxt.next  # 反转nxt和head
            nxt.next = pre.next  # 重新链接
            pre.next = nxt

        return dummy.next
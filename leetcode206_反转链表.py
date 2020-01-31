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
        


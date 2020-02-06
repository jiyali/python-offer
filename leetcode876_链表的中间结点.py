# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def middleNode(self, head):
        if not head:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

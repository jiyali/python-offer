# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle1(self, head):
        if not head or not head.next:
            return None
        dic = {}
        node = head
        while node:
            if dic.get(node, 0) != 0:
                return True
            else:
                dic[node] = 1
            node = node.next
        return False

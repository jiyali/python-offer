# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环


class Solution:
    def hasCycle(self, head):
        if not head and not head.next:
            return None

        p1 = head
        p2 = head.next
        while p1 != p2:
            if p2 is None or p2.next is None:
                return False
            p1 = p1.next
            p2 = p2.next.next
        return True

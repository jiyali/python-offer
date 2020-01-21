# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def deleteDuplicates(self, head):
        pre = None
        cur = head
        while cur:
            if pre and pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


s = Solution()
print(s.deleteDuplicates())
# 题目：删除链表中重复的节点
#       在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
#       例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead

        pNext = pHead.next

        if pNext.val != pHead.val:
            # 当前节点和下一个节点不相同，所以当前节点不删除，递归找下一个节点
            pHead.next = self.deleteDuplication(pNext)

        else:
            while pHead.val == pNext.val and pNext.next is not None:
                pNext = pNext.next
            if pNext.val != pHead.val:
                # 当前节点和下一个节点不相同，但是pHead是重复节点，所以递归找当前节点
                pHead = self.deleteDuplication(pNext)
            else:
                return None
        return pHead
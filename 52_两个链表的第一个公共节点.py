# 题目：输入两个链表，找出它们的第一个公共节点。
# 思路一：先遍历一下两个 链表，得到各自的节点数。然后让长的那个链表的head指针先走节点数差值次。
#         然后两个指针一起往后走，第一次遇到相同的节点就是第一个公共节点。


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution(object):
    def FindFirstCommonNode(self, pHead1, pHead2):
        nlength1 = self.GetListLength(pHead1)
        nlength2 = self.GetListLength(pHead2)
        nlegthDiff = abs(nlength1 - nlength2)

        if nlength1 > nlength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1

        for i in range(nlegthDiff):
            pListHeadLong = pListHeadLong.next

        while pListHeadLong is not None and pListHeadShort is not None and pListHeadShort != pListHeadLong:
            pListHeadShort = pListHeadShort.next
            pListHeadLong = pListHeadLong.next

        pFirstCommonNode = pListHeadLong
        return pFirstCommonNode

    def GetListLength(self, pHead):
        nlength = 0
        while pHead is not None:
            pHead = pHead.next
            nlength += 1
        return nlength
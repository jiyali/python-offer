# 题目：输入两个链表，找出它们的第一个公共节点。
# 思路一：先遍历一下两个 链表，得到各自的节点数。然后让长的那个链表的head指针先走节点数差值次。
#         然后两个指针一起往后走，第一次遇到相同的节点就是第一个公共节点。


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution(object):
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        length1 = self.GetListNodeLength(pHead1)
        length2 = self.GetListNodeLength(pHead2)
        lengthDiff = abs(length1 - length2)

        if length1 > length2:
            pHeadLong = pHead1
            pHeadShort = pHead2
        else:
            pHeadLong = pHead2
            pHeadShort = pHead1

        for i in range(lengthDiff):
            pHeadLong = pHeadLong.next

        while pHeadLong is not None and pHeadShort is not None and pHeadLong != pHeadShort:
            pHeadLong = pHeadLong.next
            pHeadShort = pHeadShort.next

        return pHeadLong

    def GetListNodeLength(self, pHead):
        length = 0

        while pHead is not None:
            pHead = pHead.next
            length += 1

        return length

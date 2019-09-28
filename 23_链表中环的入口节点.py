# 题目：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
# 书上思路：判断链表中是否存在环，还是需要定义两个指针，第一个指针的速度较快，第二个指针的速度较慢，
#       如果走得快的指针追上了走的慢的指针说明存在环
#       如果走得快的指针走到了链表的结尾也没追上走得慢的指针，说明不存在环


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)

        if not meetingNode:
            return None

        num = 1

        flagNode = meetingNode

        while flagNode.next != meetingNode:
            num += 1
            flagNode = flagNode.next

        pFast = pHead
        pSlow = pHead

        for i in range(num):
            pFast = pFast.next

        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast

    def MeetingNode(self, pHead):
        if pHead is None or pHead.next is None or pHead.next.next is None:
            return None
        if pHead.next == pHead:
            return pHead
        pFast = pHead.next.next
        pSlow = pHead

        while pFast != pSlow:
            if pFast.next.next is not None:
                pSlow = pSlow.next
                pFast = pFast.next.next
            else:
                return None
        return pFast



# 一个比较简单的思路：建一个列表，将节点依次放入列表中，如果有一个节点已经在列表中出现过了，说明这个节点就是环的入口


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution1(object):
    def EntryNodeOfLoop(self, pHead):
        nodelist = []
        node = pHead
        while node is not None:
            if node in nodelist:
                return node
            else:
                nodelist.append(node)
            node = node.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s1 = Solution1()
print(s1.EntryNodeOfLoop(node1).val)

s = Solution()
print(s.EntryNodeOfLoop(node1).val)

# 题目：在O(1)时间内删除链表节点
# 思路：常规删除链表中的某个节点的操作为：假设要删除的节点为j,与j相邻的节点为i,k
#       从头遍历链表，找到要删掉节点(j)的前一个节点(i)，将这个节点的next指针指向要删除的下一个节点(k),然后删除j
#       但是常规做法的时间复杂度为O(n)
#   ※ 时间复杂度为O(1)的做法是：直接将要删除节点(j)的下一个节点(k)的值和next指针复制给要删除节点(j)，然后删除要删除的节点(j)即可


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        self.data = None
        self.next = None


class Solution(object):
    def deletNode(self, pListHead, pToBeDelete):

        if not pListHead or not pToBeDelete:
            return

        if pToBeDelete.next is not None:
            pNext = pToBeDelete.next
            pToBeDelete.data = pNext.data
            pToBeDelete.next = pNext.next
            pNext.__del__()

        elif pListHead == pToBeDelete:
            pToBeDelete.__del__()
            pListHead.__del__()

        else:
            pNode = pListHead
            while pNode.next != pToBeDelete:
                pNode = pNode.next
            pNode.next = None
            pToBeDelete.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()

S.deletNode(node1, node3)
print(node3.data)
S.deletNode(node1, node3)
print(node3.data)
print(node2.data)
S.deletNode(node1, node1)
print(node1.data)
S.deletNode(node1, node1)
print(node1.data)

# 找出单向链表中的一个节点，该节点到尾指针的距离为K。链表的倒数第0个结点为链表的尾指针。要求时间复杂度为O(n)。
# 链表结点定义如下：
# struct ListNode
# {
#     int m_nKey;
#     ListNode* m_pNext;
# }
# 链表节点的值初始化为1，2，3，4，5，6，7。
# 输入描述:
# 该节点到尾指针的距离K
# 输出描述:
# 返回该单向链表的倒数第K个节点，输出节点的值


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def findKthFromEnd(self, head, k):
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow.next


head = Node(0)
tmp = head
for i in range(1, 8):
    node = Node(i)
    tmp.next = node
    tmp = node
k = int(input())
s = Solution()
print(s.findKthFromEnd(head, k).val)

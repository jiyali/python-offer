# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
#
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
#
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
#
# 返回一个符合上述规则的链表的列表。
#
# 举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def splitListToParts(self, root, k):
        cur = root
        length = 0
        res = []

        while cur:
            length += 1
            cur = cur.next

        avg = length // k  # 获取每个key的节点数
        ext = length % k  # 计算平均以后剩余的数量，然后把剩余的数量发放到每个节点

        for i in range(k):
            res.append(root)
            if root:
                for j in range(1, avg + (i < ext)):
                    root = root.next
                tmp = root.next
                root.next = None
                root = tmp
        return res

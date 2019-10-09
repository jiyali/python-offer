import copy


class RandomListNode(object):
    def __init__(self, data):
        self.label = data
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        return copy.deepcopy(pHead)


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)

class RandomListNode(object):
    def __init__(self, data):
        self.label = data
        self.next = None
        self.random = None


class Solution(object):
    def Clone(self, pHead):

        if pHead is None:
            return None

        pNode = pHead

        nodeList = []
        randomList = []
        labelList = []

        while pNode:
            nodeList.append(pNode)
            randomList.append(pNode.random)
            labelList.append(pNode.label)
            pNode = pNode.next

        # 设置random节点的索引
        labelIndexList = list(map(lambda x: nodeList.index(x) if x else -1, randomList))

        pClone = RandomListNode(0)

        nodeList = list(map(lambda x: RandomListNode(x), labelIndexList))

        for i in range(len(nodeList)):
            if labelIndexList[i] != -1:
                nodeList[i].random = nodeList[labelIndexList[i]]
        for i in nodeList:
            pClone.next = i
            pClone = pClone.next
        return pClone.next


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)


class RandomListNode(object):
    def __init__(self, data):
        self.label = data
        self.next = None
        self.random = None


class Solution(object):
    def Clone(self, pHead):

        pNode = pHead

        nodeList = []  # 存放各个节点
        randomList = []  # 存放各个节点指向的random节点。没有则为None
        labelList = []  # 存放各个节点的值

        while pNode:
            nodeList.append(pNode)
            randomList.append(pNode.random)
            labelList.append(pNode.label)
            pNode = pNode.next

        # 设置random节点的索引，没有则设置为-1
        labelIndexList = list(map(lambda x: nodeList.index(x) if x else -1, randomList))

        pClone = RandomListNode(0)
        pCloneNode = pClone

        # 设置节点列表
        nodeList = list(map(lambda x: RandomListNode(x), labelList))

        # 绑定每个节点的random
        for i in range(len(nodeList)):
            if labelIndexList[i] != -1:
                nodeList[i].random = nodeList[labelIndexList[i]]
        for i in nodeList:
            pCloneNode.next = i
            pCloneNode = pCloneNode.next
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


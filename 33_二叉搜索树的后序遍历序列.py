# 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
#       如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# 思路：根据后序遍历，尾元素一定是根节点
#       再根据二叉搜索树的性质：左子节点的元素一定小于根节点，右子节点的元素一定大于根节点
#       递归比较左右子树书否符合此特性


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        root = sequence[-1]

        if min(sequence) > root or max(sequence) < root:
            return False

        index = 0

        for i in range(len(sequence) - 1):
            index = i
            if sequence[i] > root:
                break

        for j in range(index + 1, len(sequence) - 1):
            if sequence[j] < root:
                return False

        # 递归检查左子树是否是二叉搜索树
        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        # 递归检查右子树是否是二叉搜索树
        right = True
        if index < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[index: len(sequence) - 1])
        return left and right


array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))

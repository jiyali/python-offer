# 根据逆波兰表示法，求表达式的值。
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

# 使用栈来存储，遍历整个list，遇到运算符，出栈两个元素并进行计算，计算结果继续入栈
# 时间复杂度O(N)，空间复杂度O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                if i == '+':
                    stack.append(left + right)
                elif i == '-':
                    stack.append(left - right)
                elif i == '*':
                    stack.append(left * right)
                elif i == '/':
                    stack.append(int(left / right))
        return stack[0]
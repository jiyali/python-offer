# 题目：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
# 思路：判断链表中是否存在环，还是需要定义两个指针，第一个指针的速度较快，第二个指针的速度较慢，
#       如果走得快的指针追上了走的慢的指针说明存在环
#       如果走得快的指针走到了链表的结尾也没追上走得慢的指针，说明不存在环


class Solution(object):
    def EntryNodeOfLoop(self, pHead):
# 题目：输入数字n，按顺序打印出从1到最大的n位十进制数。


# 思路一： 最普通的方法：计算出最大的数，然后挨个输出即可（python语言的优点，数字没有上限，可以直接打印，
#          但是对于其他语言而言当n非常大的时候可能会溢出）
class Solution(object):
    def print1ToMax(self, n):

        if n <= 0:
            return -1

        endnum = int('1' + '0' * n)

        for i in range(endnum):
            print(i)


s = Solution()
s.print1ToMax(3)


# 思路二：大数问题：用字符串模拟加法来解决
#         将字符串初始化全0，每次为字符串表示的数字+1，再打印出来


class Solution1(object):
    def print1ToMax(self, n):

        if n <= 0:
            return -1

        ListNum = ['0'] * n

        while self.Increament(ListNum) is False:
            self.PrintNum(ListNum)

    def Increament(self, number):
        # 两个重要的标志位：溢出和进位
        isOverFlow = False
        isTakeOver = 0

        Length = len(number)
        n = Length - 1

        while n >= 0:
            # 将当前n位置的字符转换成数字，如果满足进位则加上进位
            nSum = int(number[n]) + isTakeOver

            # 实现模拟加法
            if n == Length - 1:  # 判断当前n是不是在最低位，也就是个位
                nSum += 1  # 如果在个位，则自增1

            if nSum == 10:  # 进位
                if n == 0:  # 判断是否溢出
                    isOverFlow = True
                    return isOverFlow
                else:  # 如果不是溢出，进位
                    isTakeOver = 1  # 进位标志位置1
                    number[n] = '0'  # 将当前位置的数字归‘0’
            else:
                number[n] = str(nSum)
                break

            n -= 1  # n向前移动，观察更高位是否也满足进位
        return isOverFlow

    def PrintNum(self, number):
        for i in range(len(number)):
            if number[i] != '0':
                print(''.join(number[i:]))
                break


s = Solution1()
s.print1ToMax(3)


# 思路三： 转换为数字排列的递归


class Solution3(object):
    def Print1ToMax(self, n):
        if n <= 0:
            return

        ListNum = ['0'] * n

        for i in range(10):
            ListNum[0] = str(i)
            self.Print1ToMaxCore(ListNum, n, 0)

    def Print1ToMaxCore(self, number, length, index):
        if index == length - 1:
            self.PrintNumber(number)
            return
        for i in range(10):
            number[index + 1] = str(i)
            self.Print1ToMaxCore(number, length, index + 1)

    def PrintNumber(self, number):
        for i in range(len(number)):
            if number[i] != '0':
                print(''.join(number[i:]))  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
                break


s = Solution3()
print('here')
s.Print1ToMax(3)

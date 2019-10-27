# 题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
#      例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
#      那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
#      针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}，
#      {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

# 思路：双端队列。用一个叫window的队列存储当前滑动窗口中可能是最大值的索引。
#      首先用一个while循环把窗口范围之前的值去掉，然后删除掉window中对应值小于当前值的那些值
#      （因为先要要append进来的值比他们来得晚而且还比他们大，因此那些值永远无出头之日，删掉即可）。
#      然后把当前值添加 到window中。每次把window中的第0个元素在num中的值添加到res中。最后返回res即可。


class Solution(object):
    def maxInWindows(self, num, size):
        if not num or len(num) == 0 or size <= 0:
            return []

        res = []
        window = []

        for i in range(len(num)):

            # 考虑什么时候，要把最大移除
            # 左边界划出的时候，应该是 window.pop(0)
            # [0,1,2,3,4]
            #     [    i]
            # window[0] == i - k 这个条件特别容易忽略
            if i >= size and window[0] == i - size:
                window.pop(0)
            # 考虑把不可能是最大的元素全部 kill 掉
            while window and num[i] >= num[window[-1]]:
                window.pop()
            # 不管怎么着都加当前的索引
            window.append(i)

            # 什么时候有滑动窗口呢？
            if i >= size - 1:
                res.append(num[window[0]])
        return res


class Solution1:
    def maxInWindows(self, num, size):
        """算法一样，但是更简洁"""
        if len(num) == 0 or size <= 0 or len(num) < size:
            return []
        result = []
        window_max = max(num[0:size])
        result.append(window_max)
        for i in range(size, len(num)):
            if num[i] > window_max:
                window_max = num[i]
            elif num[i - size] == window_max:  # 这个是要出来的
                window_max = max(num[i - size + 1:i + 1])
            result.append(window_max)

        return result


s = Solution1()
print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))

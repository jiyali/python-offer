import sys


def permute(nums):
    res = []

    def backtrack(nums, tmp):
        if not nums:
            # print(tmp)
            sum_ = 0
            for i in tmp:
                # print('i', i)
                if sum_ + int(i) < 0:
                    return
                else:
                    res.append(tmp)
                    # print('res', res)
                    return
        for i in range(len(nums)):
            backtrack(nums[: i] + nums[i + 1:], tmp + [nums[i]])
            # print(nums)

    backtrack(nums, [])
    print(res)
    return len(res)


for line in sys.stdin:
    a = line.split()
    nums = ['-1', '1'] * int(a[0])
    # print(nums)
    print(permute(nums))

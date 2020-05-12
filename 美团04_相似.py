n = int(input())
nums = [int(tmp) for tmp in input().strip().split()]
result = [-1] * n
for i in range(n):
    if result[i] != 1:
        for j in range(n):
            if i != j and nums[i] & nums[j] == 0:
                result[i] = 1
                result[j] = 1
                break
res = ''
for i in range(n):
    res += str(result[i]) + ''
print(res)

arr = [1, 2, 4, 1, 7, 8, 3]


def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i - 1)
        return max(A, B)


def dp_opt(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
    return dp[len(arr) - 1]


print(rec_opt(arr, 6))
print(dp_opt(arr))

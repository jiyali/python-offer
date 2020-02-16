arr = [3, 34, 4, 12, 5, 2]
s = 9


def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr, i-1, s)
    else:
        A = rec_subset(arr, i-1, s - arr[i])
        B = rec_subset(arr, i-1, s)
        return A or B


print(rec_subset(arr, len(arr) - 1, 9))


def dp_subset(arr, s):
    if len(arr) == 1:
        return arr[0] == s
    elif s == 0:
        return True

    dp = ([0] * len(arr) for _ in range(len(arr)))
    



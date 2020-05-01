import sys

def combine(n, k):
    if k > n or k == 0:
        return []
    res = []

    def backtrack(start=1, tmp=[]):
        if len(tmp) == k:
            res.append(tmp[:])
            return
        for i in range(start, n + 1):
            tmp.append(i)
            backtrack(i + 1, tmp)
            tmp.pop()

    backtrack()
    return len(res)


for line in sys.stdin:
    a = line.split()
    n = a[0]
    k = a[1]

    print(combine(5, 3) % 3)

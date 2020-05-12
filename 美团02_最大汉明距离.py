n = int(input())
l = list(map(int, input().split()))
l = l[:n]
max_value = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        c = bin(l[i] ^ l[j]).count('1')
        if c > max_value:
            max_value = c
print(max_value)

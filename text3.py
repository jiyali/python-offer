import sys


def gray_code(n):
    if n == 1:
        return ['0', '1']
    else:
        l = gray_code(n-1)
        return ['0'+x for x in l]+['1' + x for x in l[::-1]]


for line in sys.stdin:
    a = line.split()
    n = len(a[0])

    list = gray_code(n)

    for i in range(len(list)):
        if list[i] == a[0]:
            print(i+1)

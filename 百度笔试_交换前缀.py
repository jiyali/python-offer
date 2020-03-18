string = input()
n = int(string.split(" ")[0])
m = int(string.split(" ")[1])
string = []
print(n, m)
for i in range(0, n):
    string.append(input())
print(string)


def main(string, n, m):
    s = set()
    res = 1
    for j in range(m):
        s.clear()
        for i in range(n):
            s.add(string[i][j])
            print(s)
            res = len(s) * res % 1000000007
    return res


print(main(string, n, m))

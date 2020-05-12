a = list(map(int, input().split()))
student = a[0]
major = a[1]
get_ward = [0] * student
all = []
for _ in range(student):
    score = list(map(int, input().split()))
    all.append(score)

for i in range(major):
    max_value = 0
    max_index = []
    for j in range(student):
        if all[j][i] > max_value:
            max_index = [j]
            max_value = all[j][i]
        elif all[j][i] == max_value:
            max_index.append(j)
    for k in max_index:
        get_ward[k] = 1
print(sum(get_ward))

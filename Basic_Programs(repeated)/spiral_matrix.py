a = [[1, 2, 3, 4], [5, 6, 7], [8, 7, 9]]
l = []

for i in range(len(a[0])):
     l.append(a[0][i])

for j in range(1, len(a) - 1):
     l.append(a[j][-1])

for k in range(1, len(a[-1]) + 1):
     l.append(a[-1][-k])

for m in range(len(a[1])):
    l.append(a[1][m])

print(l)

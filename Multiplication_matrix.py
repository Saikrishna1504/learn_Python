m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[7, 8], [9, 10], [11, 12]]
m3 = []
for i in range(len(m1)):
    row = []
    for j in range(len(m2[0])):
        total = 0
        for k in range(len(m1[0])):
            total += m1[i][k] * m2[k][j]
        row.append(total)
    m3.append(row)
for row in m3:
    print(row)
  

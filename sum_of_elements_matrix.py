matrix = [
     [1 ,2 ,3],
     [4 ,5 ,6],
     [7 ,8 ,9]
]
sum_of_elements = 0
for row in matrix:
     for elementS in row:
          sum_of_elements += elementS
print("sum of elements in matrix",sum_of_elements)

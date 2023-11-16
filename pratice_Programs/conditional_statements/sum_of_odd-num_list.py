n = [2, 5, 3, 2, 6, 7, 34, 1]
sum_odd = 0
for num in n:
    if num % 2 != 0:
        sum_odd += num
print("The sum of odd numbers is:", sum_odd)

n=int(input("enter the n value"))
sum_of_digits=0
while n>0:
    i = n%10
    sum_of_digits += i
    n //= 10
print("sum of digits", sum_of_digits)

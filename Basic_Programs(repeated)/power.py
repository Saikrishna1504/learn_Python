base=int(input("enter the base value: \n"))
power=int(input("enter the power value: \n"))
result=1
for element in range (power):
    result= result * base
print("Result is: ",result)

import math
a=int(input("enter a first number"))
b=int(input("enter a second number"))
lcm = (a*b)//math.gcd(a,b)
print("lcm of a and b is", lcm)

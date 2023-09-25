import math
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

gcd = math.gcd(n1, n2)

lcm = (n1 * n2) // gcd

print("GCD of", n1, "and", n2, "is:", gcd)
print("LCM of", n1, "and", n2, "is:", lcm)

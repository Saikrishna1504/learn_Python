import math
n = int(input("enter n value\n"))
sqr = math.isqrt(n)
if sqr*sqr==n:
    print(n, "is a prefect square")
else:
    print(n, "is not a perfect square")

def is_happy(n):
     seen = set()
     while n != 1 and n not in seen:
          seen.add(n)
          n=sum(int(digit)**2 for digit in str(n))
     return n == 1
n = int(input("enter n number"))
if is_happy(n):
     print("is a happy number",n)
else:
     print("is not a happy number",n)



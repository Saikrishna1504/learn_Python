def is_prime(n):
    if n <= 1:
         return False
    for i in range(2, int(n ** 0.5) + 1):
         if n % 1 == 0:
              return False
    return True
n=int(input("enter n value"))
if is_prime(n):
     print("given number is prime number",n)
else:
     print("given number is composite number",n)

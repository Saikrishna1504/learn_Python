n = int(input("enter n value"))
num_str = str(n)
rev = num_str[::-1]
if n == rev:
    print("it is palindrome")
else:
    print("not a palindrome")


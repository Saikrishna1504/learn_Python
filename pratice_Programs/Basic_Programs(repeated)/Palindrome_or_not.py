 def is_palindrome(num):
    my_string = str(num)
    if my_string == my_string[::-1]:
        print("is a palindrome")
    else:
        print("is not a palindrome")

n = int(input("Enter a number: "))
is_palindrome(n)


/*  OR  */


def is_palindrome(n):
    org = n
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    if org == rev:
        print(f"{org} is a palindrome")
    else:
        print(f"{org} is not a palindrome")

n = int(input("Enter a number: "))
is_palindrome(n)

# Finding legnth of given setence
print(len("Hi,Welcome to metaverse")) // len function won't work for int data type.

# Storing len function
length=len("Hi,Welcome to metaverse")
print("it has " +"str(length)"+ " characters")
print(type(length)) // for checking which data type it is.

# Exercise 
// adding  digits of given number

num = input("enter two digit number")
first_no=num[0]
second_no=num[1]
print(int(first_no) + int(second_no))

# Operators
a = 5
a += 2 | a %=2 | a //=2 | a -=2 | a *=2
print(a)  // we can assign and add any in same way.
print(a<5) --> False
print(a>5) --> False
print(a=5) --> True 
print(a!=5) --> False

# Adders using operators
a = 5
b = 5
print(id(a))  //if both are same data type = store in same adders else it will store in different adders
print(id(b))
print(a is b)
output--> will ba same adders and final condition is true

# Membership Operators
string="Sai Krishna"
print('a' in string) ---> True

# Exercise problem
w=int(input("enter weight of body")
h=float(input("enter height of a person")
bmi = w / h **2
print(bmi)

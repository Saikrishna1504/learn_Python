#
# Basic_print_statements
print("Hello World!!") //no need of semi-column or double doubts .

# Exercise_1
print("Hello World")
print("welcome to basics")
print("thank you")

// all these print statements will print in diff lines .

# Print(string) inside print statement
print("print('Hello World!!')")

# Print multiple lines in single statement
print("hello\nworld\nthank you") // you can give space to print space.

# String manipulation
print("Hello" + "World")  // output--> HelloWorld
print("Hello " + "World") // output-->Hello World
print("Hello" + " World") // output-->Hello World
print("Hello" + " " + "World") // output-->Hello World

# Input function
print(input("what's your name"))
print("Hi " + input("enter name"))
print(int("enter value"))  // can use any data type instead of int.

# Variables
A = input("enter name")
print(A)

A =input("enter name")
B =input(" enter your greetings")
print( A + B) // Both need to be same data type for + operater ...else u can take 1 variable as input and assign another variable directly ,since input be consider as string type.


# Exercise_2
// swapping of numbers with temp operator

a = input("enter a value")
b = input("enter b value")
temp = a
a = b
b = temp
print("a",a)
print("b",b)

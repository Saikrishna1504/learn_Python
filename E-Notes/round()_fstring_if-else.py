# Round functions
print(round(7)) ---> 7
print(round(7.6)) ---> 8
print(round(7.5)) ---> 8 // it will always try to choose nearest even number wen tie-breaker happens.
print(round(7.6665,2)) ---> 7.67
print(round(674,-3)) ---> 1000 // inverse from 0 to thousand's position
print(round(1.5475,-2)) ---> 1.55
print(round(-2.5)) ---> -2 
print(round(-3.5)) ---> -4 // round near to even numbers

# f strings
name = sai
height = 185
age = 19
print("my name is",name, "i am ",age,"years old","my height is",height,"cm") //Normal way.using fstring is alternative and efficient way
print(f"my name is {name} , i am {age} years old , my height is {height} cm") // use f and we can type in single line
print(f"my age is {age*2}") // we can use operates too

# Exercise
age=int(input("enter age"))
years_left = 90 - age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52
print(f"Time left in years{years_left},days{days_left},months{months_left},weeks{weeks_left}")


# if else conditions
age=int(input("enter age"))
if(age>18):
    print("you are eligible for voting")   // can add multiple print statemenst under singal if or else statemment
else:
    print("not eligibile")   // indentation is important,with it means it print like normal statement

# Exerice {odd or even number}
n = int(input("enter a number"))
if n % 2 ==0:
    print(n,"is even number")
else:
    print(n,"is odd number")


# Nested if else & elif statement
height = int(input("enter your height in feets"))
if height>=4:
    print("you can ride")
    age = int(input("enter your age"))
    if age>=18:                        // only this if statement comes ,wen above if statement satify condition
        print("pay 30 rs")
    else:                              // we can write mulitple condition inside another condition = nested statement
        print("pay 15 rs)
else:                                  // Directly comes to here wen first if condition is false
    print("you can't ride")            


age = int(input("enter age"))
if age = 10:
    print("pay 35 rs")
elif age < 10:
    print("pay 10 rs")
else:                                  // It comes to else when both if and elif fails
    print("pay 50 rs")

# Exercise
w=float(input("enter weight of body"))
h=float(input("enter height of a person"))
bmi = w / h ** 2
if bmi < 18.5:
    print("you are under weight)
elif bmi < 25:
    print("you are normal weight")
elif bmi < 35:
    print("you are obese")
else:
    print("you are clinically obeses")

# Another Exercise
year = int(input("enter a years"))
if year % 4 == 0:                    // we can simple write in single lines,but here me trying to do with nested statemnet
    if year % 100 == 0:  
        if year % 400 == 0:
            print("it's a Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")   
else:
    print("its not a leap year")

# Multiple if statement 
We use multiple if statements within same indentataion if we wanna verify all statements even if before statement is true.

# Excerise
size = input("What size pizza do you want (S/M/L)? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small pizza price is 100 rs")
elif size == 'M' or size == 'm':
    bill += 150
    print("Medium pizza price is 150 rs")
else:
    bill += 300
    print("Large pizza price is 300 rs")

add_pepperoni = input("Do you want pepperoni (Y/N)? ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50

extra_cheese = input("Do you want extra cheese (Y/N)? ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20

print(f"Your final price is {bill} rs.")

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


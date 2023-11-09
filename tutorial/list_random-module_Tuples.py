# Lists
n = [1,2,3,4,5] // int data type
names = ["sai","krishna","ram"] // string
mixed_list = [1,"sai",True,1010,"krish"] // different types of data also possible in lists

// Index always starts from 0.(count starts from 0 in programming)
print (n) ---> [1,2,3,4,5]
print(n[3]) ---> 4
print(n[9]) ---> End up with index error
print(len(n)) ---> 5 
print(n[-1]) ---> 5

# List slicing
n = [10,0,-1,7]
print(n[0:4]) // print(n[:]) // print(n[0:]) ---> [10,0,-1,7]
print(n[1:3]) ---> [0,-1] // here 1 is index and 3 is len(asscending order)
print(n[:3]) ---> [1,2,3] // it print upto len
print(n[0:4:2]) ---> [10,3,5]  // third element refers to skipping of numbers

# pre-defined functions
n = [1,5,3,6,-2,3]
n.sort()  // accending order and we can't include sort in print statemnt.mix_list can't be used with sort
n.reverse() // reverse of a list
print(n) 
print(min(n)) // minimum number will be printed
print(max(n)) // max number will be printed
n.append(89) ---> [1,5,3,6,-2,3,89] //  will be added into last element of list
n.insert(3,69) ---> [1,5,3,69,-2,3,89] // here 2 is index where we want to insert 
n.extend([4,6,98,75]) ---> [1,5,3,6,-2,3,4,6,98,75] // can extend the list ,more than one element
n[2] = 53 ---> [1,5,53,6,-2,3] // replace element at particular index
n[1:3] = [23,65] ---> [1,23,65,6,-2,3] // multiple elemenets at once amd here 3 is len asuaul
n.remove(5) ---> [1,3,6,-2,3] // nukes the value from it
n.remove(3) ---> [1,5,6,-2,3] // we have two 3's .so, it nuked first occurance
n.pop() ---> [1,5,3,6,-2] // nukes last element
n.pop(2) ---> [1,5,6,-2,3] // nuke by using index with pop commands

# Random Modules-predefined
a=random.randint(1,7) // will print random number including a,b .example here it is 1,7
a=random.randrang(1,7) // will print random number including a .example here it is 1
a=random.randome() // will print random floating number from 0-1 in range
a=random.uniform(1,4) // will print random floating number from rang a,b i.e. 1,4 here
print(a)
q=[3,49,-35,235,6,414]
a=random.choice(q)
print(a) // it will print a random numbers from an  given list
q=[3,49,-35,235,6,414]
random.shuffle(q)
print(a) // it will print a list after shuffling all elements

# Exercise --->(heads and tails)
import random
a=random.randint(1,2)
print(a)
if a == 1:
    print("it is heads")
else:
    print("it is tails")

# Nested Lists
l=[2,5,3,[634,46,86],24]
print(len(l)) ---> 5 // inside list is considered as single element in address and there by it slipts
print(l[4])  ---> 24
print(l[3][1]) ---> 46
print(l[-2]) ---> [634,46,86]
print(l[3][0:2]) ---> [634,46] // slicing concept here :2 is len
print(l[3][::2]) --->[634,86]  // stepping based in len


# Tuples
tuple1 = (1,2,-7,4,3) //we use () instead of [] here
tuple2 = (2,) // , is mandatory even if we initiate one elements else read as assign
print(type(tuple1)) ---> tuple
print(tuple1[2]) ---> -7 //index as same as list which starts from 0
tuple_mix = (12,9,-31,'saikrishna',True,23) // different types in tuple possible
// insert,deletion,remove etc.. functions not supported in tuples 

# Tuple slicing
tuple1 = (12,9,-31,'saikrishna',True,23,29,'krish')
print(tuple[1:]) --->(9,-31,'saikrishna',True,23,29,'krish') // same as list ,here 1 is index
print(tuple[:3]) ----> (12,9,-31) //here 3 is length
print(tuple[::2]) ---> (12,-31,True,29,'krish') // step skips

# Extra Tuple stuff
tuple1=(1,2,-7,4,3)
print(len(tuple1)) ---> 5 //finding length of 

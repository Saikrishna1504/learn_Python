# Sets
set1 = {2,4,2,4,6,24,7,}
set2 = {}
set3 = set()
print(set1) //outside wont be in order or we can't acces index and we can't change elements in sets
print(type(set1)) ---> set
print(type(set2)) ---> dict
print(type(set3)) ---> set
set1.add(99)
print(set1) --->{2,4,2,4,7,6,99,24}
print(len(set1)) --->6 // no duplicates allowed
set1.remove(24) ---> {2,4,2,4,7,6,99}
set1.discard(99)
print(set1) // if elemets = remove else just ignore and print same
set1.clear()
print(set1) ---> set() // empty set
set1.pop()
print(set1) // randomly removes 1 elements
set1.add(13,53,4)
print(set1) ---> {2,4,2,(13,53,4),4,7,6,99} // cant be changed


# for loop
name = 'sai krishna'
for i in name:
    print(i)   // will print letter by letter .indentation should be 4 spacing

list1 = [2,5,3,6]
squae = [ ]
for i in list1:
    sqr = i**2
    square.append(sqr)
    print(sqr)  // will print squares one by one
print(square) // will print in list






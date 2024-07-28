random_list = ['H','E','L','L','O']
frequency = {}
for item in random_list:
     if item in frequency:
          frequency[item] += 1
     else:
          frequency[item] = 1
print(frequency)

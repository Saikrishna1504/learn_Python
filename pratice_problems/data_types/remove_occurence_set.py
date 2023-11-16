my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2
my_list = [item for item in my_list if item != element_to_remove]
print("List after removing", element_to_remove, ":", my_list)

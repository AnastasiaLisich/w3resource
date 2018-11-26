# Write a Python program to clone or copy a list
import copy

list_of_elements = ['hello', 135, 'winter', 789]
list_of_elements2 = []

for elem in list_of_elements:
    list_of_elements2.append(elem)

print(list_of_elements2)


list(list_of_elements)
list_of_elements[:]
list_of_elements.copy()
copy.copy(list_of_elements)
copy.deepcopy(list_of_elements)
[x for x in list_of_elements]

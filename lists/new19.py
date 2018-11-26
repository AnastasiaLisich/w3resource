 # Write a Python program to get the difference between the two lists.

list1 = [1, 2, 5]
list2 = [2, 4]
# list3 = []

# for elem in list1:
#    if elem not in list2:
#        list3.append(elem)

print(list(set(list1) - set(list2)))


# Write a Python program to remove duplicates from a list.

list1 = [1, 3, 5, 7, 5, 6, 7, 5]

list2 = []

for elem in list1:
    if elem not in list2:
        list2.append(elem)
print(list2)

# Alternative solution:
list2 = list(set(list1))


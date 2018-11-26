# Write a Python program to flatten a shallow list.

lists = [['a', 'b', 2],['e', 'm', 0],[],[100, '^^^', 30],[1, 1]]

the_list = []

for sublist in lists:
    the_list.extend(sublist)

print(the_list)

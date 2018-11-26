# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

lst1 = ['Winter', 'Snowballs', 'Santa', 31, 1, 'We wish u a Merry Christmas', 365, 'and a', 'Happy New Year', 364]

lst2 = lst1[1:4] + lst1[6:]

print(lst2)

for index in [5, 4, 0]:
    del lst1[index]
    # lst1.pop(index)
print(lst1)



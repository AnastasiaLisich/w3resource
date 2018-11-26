# Write a Python program to remove duplicates from a list.


elements0 = ['a', 'a', 'b', 'c', 'e', 'c']

elements = []

for temp in elements0:
    if temp not in elements:
        elements.append(temp)

print(elements)

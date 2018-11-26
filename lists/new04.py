# Write a Python program to get the smallest number from a list.

elements = [-100, 0, -1000, -5, -10, 0]

num = None
for temp in elements:
    if num is None:
        num = temp
    if temp < num:
        num = temp

print(num)

print(min(elements))


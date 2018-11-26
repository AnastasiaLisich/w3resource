# Write a Python program to generate
# and print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included)

l1 = range(1, 31)
l2 = [x ** 2 for x in l1][5:]
print(l2)


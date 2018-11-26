# # Write a Python program to generate and print a list of first
# and last 5 elements where the values are square of numbers between 1 and 30 (both included)

l1 = [x ** 2 for x in range(1, 31)]
l2 = l1[:5] + l1[-5:]
print(l2)

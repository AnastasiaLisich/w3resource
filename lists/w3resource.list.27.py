# Write a Python program to find the second smallest nuber in a list.
import random

# x = [random.randint(-100, 100) for _ in range(10)]
x = [1, 1, 1, 1]

minm = None
prev_min = None
for current in x:
    if minm is None or current < minm:
        prev_min = minm
        minm = current
    elif (prev_min is None and current != minm) or minm < current < prev_min:
        prev_min = current

print(x)
print(prev_min, minm)





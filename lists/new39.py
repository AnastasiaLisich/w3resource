# Write a Python program to convert a list of multiple integers into a single integer.

integers = [11, 55, 90]

sing_int = ''

for number in integers:
    sing_int += str(number)

print(sing_int)

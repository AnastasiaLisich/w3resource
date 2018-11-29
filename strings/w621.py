# Write a Python program to compute sum of digits of a given string.

string = '2, 6, 9, 16, -50, 2.6'
digits = '0123456789'

list_of_digits = []

for digit in string:
    if digit in digits:
        list_of_digits.append(int(digit))

print(sum(list_of_digits))

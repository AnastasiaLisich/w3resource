# Write a Python program to compute sum of numbers of a given string.

string = '2, 6, 9, 16, -50, 2.6'
list_of_numbers = string.split(', ')
list_of_numbers2 = []

for number in list_of_numbers:
    list_of_numbers2.append(float(number))

print(sum(list_of_numbers2))

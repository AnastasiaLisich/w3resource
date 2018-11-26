# Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are same from a given list of strings.
# plus: add all of those elements to the new list

list_of_strings0 = ['aba', 'ama', 'acn', 'yyy', '', '123', '121']

number = 0
list_of_strings1 = []
for temporary in list_of_strings0:
    if len(temporary) >= 2 and temporary[0] == temporary[-1]:
        number += 1
        list_of_strings1.append(temporary)

print(number)
print(list_of_strings1)

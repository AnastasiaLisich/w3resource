# Write a Python program to insert an element before each element of a list.


the_list = ['a', 'b', 'c', 'd']
element = 'X'

# ['X', 'a', 'X', 'b', 'X', 'c', 'X', 'd']

result = []

for letter in the_list:
    result.append(element)
    result.append(letter)

print(result)

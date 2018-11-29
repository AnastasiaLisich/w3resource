# Write a Python program to move spaces to the front of a given string.

spaces = '  Hello  there, beauty !'

front_spaces = ''
the_other_elements = ''

for element in spaces:
    if element == ' ':
        front_spaces += element
    else:
        the_other_elements += element

ans = front_spaces + the_other_elements

print(ans)


answer = ' ' * spaces.count(' ') + spaces.replace(' ', '')
print(answer)


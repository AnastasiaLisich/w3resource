# Write a Python program to swap comma and dot in a string.

string = 'Haha, haha, hahaha...ha!'

t = ''
for letter in string:
    if letter == '.':
        t += ','
    elif letter == ',':
        t += '.'
    else:
        t += letter

print(t)


answer = string.replace(',', '*').replace('.', ',').replace('*', '.')

print(answer)



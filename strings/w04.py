# Write a Python program to get a string
# from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself.

a = 'kddemmkk'
a = ''

first = a[0]

buff = first
for letter in a[1:]:
    if letter == first:
        buff += '$'
    else:
        buff += letter
    # buff += '$' if letter == first else letter

print(buff)

answer = a[0] + a[1:].replace(a[0], '$')
print(answer)

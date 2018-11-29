# Write a Python program to lowercase first n characters in a string.

string = 'MISty MAgic Forest'
n = 3


def lowercase(string, n):
    new_string = ''
    for letter in string[:n]:
        new_string += letter.lower()
    return new_string + string[n:]

print(lowercase(string, n))

answer = string[:n].lower() + string[n:]
print(answer)

# Write a Python function to convert a given string
# to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

string = 'aRachUUU'
string1 = ''

def upper_letters(any_str):
    t = 0
    for letter in any_str[:4]:
        if letter == letter.upper():
            t += 1
    if t >= 2:
        return any_str.upper()
    else:
        return any_str


print(upper_letters(string))
print(upper_letters(string1))

# Write a Python function to get a string made of its first three characters
# of a specified string. If the length of the string is less than 3 then return the original string.

string = 'Made in China'

def changed_string(any_str):
    # if len(any_str) < 3:
    #     return any_str
    return any_str[:3]

print(changed_string(string))

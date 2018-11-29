 # Write a Python function to get a string made of 4 copies
 # of the last two characters of a specified string (length must be at least 2).

string2 = 'Bo'
string3 = 'Bobby'

def multiple(any_str):
    if len(any_str) < 2:
        raise Exception('your string is too short')
    else:
        return any_str[-2:] * 4


print(multiple(string2))
print(multiple(string3))

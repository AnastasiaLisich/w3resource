# Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with 'ing'
# then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

str1 = 'Jumping'
str2 = 'Badly'
str3 = 'OK'
str4 = 'ing'
str5 = 'OKOKOK'
str6 = 'OKOKOKlykokoko'

def changed_string(any_str):
    if len(any_str) <= 3:
        return any_str
    if any_str[-3:] == 'ing':
        return any_str[:-3] + 'ly'
    if any_str[-2:] == 'ly':
        return any_str[:-2] + 'ing'
    return any_str + 'ing'


# def changed_string_kk(any_str):
#     if len(any_str) <= 3:
#         return any_str
#     if any_str.endswith('ing'):
#         return any_str.rsplit('ing', 1)[0] + 'ly'
#     if any_str.endswith('ly'):
#         return any_str.rsplit('ly', 1)[0] + 'ing'
#     return any_str + 'ing'


print(changed_string(str1))
print(changed_string(str2))
print(changed_string(str3))
print(changed_string(str4))
print(changed_string(str5))
print(changed_string(str6))
